# Task -- Create Bucket Sort function with given range of postive numbers only


# Imported modules
import math 
import Insertion_Sort as isort

def bucket_sort(sort_list):
    num_buckets = round(math.sqrt(len(sort_list)))
    max_data = max(sort_list)
    bucket_list = []
    
    for i in range(num_buckets):
        bucket_list.append([])

    for i in range(len(sort_list)):
        bucket_num = math.ceil(sort_list[i] * num_buckets / max_data)
        bucket_list[bucket_num - 1].append(sort_list[i])

    sort_list = []
    for i in bucket_list:
        sort_list.extend(isort.insertion_sort(i))

    return sort_list 


## Sample test inputs

sort_list = [2,1,4,3,6,5]
print(sort_list)
print('------------------')
print(bucket_sort(sort_list))






