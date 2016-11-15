'''
Created on Nov 9, 2016

@author: justinhoyt

Suppose we had a list of n integers in sorted order. 
How quickly could we check if a given integer is in the list?
'''

def is_in_list(list, target_number):
    #check the middle number
    if len(list) == 1:
        return list[0] == target_number
    if len(list) == 2:
        return list[0] == target_number or list[1] == target_number
    middle_index = len(list) // 2
    if list[middle_index] == target_number:
        return True
    elif target_number < list[middle_index]:
        return is_in_list(list[:middle_index], target_number)
    else:
        return is_in_list(list[middle_index + 1:], target_number)
        
        
list = [1,2,4,5,7,8,12,34,54,100]
target_number1 = 34
target_number2 = 33

print(is_in_list(list, target_number1))
print(is_in_list(list, target_number2))