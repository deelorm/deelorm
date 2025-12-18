
def coin_change(amount, coins):
    coins.sort()
    for i in range(len(coins)-1, -1, -1):
        while coins[i] <= amount:
            print(coins[i])
            amount -= coins[i]
        if amount == 0:
            break

coins = [1,2,5,10,20,50,100]
coin_change(491, coins)



