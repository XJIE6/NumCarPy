import Car
class Object:

    def __init__(self, id: int, next, len: int = 0) -> ():
        self.cars = []
        self.id = id
        self.next = next
        self.len = len
        self.type = "road"
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
                self.next.add(self.cars.pop(0))

    def add(self, car: Car) -> ():
        self.cars.append(car)