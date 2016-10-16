import numpy as np
import tqdm
import main
max_k = 100
k = max_k + 1
N = 1000000
cars = np.array([main.fective_car])
res = []
for i in tqdm.tqdm(range(N)):
    if i % int(N / 10) == 0:
        res.append(len(cars))
    k += 1
    if (np.random.random_integers(0, 1) == 1 and k > max_k):
        cars = np.concatenate((cars, [[0, 0, main.get_speed()]]))
        k = 0
    cars = main.update_cars_fast(cars)
res.append(len(cars))
print(res)
res = []
max_k = 100
k = max_k + 1
N = 1000000
cars = np.array([main.fective_car])
for i in tqdm.tqdm(range(N)):
    if i % int(N / 10) == 0:
        res.append(len(cars))
    k += 1
    if (np.random.random_integers(0, 1) == 1 and k > max_k):
        cars = np.concatenate((cars, [[0, 0, main.get_speed()]]))
        k = 0
    cars = main.update_cars_slow(cars)
res.append(len(cars))
print(res)