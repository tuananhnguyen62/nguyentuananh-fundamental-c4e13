from random import *
from simple_cal import eval
#dung eval de tinh cac truong hop

while True:
    x = randint(0,100)
    y = randint(0,100)
    error = randint(-1,1)
    # operators = ['+','-','*','/']
    op = choice(['+','-','*','/'])
    result = eval(x, y, op) + error
    

    print("{0} {3} {1} = {2}".format(x,y,result,op))

    user = input("Y/N? ").upper()
    if error == 0:
        if user == "Y":
            a = 1
        else:
            a = 0
    else:
        if user == "N":
            a = 1
        else:
            a = 0
    if a == 1:
        print("Good")
    else:
        print("Stupid")
