"""
Created on Nov 1, 2016
denominations = [1, 2, 3]
amount = 4
@author: justinhoyt
4¢ with those denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢
"""


def make_change(amount, denominations):
    memo = [(amount+1) * [0] for x in range(len(denominations))]
    for row in range(len(memo)):
        for col in range(len(memo[0])):
            if row != 0:
                memo[row][col] = memo[row-1][col]
            if col == denominations[row]:
                memo[row][col] += 1
            if col - denominations[row] > 0:
                memo[row][col] += memo[row][col-denominations[row]]
    return memo[len(memo)-1][len(memo[0])-1]


# amount = 4
# denominations = [1,2,3]
amount = 6
denominations = [2,3,4]
print(make_change(amount, denominations))
