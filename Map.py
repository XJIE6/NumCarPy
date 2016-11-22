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
        left_o = Object.Object("road", 0, None, 1000)
        left_i = Object.Object("road", 1, None, 1000)
        right_o = Object.Object("road", 2, None, 1000)
        right_i = Object.Object("road", 3, None, 1000)
        top_o = Object.Object("road", 4, None, 1000)
        top_i = Object.Object("road", 5, None, 1000)
        bot_o = Object.Object("road", 6, None, 1000)
        bot_i = Object.Object("road", 7, None, 1000)
        left_top = Object.Object("crossroad", 8, roads=[left_o, left_i, top_o, top_i])
        left_bot = Object.Object("crossroad", 9, roads=[left_o, left_i, bot_o, bot_i])
        right_top = Object.Object("crossroad", 10, roads=[right_o, right_i, top_o, top_i])
        right_bot = Object.Object("crossroad", 11, roads=[right_o, right_i, bot_o, bot_i])
        left_o.next = left_bot
        left_i.next = left_top
        right_o.next = right_top
        right_i.next = right_bot
        bot_o.next = right_bot
        bot_i.next = left_bot
        top_o.next = left_top
        top_i.next = right_top

        return [left_o, left_i, right_o, right_i, top_o, top_i, bot_o, bot_i, left_top, left_bot, right_top, right_bot]
