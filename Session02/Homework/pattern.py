column = int(input("Number of stars in row: "))
row = int(input("Number of row: "))
print("This is your pattern:")
for y in range(row):
    for x in range(column):
        if (x+y) % 2 ==0:
            print("* ", end="")
        else:
            print("x ", end="")
    print()
