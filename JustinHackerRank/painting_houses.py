import math


def paint(houses, memo, house, paint_color):
    key = str(house) + ", " + str(paint_color)
    if key in memo:
        return memo[key]

    if house == len(houses)-1:
        return houses[house][paint_color]

    lowest_cost = math.inf
    for i in range(3):
        if paint_color != i:
            possible_cost = paint(houses, memo, house+1, i)
            possible_cost += houses[house][paint_color]
            lowest_cost = min(possible_cost, lowest_cost)

    memo[key] = lowest_cost
    return lowest_cost


def paint_houses(houses):
    memo = {}
    house = 0
    result = math.inf
    # result = paint(houses, memo, house, -1)
    for paint_color in range(3):
        result = min(paint(houses, memo, house, paint_color), result)
    return result


print(paint_houses([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
