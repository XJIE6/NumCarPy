import Object
import Car
import types

def dead_add(self, car: Car) -> ():
    self.count += 1
    return


class Map:
    DEAD = Object.Object("dead", -1)
    DEAD.count = 0
    DEAD.add = types.MethodType(dead_add, DEAD)
    DEAD.type = "dead"
    @staticmethod
    def get_map() -> [Object]:
        left_a = Object.Object("road", 0, None, 1000, (0, 0), (0, 10))
        left_c = Object.Object("road", 1, None, 1000, (1, 9), (1, 1))
        right_a = Object.Object("road", 2, None, 1000, (10, 10), (10, 0))
        right_c = Object.Object("road", 3, None, 1000, (9, 1), (9, 9))
        top_a = Object.Object("road", 4, None, 1000, (10, 0), (0, 0))
        top_c = Object.Object("road", 5, None, 1000, (1, 1), (9, 1))
        bot_a = Object.Object("road", 6, None, 1000, (0, 10), (10, 10))
        bot_c = Object.Object("road", 7, None, 1000, (9, 9), (1, 9))

        left_top_s = Object.Object("road", 12, None, 1000, (0, -2), (0, 0))
        left_bot_s = Object.Object("road", 13, None, 1000, (-2, 10), (0, 10))
        right_top_s = Object.Object("road", 14, None, 1000, (12, 0), (10, 0))
        right_bot_s = Object.Object("road", 15, None, 1000, (10, 12), (10, 10))

        left_top = Object.Object("crossroad", 8, inRoads=[left_c, top_a, left_top_s, None], outRoads=[left_a, top_c, None, None])
        left_bot = Object.Object("crossroad", 9, inRoads=[bot_c, left_a, left_bot_s, None], outRoads=[bot_a, left_c, None, None])
        right_top = Object.Object("crossroad", 10, inRoads=[top_c, right_a,right_top_s, None], outRoads=[top_a, right_c, None, None])
        right_bot = Object.Object("crossroad", 11, inRoads=[right_c, bot_a, right_bot_s, None], outRoads=[right_a, bot_c, None, None])
        left_a.next = left_bot
        left_c.next = left_top
        right_a.next = right_top
        right_c.next = right_bot
        bot_a.next = right_bot
        bot_c.next = left_bot
        top_a.next = left_top
        top_c.next = right_top

        left_top_s.next = left_top
        left_bot_s.next = left_bot
        right_top_s.next = right_top
        right_bot_s.next = right_bot

        return [left_a, left_c, right_a, right_c, top_a, top_c, bot_a, bot_c, left_top, left_bot, right_top, right_bot, left_top_s, left_bot_s, right_top_s, right_bot_s]
