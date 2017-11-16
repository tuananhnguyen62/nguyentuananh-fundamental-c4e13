numbers = [1, 6, 8, 1, 2, 1, 5, 6]
x = int(input("Enter a number: "))

# cach 1:
count_x = numbers.count(x)

#cach 2:
count_x = 0
for index in numbers:
    if index == x:
        count_x += 1

if count_x == 0:
    print("Not found in list")
else:
    print("{0} appears {1} times in the list".format(x, count_x))
