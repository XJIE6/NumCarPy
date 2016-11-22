import Object
from functools import reduce
import math
import numpy as np
import Car


def union(tuple: tuple) -> Car:
    if tuple[0] == God.INF:
        return God.INF
    else:
        tuple[0].update(tuple[1], tuple[2])
        return tuple[0]

def add_inf(res: [Car], arr: [Car]) -> [Car]:
    res.append(God.INF)
    res.extend(arr)
    return res

class God:
    INF = Car.Car(0, 1000000000, 0, [])
    TIME = 0.3
    T = 1.5
    A = 1.0
    B = 3.0
    SIGMA = 4
    S0 = 20
    L = 40

    def __init__(self, map: [Object]) -> ():
        self.map = map

    def move(self, cars: [Car]) -> ():
        if len(cars) == 0:
            return []

        v0 = list(map(lambda car: car.max_v, cars))
        s  = list(map(lambda car: car.x, cars))
        v  = list(map(lambda car: car.v, cars))

        v0 = v0[1:]
        s1 = s[1:]
        s2 = s[:-1]
        v1 = v[1:]
        v2 = v[:-1]

        res_x = np.add(s1, np.multiply(v1, God.TIME))
        s_star = np.add(
            np.add(
                np.divide(
                    np.multiply(
                        np.subtract(v1, v2),
                        v1),
                    2 * math.sqrt(God.A * God.B)),
                np.multiply(v1, God.T)),
            God.S0)
        func_result = np.multiply(
            God.A,
            np.subtract(
                1,
                np.add(
                    np.power(
                        np.divide(v1, v0),
                        God.SIGMA),
                    np.power(
                        np.divide(
                            s_star,
                            np.subtract(
                                np.subtract(s2, s1),
                                God.L)),
                        2))))
        res_v = np.add(v1, np.multiply(func_result, God.TIME))
        list(map(union, zip(cars[1:], res_x, res_v)))

    def update(self) -> ():
        cars = reduce(add_inf, map(lambda obj: obj.cars, filter(lambda obj: obj.type == "road", self.map)), [])
        self.move(cars)
        for obj in self.map:
            obj.update()
