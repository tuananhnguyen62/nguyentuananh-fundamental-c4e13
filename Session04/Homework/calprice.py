prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {}
stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15
# print(stock)

for i in prices:
    print("""• {0}: {1}
• price: {2}""".format(i, stock[i], prices[i]))
    print()

total = 0
for n in prices:
    print("Money from selling all {0} is {1}".format(n, prices[n] * stock[n]))
    money = (prices[n] * stock[n])
    total += money
print("Total money: ",total)
