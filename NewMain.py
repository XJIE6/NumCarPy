import Map
import Car
import God
import tqdm
import random
import Drawer
import pygame
import sys


window_len = 1000
size = (window_len, 800)
screen = pygame.display.set_mode(size)
pygame.init()


map = Map.Map.get_map()
god = God.God(map)
drawer = Drawer.Drawer(map, (0, 0), 40, screen)
clock = pygame.time.Clock()

paths = [
    [map[12], map[0], map[6], map[2], map[4]],
    [map[13], map[6], map[2], map[4], map[0]],
    [map[15], map[2], map[4], map[0], map[6]],
    [map[14], map[4], map[0], map[6], map[2]],

    [map[13], map[1], map[5], map[3], map[7]],
    [map[12], map[5], map[3], map[7], map[1]],
    [map[14], map[3], map[7], map[1], map[5]],
    [map[15], map[7], map[1], map[5], map[3]],
]

def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

N = 10000000
car = None
for i in tqdm.tqdm(range(N)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if i % 100 == 0:
        car = Car.Car(random.randint(10, 20), 0, 0, paths[random.randint(0, 7)].copy(), rand_color(), )
        car.start()
    god.update()
    drawer.draw()
    pygame.display.flip()
    clock.tick(1000)


# path = [map[0], map[6], map[2], map[4]]
# car = Car.Car(30, 0, 0, path)
# car.start()
# while (Map.Map.DEAD.count == 0):
#     print(car.x)
#     god.update()


# import tqdm
# import numpy as np
# import main
#
# max_k = 100
# k = max_k + 1
# N = 100000
# res = []
# for i in tqdm.tqdm(range(N)):
#     if i % int(N / 10) == 0:
#         res.append(len(map[0].cars))
#     k += 1
#     if (np.random.random_integers(0, 1) == 1 and k > max_k):
#         map[0].add(Car.Car(main.get_speed(), 0, 0))
#         k = 0
#     god.update()
# res.append(len(map[0].cars))
# print(res)