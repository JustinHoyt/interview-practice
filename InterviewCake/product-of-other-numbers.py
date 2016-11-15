'''
Created on Oct 29, 2016

@author: justinhoyt
'''

def get_products_of_all_ints_except_at_index(int_list):
    products_of_all_ints_before_index = []
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_before_index.append(product_so_far)
        product_so_far *= int_list[i]
    print(products_of_all_ints_before_index)
    
    product_so_far = 1
    products_of_all_ints_after_index = []
    for i in reversed(range(len(int_list))):
        products_of_all_ints_after_index.append(product_so_far)
        product_so_far += int_list[i]
    print(products_of_all_ints_after_index)

test = [3, 1, 2, 5, 6, 4]
test2 = [1, 7, 3, 4]

get_products_of_all_ints_except_at_index(test)
print()
get_products_of_all_ints_except_at_index(test2)