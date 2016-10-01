import numpy as np
import math
import pygame

pygame.init()
done = False
window_len = 1000
size = (window_len, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
cars = [[10000, 0]]

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

def draw_car(x):
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
    #dummy version
    if (cars == []):
        return []
    res = [cars[0]]
    for i in range(len(cars)):
        if i != 0:
            cur = model_func(cars[i], cars[i - 1])
            if (cur[0] <= window_len):
                res.append(cur)
    return res
k = 31
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    k += 1
    if (np.random.random_integers(0, 1) == 1 and k > 30):
        cars.append([0, 0])
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
