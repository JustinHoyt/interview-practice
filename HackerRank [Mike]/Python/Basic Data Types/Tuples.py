'''
https://www.hackerrank.com/challenges/python-tuples
Task
Given an integer, n, and n space-separated integers as input,
create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output Format
Print the result of hash(t).

Sample Input
2
1 2

Sample Output
3713081631934410656
'''

n = int(input())
line = input().split(' ')
input_list = map(int, line)
t = tuple(input_list)
print(hash(t))