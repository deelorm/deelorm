import itertools as tools

# def num_factor(a=5, b=[1,3,4]):
#     num_comb = []
#     for i in range(1,a+1):
#         temp = tools.product(b, repeat=i)
#         for k in temp:
#             num_comb.append(k)
#     num_comb_factor = []

#     for i in num_comb:
#         if sum(i) == a:
#             num_comb_factor.append(i)
#     print(len(num_comb_factor))



def num_factor(num):
    if num == 0:
        return 0
    if num in [1,2]:
        return 1
    if num == 3:
        return 2
    op1 = num_factor(num - 1)
    op2 = num_factor(num - 3)
    op3 = num_factor(num - 4)
    return op1 + op2 + op3

a = 5
num = [1,3,4]

# num_factor()
print(num_factor(a))




# 1 3 4; 6 -- f(0)-0 f(1)-0, f(2)-1, f(3)-2, f(4) 
# f(6)
# f(5)+1 - f(5+1) 
# f(3)+3 - [3,3] [1,1,1,3]
# f(2)+4 - [1 1 4]

# f(5)      f(6)
# f(1) + 4  [1,4] + 1
# f(2) + 3 - [1,1,3] + 1
# f(4) + 1 - [1,4] + 1

# f(4)         f(5)         f(6)
# f(1) + 3 - [1,3] + 1  -   [1,3] + 1 + 1   
# f(3) + 1 - [3,1] + 1  -   [3,1] + 1 + 1 

# f(3)
# f(2) + 1 - [2,1] [1,1,1]

# f(2)
# f(1) + 1

# f(1)
# f(0) + 1 

# 1 3 4: 5
# f(5) - f(1)-0 f(2)-1 f(3)-2
# f(4) + 1 - [1,4]
# f(2) + 3 - [1 1 3]
# f(1) + 4 - [1,4]

# f(4)              f(5)
# f(3) + 1 - [3 1] + 1
# f(1) + 3 - [1 3] + 1

# f(3)              f(4)     f(5)
# f(2) + 1 - [1 1] + 1   [2 1] + 1 + 1




