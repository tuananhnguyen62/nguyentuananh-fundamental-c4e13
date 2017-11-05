from random import randint
a = randint(1,20)
loop_continue = True
guess_count = 0
while loop_continue:
    n = int(input("Guess my number (1-20): "))
    if n == a:
        print("Bingo!")
        # loop_continue = False
        break
    elif n < a:
        print("Too small")
        guess_count += 1
    else:
        print("Too big")
        guess_count += 1
    if guess_count > 8:
        print("Game Over!")
        break
