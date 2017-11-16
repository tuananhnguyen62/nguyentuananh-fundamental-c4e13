array = [1, 2, 6, 9, 20, 40, 50]
# array.sort()
x = int(input("Enter a number: "))
start = 0
stop = len(array)
found_index = -1
mid = (start + stop) // 2
while (stop - start) >1:
    if x < array[mid]:
        mid = (start + stop) // 2
        stop = mid
    elif x > array[mid]:
        mid = (start + stop + 1) // 2
        start = mid
    else:
        found_index = mid
        break
if found_index == -1:
    print("Not found")
else:
    print("Found at: ", found_index)
# 21 -> len = 7 -> mid = 3 -> arraymid = 6 -> 21  > 6 -> start = 3 -> mid = 4 -> arraymid = 20 -> 21>20 ->start = 3
