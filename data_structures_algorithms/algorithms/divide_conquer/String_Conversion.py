
def string_conversion(str1, str2, index1, index2):

    if index1 == len(str1):
        return len(str2) - index2
    if index2 == len(str2):
        return len(str1) - index1
    if str1[index1] == str2[index2]:
        return string_conversion(str1, str2, index1+1, index2+1)

    delete_op = 1 + string_conversion(str1, str2, index1, index2+1)
    insert_op = 1 + string_conversion(str1, str2, index1+1, index2)
    sub_op = 1 + string_conversion(str1, str2, index1+1, index2+1)

    return min(delete_op, insert_op, sub_op)

str1 = 'struct'
str2 = 'stuct'
print(string_conversion(str1, str2, 0, 0))

