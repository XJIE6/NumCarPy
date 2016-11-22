class Car:

    def __init__(self, max_v: int, x: int = None, v: int = None) -> ():
        self.max_v = max_v
        self.x = x
        self.v = v

    def update(self, x: int, v: int):
        self.x = x
        self.v = v