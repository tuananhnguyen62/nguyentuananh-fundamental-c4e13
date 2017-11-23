from random import *
from simple_cal import eval
# score = 0

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    error = randint(-1,1)
    op = choice(['+','-','*','/'])
    result = eval(x, y, op) + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    error = eval(x,y,op) - result
    if user_choice:
        if error == 0:
            return True
                # print("Congrats!")
        else:
            return False
                # print("Game over")
    else:
        if error == 0:
            return False
                # print("Game over")
        else:
            return True
                # print("Congrats!")
