def paint(houses, memo, house, paint_color):
    key = str(house) + "-" + str(paint_color)
    if key in memo:
        return memo[key]

    if house == len(houses)-1:
        return houses[house][paint_color]

    lowest_cost = float('inf')
    for i in range(3):
        if paint_color != i:
            possible_cost = paint(houses, memo, houses+1, i)
            possible_cost += houses[house][i]
            lowest_cost = min(possible_cost, lowest_cost)

    memo[key] = lowest_cost
    return lowest_cost


def paint_houses(houses):
    memo = {}
    house = 0
    paint_color = -1
    paint(houses, memo, house, paint_color)


print(paint_houses([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
