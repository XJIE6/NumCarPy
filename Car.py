import Object
class Car:


    def __init__(self, max_v: int, x: int, v: int, path: [Object], color = (0, 0, 0)) -> ():
        self.color = color
        self.max_v = max_v
        self.x = x
        self.v = v
        self.path = path

    def start(self):
        self.path.pop(0).add(None, self)

    def update(self, x: int, v: int):
        self.x = x
        self.v = v