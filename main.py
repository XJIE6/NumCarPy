import numpy as np
import math
import pygame

pygame.init()
done = False
window_len = 1000
size = (window_len, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

fective_car = [10000, 0]
cars = np.array([fective_car])

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

def draw_car(x):
    if (x >= 0 and x <=window_len):
        pygame.draw.rect(screen, BLACK, [x, 390, 40, 20], 0)



time = 1
v0 = 20.0
T = 1.5
a = 1.0
b = 3.0
sigma = 4
s0 = 20
l = 40

def model_func(cur, next):
    xc = cur[0]
    vc = cur[1]
    xn = next[0]
    vn = next[1]
    sc = xn - xc - l
    s = (s0 +
         vc * T +
         vc * (vc - vn) / (2 * math.sqrt(a * b))
         )
    ac = a * (
        1 -
        (vc / v0) ** sigma -
        (s / sc) ** 2
    )
    return [xc + vc * time, vc + ac * time]

def update_cars(cars):
    if (cars.size == 0):
        return []
    s = cars.compress([1, 0], axis=1).squeeze(1)
    s1 = s[1:]
    s2 = s[:-1]
    v = cars.compress([0, 1], axis=1).squeeze(1)
    v1 = v[1:]
    v2 = v[:-1]
    res_x = np.add(s1, np.multiply(v1, time))
    s_star = np.add(
        np.add(
            np.divide(
                np.multiply(
                    np.subtract(v1, v2),
                    v1),
                2 * math.sqrt(a * b)),
            np.multiply(v1, T)),
        s0)
    func_result = np.multiply(
        a,
        np.subtract(
            1,
            np.subtract(
                np.power(
                    np.divide(v1, v0),
                    sigma),
                np.power(
                    np.divide(
                        s_star,
                        np.subtract(
                            np.subtract(s2, s1),
                            l)),
                    2))))

    res_v = np.add(v1, np.multiply(func_result, time))
    res_x = np.extract(np.subtract(res_x, window_len) <= 0, res_x)
    res_x = np.extract(res_x >= 0, res_x)
    if (res_x.size != 0):
        res_v = res_v[-res_x.size:]
    else :
        res_v = []
    ans = np.column_stack((res_x, res_v))
    if  (ans.size == 0) :
        return np.array([fective_car])
    return np.concatenate(([fective_car], ans))

    '''
    #dummy version
    res = [cars[0]]
    for i in range(len(cars)):
        if i != 0:
            cur = model_func(cars[i], cars[i - 1])
            if (cur[0] <= window_len):
                res.append(cur)
    return res
    '''

k = 31
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    k += 1
    if (np.random.random_integers(0, 1) == 1 and k > 30):
        cars = np.concatenate((cars, [[0, 0]]))
        print(cars)
        k = 0
    print(cars)
    cars = update_cars(cars)

    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, [0, 300, 1000, 200], 0)
    for car in cars:
        draw_car(car[0])

    pygame.display.flip()
    clock.tick(100)

pygame.quit()