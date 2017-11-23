
# n = 0
# m = 1
# for i in range(4):
#     month = i
#     m = n+ m
#     n = m
#
#     # print("Month {}: {1} pair(s) of rabbits".format(month, m))
#     print(m)

mature = 1
newborn = 0
new_mature = 0

for i in range(5):
    total = mature + new_mature + newborn
    newborn = mature
    mature = mature + new_mature
    new_mature = newborn
    newborn = 0
    print("Month {0}: {1} pair(s) of rabbit".format(i,total))
