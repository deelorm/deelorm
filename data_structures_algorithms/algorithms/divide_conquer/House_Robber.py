
def house_robber(houses, house_num):
    if house_num > len(houses) - 1:
        return 0
    op1 = houses[house_num] + house_robber(houses, house_num + 2)
    skip_op = house_robber(houses, house_num + 1)
    return max(op1, skip_op)


houses = [1,3,6,5,8]
print(house_robber(houses, 0))
