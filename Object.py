import Car
import Map
class Object:

    def __init__(self, type: str, id: int, next = None, len: int = 0, point1 = (0, 0), point2 = (0, 0), inRoads = None, outRoads = None) -> ():
        self.cars = []
        self.id = id
        self.type = type
        self.k = 1

        if type == "road":
            self.next = next
            self.len = len
            self.point1 = point1
            self.point2 = point2

        elif type == "crossroad":
            self.inRoads = {inRoads[0]: 0, inRoads[1]: 1, inRoads[2]: 2, inRoads[3]: 3}
            self.outRoads = {outRoads[0]: 0, outRoads[1]: 1,outRoads[2]: 2, outRoads[3]: 3}
            self.cars = [[], [], [], []]
            self.lock = [[0 for x in range(4)] for y in range(3)]
            self.onRoad = [[], [], []]

    # def __init__(self, id: int, left: Object, right: Object, top: Object, bottom: Object, len: int = None) -> ():
    #     self.cars = []
    #     self.id = id
    #     self.left   = left
    #     self.right  = right
    #     self.top    = top
    #     self.bottom = bottom
    #     if  left   is None and \
    #         right  is None and \
    #         top    is None and \
    #         bottom is None:
    #
    #         if len == None:
    #             raise "len_is_nessasery_for_street_object"
    #
    #         self.type = "vertical_road"
    #         self.len = len
    #
    #     elif top    is None and \
    #          bottom is None and \
    #          right  is None and \
    #          left   is None:
    #
    #         if len == None:
    #             raise "len_is_nessasery_for_street_object"
    #
    #         self.type = "horizontal_road"
    #         self.len = len
    #
    #     else :
    #         self.type = "crossroad"

    def update(self) -> ():
        if len(self.cars) == 0:
            return
        if self.type == "road":
            if (self.cars[0].x > self.len):
                self.cars[0].x = 0
                self.next.add(self, self.cars.pop(0))
        elif self.type == "crossroad":
            self.k += 1
            if (self.k == 20):
                self.upd()
                self.crossroad()
                self.k = 0
            # while len(self.cars) > 0:
            #     if len(self.cars[0].path) == 0:
            #         Map.Map.DEAD.add(self.cars.pop(0))
            #     else:
            #         car = self.cars[0]
            #         car.path[0].add(self.cars.pop(0))
            #         car.path.pop(0)


    def add(self, road, car: Car) -> ():
        if self.type == "road":
            self.cars.append(car)
        elif self.type == "crossroad":
            rd = self.inRoads[road]
            self.cars[rd].append(car)

    def prior(self, start, finish):
        res = (start - finish + 4) % 4
        if res == 1:
            return 1
        elif res == 2:
            return 0
        else:
            return 2


    def crossroad(self):
        cur = []
        for i in range(len(self.cars)):
            while len(self.cars[i]) > 0 and len(self.cars[i][0].path) == 0:
                Map.Map.DEAD.add(self.cars[i].pop(0))
            if len(self.cars[i]) != 0:
                car = self.cars[i][0]
                cur.append((car, i, self.outRoads[car.path[0]]))
        if len(cur) == 0:
            return
        cars = sorted(cur, key=lambda car: self.prior(car[1], car[2]))
        for car in cars:
            i = 0
            f = True
            while ((car[1] + i) % 4 != car[2]):
                if self.lock[i][(car[1] + i) % 4] != 0:
                    f = False
                i += 1
            if f == True:
                i = 0
                while ((car[1] + i) % 4 != car[2]):
                    self.lock[i][(car[1] + i) % 4] = 1
                    i += 1
                self.cars[car[1]].pop(0)
                self.onRoad[self.prior(car[1], car[2])].append(car[0])

    def upd(self):
        for car in self.onRoad[0]:
            if len(car.path) == 0:
                Map.Map.DEAD.add(car)
            else:
                car.path[0].add(self, car)
                car.path.pop(0)
        self.onRoad[0] = self.onRoad[1]
        self.onRoad[1] = self.onRoad[2]
        self.onRoad[2] = []

        self.lock[0] = self.lock[1]
        self.lock[1] = self.lock[2]
        self.lock[2] = [0, 0, 0, 0]