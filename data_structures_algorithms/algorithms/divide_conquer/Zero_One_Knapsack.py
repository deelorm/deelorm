
class Product:
    def __init__(self, weight, value):
        self.weight= weight 
        self.value = value 

def zero_one_knapsack(products, capacity, index):
    if capacity <= 0 or index < 0 or index >= len(products):
        return 0
    elif products[index].weight < capacity:
            
        acum_value1 = acum_item = products[index].value + zero_one_knapsack(products, capacity - products[index].weight, index+1)
        acum_value2 = zero_one_knapsack(products, capacity, index+1)
        print(acum_value1, acum_value2)
        return max(acum_value1, acum_value2)
    else:
        return 0


product1 = Product(3, 6) # 29 #   # 6 # 8 # 10 # 5
product2 = Product(4, 8)
product3 = Product(2, 10)
product4 = Product(1, 5)

products = [product1, product2, product3, product4]
print(zero_one_knapsack(products, 10, 0))

item1 = Product(3, 31)
item2 = Product(1, 26)
item3 = Product(2, 17)
item4 = Product(5, 72)
items = [item1, item2, item3, item4]
#print(zero_one_knapsack(items, 7, 0))



