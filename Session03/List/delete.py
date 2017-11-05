menu = ['com ga','pho bo', 'bun bo', 'mien ga']
print(*menu, sep=', ')
print("*" * 20)
n = input("Ban muon bo mon nao? ")

if n in menu:
    menu.remove(n)
    print(*menu, sep=', ')
else:
    print(n, "khong co trong list")
