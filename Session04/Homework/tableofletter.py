table = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
}
table_list = list(table)
# print(table)

word = input("Please create your sentence: ")
word_list = list(word)
for index in range(len(word_list)):
    # print(word_list[index])
    if word_list[index] in table:
        n = word_list[index]
        table[n] += 1

table = {key:val for key, val in table.items() if val != 0}

print(table)
