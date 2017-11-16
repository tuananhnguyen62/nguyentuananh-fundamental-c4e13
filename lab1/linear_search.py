numbers = [1, 4, -2, 5, -10, 20, 125]

x = int(input("Enter your number: "))
count = 0
for n in numbers:
    if n == x:
        count += 1
        a = str("Found {0} at position {1}".format(x, numbers.index(x)+1))
        break

if count != 0:
    print(a)
else:
    print("Not found")
