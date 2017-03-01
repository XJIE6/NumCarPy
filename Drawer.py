import Object
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
class Drawer:
    def __init__ (self, map: [Object], point, k, screen):
        self.map = map
        self.point = point
        self.k = k
        self.screen = screen

    def ok(self, point):
        return point[0] > -50 and point[0] < 600 and point[1] > -50 and point[1] < 600

    def draw_car(self, color, point) -> ():
        print(point)
        pygame.draw.rect(self.screen, color, [point[0], point[1], 20, 20], 0)


    def draw(self) -> ():
        self.screen.fill(WHITE)
        for obj in self.map:
            if obj.type == 1:
                for car in obj.cars:
                     print (car.x)
                     print (obj.id)
                     x = ((obj.point2[0] - obj.point1[0]) * car.x / obj.len + obj.point1[0]) * self.k + self.point[0]
                     y = ((obj.point2[1] - obj.point1[1]) * car.x / obj.len + obj.point1[1]) * self.k + self.point[1]
                     self.draw_car(car.color, (x, y))
            elif obj.type == 0:
                color = GRAY
                if obj.lock[0][0] != None:
                    color = obj.lock[0][0][0].color
                pygame.draw.rect(self.screen, color, [(obj.point1[0] + 1) * self.k, (obj.point1[1] + 1) * self.k, self.k, self.k], 0)

                color = GRAY
                if obj.lock[0][1] != None:
                    color = obj.lock[0][1][0].color
                pygame.draw.rect(self.screen, color, [(obj.point1[0] + 1) * self.k, obj.point1[1] * self.k, self.k, self.k], 0)

                color = GRAY
                if obj.lock[0][2] != None:
                    color = obj.lock[0][2][0].color
                pygame.draw.rect(self.screen, color,[(obj.point1[0]) * self.k, (obj.point1[1]) * self.k, self.k, self.k], 0)

                color = GRAY
                if obj.lock[0][3] != None:
                    color = obj.lock[0][3][0].color
                pygame.draw.rect(self.screen, color, [obj.point1[0] * self.k, (obj.point1[1] + 1) * self.k, self.k, self.k], 0)
