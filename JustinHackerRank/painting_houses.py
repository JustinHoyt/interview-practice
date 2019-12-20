import math


def paint(houses, memo, house, curr_house_color):
    key = (house, curr_house_color)
    if key in memo:
        return memo[key]

    if house == len(houses)-1:
        return houses[house][curr_house_color]

    lowest_cost = math.inf
    for next_house_color in range(3):
        if curr_house_color != next_house_color:
            possible_cost = paint(houses, memo, house+1, next_house_color)
                            + houses[house][curr_house_color]
            lowest_cost = min(possible_cost, lowest_cost)

    memo[key] = lowest_cost
    return lowest_cost


def paint_houses(houses):
    memo = {}
    house = 0
    result = math.inf
    for curr_house_color in range(3):
        result = min(paint(houses, memo, house, curr_house_color), result)
    return result


print(paint_houses([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
