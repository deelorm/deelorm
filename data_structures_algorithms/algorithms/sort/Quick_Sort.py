# Task -- Create Quick Sort function

def swap(sort_list, index1, index2):    # Swap elements of given indexes
    sort_list[index1], sort_list[index2] = sort_list[index2], sort_list[index1]

def pivot(sort_list, pivot_index, last_index):      # Returns the swap index 
    swap_index = pivot_index 
    for i in range(pivot_index + 1, last_index + 1):
        if sort_list[i] < sort_list[pivot_index]:
            swap_index += 1
            swap(sort_list, swap_index, i)
    swap(sort_list, pivot_index, swap_index)
    return swap_index

def quick_sort_pivot(sort_list, left_index, right_index):       # Sorts list by calling pivot function and recursively calling itself
    if left_index < right_index:
        swap_index = pivot(sort_list, left_index, right_index)
        quick_sort_pivot(sort_list, left_index, swap_index - 1)
        quick_sort_pivot(sort_list, swap_index + 1, right_index)


## Sample test inputs

def quick_sort(sort_list):      #   Initializes input and calls quick_sort_pivot function
    quick_sort_pivot(sort_list, 0, len(sort_list) - 1)

sort_list = [2,1,4,3,6,5]
print(sort_list)

print('-----------------------')

quick_sort(sort_list)
print(sort_list)

