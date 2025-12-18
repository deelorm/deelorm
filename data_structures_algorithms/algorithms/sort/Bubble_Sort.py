# Task -- Create Bubble Sort function

def bubble_sort(sort_list):
    for i in range(len(sort_list) - 1):
        for k in range(len(sort_list) - i - 1):
            if sort_list[k+1] < sort_list[k]:
                sort_list[k], sort_list[k+1] = sort_list[k+1], sort_list[k]
    return sort_list


## Sample test input

sort_list = [2,1,4,3,6,5]
print(bubble_sort(sort_list))


