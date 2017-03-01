import Map
import Car
import God
import tqdm
import random

k = 10
l = 20000

map = Map.Map.get_test_map(k, l)
god = God.God(map)

print(len(map))

path = [[map[0]], [map[1]]]

for i in range(k):
    print(i)
    path[0].append(map[i * 7 + 6])
    path[0].append(map[i * 7 + 8])

    path[1].append(map[i * 7 + 3])
    path[1].append(map[i * 7 + 5])


N = 100000
car = None
for i in tqdm.tqdm(range(N)):
    if i % 100 == 0:
        car = Car.Car(random.randint(10, 20), 0, 0, path[random.randint(0, 1)].copy())
        car.start()

    god.update()
