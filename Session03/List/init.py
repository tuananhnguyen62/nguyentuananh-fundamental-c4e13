# menu = []
# print(menu)
# menu = ['chan ga sa ot']
# print(menu)
menu = ['chan ga sa ot', 'ga xao pho mai', 'com rang dua bo']
print(*menu, sep=', ')
print("*" * 10)
# menu.append(input("Ban muon them gi: "))
# n  = input("Ban muon them gi: ")
menu.insert(0,input("Mon an moi nhat la gi? "))
print(*menu, sep=', ')
