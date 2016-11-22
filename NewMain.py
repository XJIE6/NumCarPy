import Map
import Car
import God

map = Map.Map.get_map()
god = God.God(map)


import tqdm
import numpy as np
import main

max_k = 100
k = max_k + 1
N = 100000
res = []
for i in tqdm.tqdm(range(N)):
    if i % int(N / 10) == 0:
        res.append(len(map[0].cars))
    k += 1
    if (np.random.random_integers(0, 1) == 1 and k > max_k):
        map[0].add(Car.Car(main.get_speed(), 0, 0))
        k = 0
    god.update()
res.append(len(map[0].cars))
print(res)