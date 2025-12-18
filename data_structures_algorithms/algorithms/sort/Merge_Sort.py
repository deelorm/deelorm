

def merge(sort_list, left_index, middle_index, right_index):
    first_range = middle_index - left_index + 1
    second_range = right_index - middle_index
    merge_list1 = [0] * first_range 
    merge_list2 = [0] * second_range 

    for i in range(first_range):
        merge_list1[i] = sort_list[i + left_index]

    for i in range(second_range):
        merge_list2[i] = sort_list[i + middle_index + 1]

    i = 0
    k = 0
    l = left_index

    while i < first_range and k < second_range:
        if merge_list1[i] <= merge_list2[k]:
            sort_list[l] = merge_list1[i]
            i += 1
            l += 1
        else:
            sort_list[l] = merge_list2[k]
            k += 1
            l += 1

    while i < first_range:
        sort_list[l] = merge_list1[i]
        i += 1
        l += 1

    while k < second_range:
        sort_list[l] = merge_list2[k]
        k += 1
        l += 1
 

def merge_sort(sort_list, left_index, right_index):
    if left_index < right_index:
        middle_index = (left_index + (right_index - 1)) // 2
        merge_sort(sort_list, left_index, middle_index)
        merge_sort(sort_list, middle_index + 1, right_index)
        merge(sort_list, left_index, middle_index, right_index)
    return sort_list


sort_list = [2,1,4,3,6,5]
print(sort_list)

print('----------------------')

print(merge_sort(sort_list, 0, 5))

