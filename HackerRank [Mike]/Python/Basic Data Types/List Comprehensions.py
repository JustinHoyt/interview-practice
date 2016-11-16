'''
https://www.hackerrank.com/challenges/list-comprehensions

Let's learn about list comprehensions! You are given three integers X, Y and Z
representing the dimensions of a cuboid along with an integer N. You have to
print a list of all possible coordinates given by (i,j,k) on a 3D grid where the
sum of i+j+k is not equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z

Input Format
Four integers X, Y, Z and N each on four separate lines, respectively.

Constraints
Print the list in lexicographic increasing order.

Sample Input
1
1
1
2

Sample Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

'''
# X = int(input())
# Y = int(input())
# Z = int(input())
# N = int(input())
list = []
X = 1
Y = 1
Z = 1
N = 2

[list.append([x,y,z]) for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != N]
print(list)