# Task -- Create Heap Sort function using binary heap

def heapify_sort(sort_list, num_nodes, index):      # Maintains heapify property of binary heap
    parent_index = index

    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < num_nodes and sort_list[left_index] < sort_list[parent_index]:
        parent_index = left_index 

    if right_index < num_nodes and sort_list[right_index] < sort_list[parent_index]:
        parent_index = right_index 

    if parent_index is not index:
        sort_list[parent_index], sort_list[index] = sort_list[index], sort_list[parent_index]
        heapify_sort(sort_list, num_nodes, parent_index)

def heap_sort(sort_list):       # Heap sort function
    num_nodes = len(sort_list)

    for i in range(int(num_nodes / 2) - 1, -1, -1):
        heapify_sort(sort_list, num_nodes, i)

    for i in range(num_nodes - 1, 0, -1):
        sort_list[i], sort_list[0] = sort_list[0], sort_list[i]
        heapify_sort(sort_list, i, 0)
    return sort_list


## Sample test inputs

# sort_list = [2,1,4,3,6,5]
# print(sort_list)

# print('------------------')

# print(heap_sort(sort_list))













