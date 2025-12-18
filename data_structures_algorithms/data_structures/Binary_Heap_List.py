# Task -- Create Binary Heap data structure using Python list  with peek heap, size_heap, level_order_traversal, heapify_insert
# Cont'd -- insert_node, heapify_extract, extract_node, and delete_heap functions

class Binary_Heap:
    '''
Binary heap structure implementation
    '''
    def __init__(self, size):       # Initializes binary heap class with size as parameter
        self.heap_list = [None] * (size+1)
        self.heap_size = 0
        self.maxsize = size+1 

    def peek_heap(self, root_node):     # Return data of root node in the binary heap, otherwise None
        if not root_node:
            return 
        return root_node.heap_list[1]

    def size_heap(self, root_node):     # Returns size of the binary heap 
        if not root_node:
            return 
        return root_node.heap_size 

    def level_order_traversal(self, root_node):     # Traverses nodes in the binary heap structure level- wise i.e levels 0, 1, 2, etc. with root node passed as parameter
        if not root_node:
            return 
        for i in range(1, root_node.heap_size+1):
            print(root_node.heap_list[i], end=' ')
        print('')

    def heapify_insert(self, root_node, index, heap_type):  # Maintains min or max heap property of binary heap after insert_node operation with root node, index, and heap type (min or max) passed as parameters
        parent_index = int(index/2) 
        if index <= 1:
            return 
        else:
            if heap_type == 'min':
                if root_node.heap_list[index] < root_node.heap_list[parent_index]:
                    temp = root_node.heap_list[index]
                    root_node.heap_list[index] = root_node.heap_list[parent_index]
                    root_node.heap_list[parent_index] = temp 
                self.heapify_insert(root_node, parent_index, heap_type)
            elif heap_type == 'max':
                if root_node.heap_list[index] > root_node.heap_list[parent_index]:
                    temp = root_node.heap_list[index]
                    root_node.heap_list[index] = root_node.heap_list[parent_index]
                    root_node.heap_list[parent_index] = temp 
                self.heapify_insert(root_node, parent_index, heap_type)

    def insert_node(self, root_node, node_data, heap_type):     # Adds new node to the binary heap with root node, node data and heap type (min or max) passed as parameters
        if not root_node:
            return
        if root_node.heap_size + 1 == root_node.maxsize:
            print('Binary heap is full')
            return
        root_node.heap_list[root_node.heap_size+1] = node_data 
        root_node.heap_size += 1 
        self.heapify_insert(root_node, root_node.heap_size, heap_type)
        print('Node inserted..', node_data)

    def heapify_extract(self, root_node, index, heap_type):     # Maintains min or max heap property of binary heap after extract_node operation with root node, index, and heap type (min or max) passed as parameters
        right_index = 2*index+1
        left_index = 2*index 
        swap_child = 0

        if root_node.heap_size < left_index or left_index == 0 or right_index == 0:
            return 
        if root_node.heap_size == left_index:
            if heap_type == 'min':
                if root_node.heap_list[index] > root_node.heap_list[left_index]:
                    temp = root_node.heap_list[index] 
                    root_node.heap_list[index] = root_node.heap_list[left_index]
                    root_node.heap_list[left_index] = temp 
                    return
            elif heap_type == 'max':
                if root_node.heap_list[index] < root_node.heap_list[left_index]:
                    temp = root_node.heap_list[index]
                    root_node.heap_list[index] = root_node.heap_list[left_index]
                    root_node.heap_list[left_index] = temp 
                    return
        else:
            if heap_type == 'min':
                if root_node.heap_list[left_index] < root_node.heap_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if root_node.heap_list[index] > root_node.heap_list[swap_child]:
                    temp = root_node.heap_list[swap_child]
                    root_node.heap_list[swap_child] = root_node.heap_list[index]
                    root_node.heap_list[index] = temp 
            elif heap_type == 'max':
                if root_node.heap_list[left_index] > root_node.heap_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if root_node.heap_list[index] < root_node.heap_list[swap_child]:
                    temp = root_node.heap_list[index] 
                    root_node.heap_list[index] = root_node.heap_list[swap_child]
                    root_node.heap_list[swap_child] = temp 
        self.heapify_extract(root_node, swap_child, heap_type)

    def extract_node(self, root_node, heap_type):   # Extracts node in the binary heap with given root node and heap type (min or max) as parameters 
        if root_node.heap_size == 0:
            print('Binary heap is empty')
            return 
        extracted_node = root_node.heap_list[1]
        root_node.heap_list[1] = root_node.heap_list[root_node.heap_size]
        root_node.heap_list[root_node.heap_size] = None
        root_node.heap_size-=1
        self.heapify_extract(root_node, 1, heap_type)
        return extracted_node 

    def delete_heap(self, root_node):       # Deletes entire binary heap
        root_node.heap_list = None
        root_node = None
        return root_node



## Sample test inputs

bheap = Binary_Heap(5)

# print(bheap.peek_heap(bheap))
# print(bheap.heap_list)

# bheap.insert_node(bheap, 20, 'min')
# bheap.insert_node(bheap, 30, 'min')
# bheap.insert_node(bheap, 10, 'min')
# bheap.insert_node(bheap, 40, 'min')
# bheap.insert_node(bheap, 50, 'min')

# bheap.level_order_traversal(bheap)
# print('----------------------')
# print(bheap.extract_node(bheap, 'min'))
# bheap.level_order_traversal(bheap)


bheap.insert_node(bheap, 20, 'max')
bheap.insert_node(bheap, 30, 'max')
bheap.insert_node(bheap, 10, 'max')
bheap.insert_node(bheap, 40, 'max')
bheap.insert_node(bheap, 50, 'max')

bheap.level_order_traversal(bheap)

#bheap.level_order_traversal(bheap)
print('----------------------')
# print(bheap.extract_node(bheap, 'max'))
# bheap.level_order_traversal(bheap)

bheap = bheap.delete_heap(bheap)
print(bheap)