'''
https://www.hackerrank.com/challenges/python-lists
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of
commands where each command will be of the types listed above. Iterate
through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''

list = []
num_commands = int(input())

while num_commands > 0:
    command = input()
    command = command.split(' ')
    if 'insert' in command:
        index = int(command[-2])
        num = int(command[-1])
        list.insert(index, num)
    elif 'print' in command:
        print(list)
    elif 'remove' in command:
        list.remove(int(command[-1]))
    elif 'append' in command:
        list.append(int(command[-1]))
    elif 'sort' in command:
        list.sort()
    elif 'pop' in command:
        list.pop()
    elif 'reverse' in command:
        list.reverse()
    num_commands -= 1