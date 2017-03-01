import Object
import Car
import types

def dead_add(self, obj, car: Car) -> ():
    self.count += 1
    return


class Map:
    DEAD = Object.Object(2, -1)
    DEAD.count = 0
    DEAD.add = types.MethodType(dead_add, DEAD)
    DEAD.type = 2

    @staticmethod
    def get_map() -> [Object]:
        left_a = Object.Object(1, 0, None, 1000, (2, 4), (2, 14))
        left_c = Object.Object(1, 1, None, 1000, (3, 14), (3, 4))
        right_a = Object.Object(1, 2, None, 1000, (15, 14), (15, 4))
        right_c = Object.Object(1, 3, None, 1000, (14, 4), (14, 14))
        top_a = Object.Object(1, 4, None, 1000, (14, 2), (4, 2))
        top_c = Object.Object(1, 5, None, 1000, (4, 3), (14, 3))
        bot_a = Object.Object(1, 6, None, 1000, (4, 15), (14, 15))
        bot_c = Object.Object(1, 7, None, 1000, (14, 14), (4, 14))

        left_top_s = Object.Object(1, 12, None, 200, (2, 0), (2, 2))
        left_bot_s = Object.Object(1, 13, None, 200, (0, 15), (2, 15))
        right_top_s = Object.Object(1, 14, None, 200, (18, 2), (16, 2))
        right_bot_s = Object.Object(1, 15, None, 200, (15, 18), (15, 16))

        left_top = Object.Object(0, 8, inRoads=[left_c, top_a, left_top_s, None], outRoads=[left_a, top_c, None, None], point1 = (2, 2))
        left_bot = Object.Object(0, 9, inRoads=[None, bot_c, left_a, left_bot_s], outRoads=[None, bot_a, left_c, None], point1 = (2, 14))
        right_top = Object.Object(0, 10, inRoads=[right_a,right_top_s, None, top_c], outRoads=[right_c, None, None, top_a], point1 = (14, 2))
        right_bot = Object.Object(0, 11, inRoads=[right_bot_s, None, right_c, bot_a], outRoads=[None, None, right_a, bot_c], point1 = (14, 14))
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


    @staticmethod
    def get_test_map(k, l) -> [Object]:

        res = []

        first = Object.Object(1, 0, None, l)
        second = Object.Object(1, 1, None, l)
        res.append(first)
        res.append(second)

        for i in range(k):

            left = Object.Object(1, 7 * i + 3, None, l)
            top = Object.Object(1, 7 * i + 5, None, l)
            bot = Object.Object(1, 7 * i + 6, None, l)
            right = Object.Object(1, 7 * i + 8, None, l)

            start = Object.Object(0, 7 * i + 2, inRoads=[first, second, None, None], outRoads=[None, None, bot, left])
            up = Object.Object(0, 7 * i + 4, inRoads=[left, None, None, None], outRoads=[None, top, None, None])
            down = Object.Object(0, 7 * i + 7, inRoads=[bot, None, None, None], outRoads=[None, None, None, right])

            left.next = up
            bot.next = down
            first.next = start
            second.next = start

            first = top
            second = right

            res.append(start)
            res.append(left)
            res.append(up)
            res.append(top)
            res.append(bot)
            res.append(down)
            res.append(right)

        first.next = Map.DEAD
        second.next = Map.DEAD

        return res