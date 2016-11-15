'''
Created on Oct 29, 2016

@author: justinhoyt
'''
def highest_product(list_of_ints):
    highest_product = 0
    highest = 0 
    second_highest = 0
    third_highest = 0
    lowest = float("INF")
    second_lowest = float("INF")
    for element in list_of_ints:
        if element > highest:
            third_highest = second_highest
            second_highest = highest
            highest = element
        elif element > second_highest:
            third_highest = second_highest
            second_highest = element
        elif element > third_highest:
             third_highest = element
        if element < lowest:
            second_lowest = lowest
            lowest = element 
        elif element < second_lowest:
            second_lowest = element

    highest_product = max(highest * second_highest * third_highest, 
                          lowest * second_lowest * highest)
    return highest_product

list = [4, 5, 2, 3, -6, -7, 10, 1]

print(highest_product(list))
