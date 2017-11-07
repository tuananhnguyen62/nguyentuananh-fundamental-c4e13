teen_dict = {
    'ck': 'chồng',
    'vk': 'vợ',
    'dk': 'được',
    'cc': 'cục cưng',
    'idk': 'I dont know',
}
while True:
    print(teen_dict)
    look_up = input("Enter your code for translation: ")
    if look_up in teen_dict:
        print(teen_dict[look_up])
    else:
        while True:
            new_word = input("Not found, do you want to contribute this word? (Y/N) ")
            if new_word.upper() == "Y":
                teen_dict[look_up] = input("Enter your new translation: ")
                print("Updated")
                break
            elif new_word.upper() == "N":
                print("Thank you")
                break
            else:
                print("No function, please choose Y or N")
