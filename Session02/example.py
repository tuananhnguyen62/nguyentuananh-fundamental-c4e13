# a = int(input("Enter a number: "))
# # for i in range(n):
# #     print(i)
#
# # print(*range(a))
#
# # or
#
# print(i, end=', ')

# a = int(input("Enter a number: "))
# b = a%2
# if b==0:
#     for i in range(0, a, 2):
#         print(i, end=', ')
# else:
#     for i in range(0, a+1, 2):
#         print(i, end=', ')

a = int(input("Enter a number: "))
for i in range (a):
    if i%2 ==0:
        print("Fish")
    if i%3 ==0:
        print("Bird")
