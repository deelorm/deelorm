

def LCS(str1, str2, index1, index2):
    if index1 == len(str1) or index2 == len(str2):
        return 0
    if str1[index1] is str2[index2]:
        return 1 + LCS(str1, str2, index1+1, index2+1) 
    op1 = LCS(str1, str2, index1, index2+1)
    op2 = LCS(str1, str2, index1+1, index2)
    return max(op1, op2)

str1 = 'ellepatt'
str2 = 'errepat'
print(LCS(str1, str2, 0, 0))





