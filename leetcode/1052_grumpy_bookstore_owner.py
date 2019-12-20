from typing import List


def max_satisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    satisfied_without_ungrumpy = 0
    satisfied_window_with_technique = 0
    best_satisfied_window_with_technique = 0
    i = 0
    for num_customers, is_grumpy in zip(customers, grumpy):
        if is_grumpy == 0:
            satisfied_without_ungrumpy += num_customers
        else:
            satisfied_window += num_customers
            # X = 3, i = 3
            if i >= X:
                pass

        i += 1



customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]

X = 3


print(max_satisfied(customers, grumpy, X))
