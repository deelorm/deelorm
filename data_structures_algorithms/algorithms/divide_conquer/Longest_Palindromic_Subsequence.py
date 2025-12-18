

def longest_palindromic_subsequence(str1, left_index, right_index):
    if left_index > right_index:
        return 0
    if left_index is right_index:
        return 1
    if str1[left_index] is str1[right_index]:
        return 2 + longest_palindromic_subsequence(str1, left_index+1, right_index-1)
    op1 = longest_palindromic_subsequence(str1, left_index, right_index-1)
    op2 = longest_palindromic_subsequence(str1, left_index+1, right_index)
    return max(op1, op2)

str1 = 'elrmenmet'
print(longest_palindromic_subsequence(str1, 0, 8))




