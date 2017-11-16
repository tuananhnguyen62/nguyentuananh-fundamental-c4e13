list = [1, 5,-10, -100, -99]
min_list = list[0]
max_list = list[0]

for n in list:

    if min_list > n:
        min_list = n

print(min_list)
