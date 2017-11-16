numbers = [1, 2, 6, 9, 20, 40, 50]
x = int(input("Enter a number: "))
start = 0
stop = len(numbers)  -  1
found_index = -1
mid = (start + stop) //2
while (stop - start) >1:

    if x == numbers[mid]:
        found_index = mid
        break
    elif x < numbers[mid]:
        stop = mid
        mid = (start + stop -1) //2
    else:
        start = mid
        mid = (start + stop) //2
if found_index == -1:
    print("Not found")
else:
    print("Found at index {} in number".format(found_index))
