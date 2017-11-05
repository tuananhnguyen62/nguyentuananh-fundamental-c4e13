menu =  ['com', 'bun', 'pho']
print(*menu, sep=", ")
print("*" * 20)
menu.remove('bun')
print(*menu, sep=", ")
