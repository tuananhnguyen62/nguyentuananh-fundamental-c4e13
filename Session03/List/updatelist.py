menu = ['com', 'bun', 'pho', 'thit']
for index, item in enumerate(menu):
 print(index +1,". ", item, sep='')
print("*"  *20)
n=int(input("Ban muon update item o vi tri nao? "))
m=input("Ban muon thay bang gi? ")
# menu.remove(menu[n-1])
# menu.insert(n-1,m)
index = n - 1
menu[index] = m
for index, item in enumerate(menu):
    print(index +1,". ", item, sep='')
