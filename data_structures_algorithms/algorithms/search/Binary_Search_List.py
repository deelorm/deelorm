# Task -- Create Binary Search function

# Imported modules

import math 
import Heap_Sort as hs 

def binary_search(sort_list, data):
    sort_list = hs.heap_sort(sort_list)
    sort_list.reverse()
    left_index = 0
    right_index = len(sort_list) - 1
    middle_index = math.floor((left_index + right_index) / 2)
    
    while left_index <= right_index:
        print(middle_index)
        if sort_list[middle_index] == data:
            return middle_index

        if sort_list[middle_index] < data:
            left_index = middle_index + 1
        elif sort_list[middle_index] > data:
            right_index = middle_index - 1

        middle_index = math.floor((left_index + right_index) / 2)
    return False


## Sample test inputs

sort_list = [2,1,4,3,6,5]
print(sort_list)

print('---------------------')

print(binary_search(sort_list, 2))

