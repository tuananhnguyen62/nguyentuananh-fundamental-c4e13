def eval(x, y, operation):
    if operation == "+":
            result = x + y
    elif operation == "-":
            result = x - y
    elif operation == "*":
            result = x*y
    elif operation == "/":
        if y == 0:
                result = 'NaN'
        else:
                result = x/y
    return result

# x1 = 10
# y2 = 10
# operation3 = '+'
# r = eval(1, 2,'-')
# print (r)
# s = eval()
#
# x = int(input(" x = :"))
# operation = input("Operation (+,-,*,/): ")
# y = int(input(" y = :"))
# if operation in ["+", "-", "*", "/"]:
#     r = eval()
#
#     print("{0} {1} {2} = {3}".format(x,operation,y,r))
# else:
#     print("Wrong syntax")
