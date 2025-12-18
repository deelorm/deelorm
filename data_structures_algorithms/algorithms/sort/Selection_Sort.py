# Task -- Create Selection Sort function

def selection_sort(sort_list):
    for i in range(len(sort_list)):
        index = i
        for k in range(i+1, len(sort_list)):
            if sort_list[k] < sort_list[index]:
                index = k
        sort_list[index], sort_list[i] = sort_list[i], sort_list[index]
    return sort_list 


## Sample test inputs

sort_list = [2,1,4,3,6,5]
print(sort_list)
print('-------------------')
print(selection_sort(sort_list))




