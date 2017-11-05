from random import choice
s = input("Type your word here: ")
characters = list(s)
n = len(characters)

while n >0:
    c = choice(characters)
    characters.remove(c)
    n += -1
    print(c, end="")
print()
a = input("Guess the word: ")
# thiếu trường hợp khi nhập sai
while a != s:
    b = input("Guess again: ")
    if b == s:
        print("Bingo")
        break

    # cho phép user nhập input
    # so sánh với từ s ban đầu

    # break
# print("bingo")
