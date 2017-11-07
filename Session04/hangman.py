# Lập từ điển các từ để chơi
from random import choice
storage_word = ["apple", "orange","blackberry"]
picture = [
"""
 |-------
 |      O
 |    --|--
 |     / \\
 |
_|_
""",
"""
 |-------
 |      O
 |    --|--
 |     /
 |
_|_
""",
"""
 |-------
 |      O
 |    --|--
 |
 |
_|_
""",
"""
 |-------
 |      O
 |    --|
 |
 |
_|_
""",
"""
 |-------
 |      O
 |      |
 |
 |
_|_
""",
"""
 |-------
 |      O
 |
 |
 |
_|_
"""
]
# random ra 1 từ để chơi
word = choice(storage_word)
# Hiển thị từ được chọn
original_word = list(word)
list_word = list(word)
for i in range(len(word)):
    list_word[i] = "_"
print(*list_word)

guess_left = 5
# Cho đoán từ
while guess_left > 0:
    print("Suggesstion: This is a kind of fruit")
    letter = input("Guess a letter: ")
    if letter in original_word:
        # giải quyết bài toàn có 2 chữ trùng nhau trở lên
        # Từ từ được đoán, hiện ra các chữ cần lật
        for index in range (len(original_word)):
            if  original_word[index] == letter:
                list_word[index] = letter
                print(*list_word)
                # Đoán hết số từ >>> thắng
        if "_" not in list_word:
            print("You are winner!")
            break
    else:
        guess_left += -1
        print(picture[guess_left])
        print(*list_word)
else:
    print(picture[0])
    print("Game over!")
    # cho vòng lặp while đến khi guess_left = 0 >>> done
# Vẽ hình treo cổ
