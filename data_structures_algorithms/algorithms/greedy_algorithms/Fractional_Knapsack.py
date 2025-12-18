

class Product:
    def __init__(self, weight, value):
        self.weight = weight 
        self.value = value 
        self.density = self.value / self.weight

    def fractional_knapsack(self, products, max_weight):
        max_value = 0
        total_weight_used = 0
        products.sort(key=lambda i:i.density, reverse=True)
        for i in products:
            if i.weight <= (max_weight - total_weight_used):
                max_value += i.value 
                total_weight_used  += i.weight
            else:
                value = i.density * (max_weight - total_weight_used)
                max_value += value
                total_weight_used  += (max_weight - total_weight_used)
            if total_weight_used == max_weight:
                return max_value 


product1 = Product(10, 15)
product2 = Product(20, 20)
product3 = Product(40, 30)
product_list = [product1, product2, product3]

print(product1.fractional_knapsack(product_list, 60))


