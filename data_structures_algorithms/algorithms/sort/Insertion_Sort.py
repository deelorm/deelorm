# Task -- Create Insertion Sort function

def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        index_data = sort_list[i]
        k = i - 1
        while k >= 0 and index_data < sort_list[k]:
            sort_list[k+1] = sort_list[k]
            k -= 1
        sort_list[k + 1] = index_data 
    return sort_list 


## Sample test inputs

# sort_list = [2,1,4,3,6,5]

# print(sort_list)
# print('-----------------------')
# print(insertion_sort(sort_list))




