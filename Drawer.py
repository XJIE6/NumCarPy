import Object
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Drawer:
    def __init__ (self, map: [Object], point, k, screen):
        self.map = map
        self.point = point
        self.k = k
        self.screen = screen

    def draw_car(self, point) -> ():
        print(point)
        pygame.draw.rect(self.screen, BLACK, [point[0], point[1], 20, 20], 0)


    def draw(self) -> ():
        self.screen.fill(WHITE)
        for obj in self.map:
            if obj.type == "road":
                for car in obj.cars:
                     x = ((obj.point2[0] - obj.point1[0]) * car.x / obj.len + obj.point1[0]) * self.k + self.point[0]
                     y = ((obj.point2[1] - obj.point1[1]) * car.x / obj.len + obj.point1[1]) * self.k + self.point[1]
                     self.draw_car((x, y))
