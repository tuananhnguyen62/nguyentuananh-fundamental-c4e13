menu = ['T-shirt', 'Sweater']
order_list = ['C', 'R', 'U', 'D' ]

while True:
    a = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if a.upper() not in order_list:
        print("No function, please select again.")
    else:
        if a.upper() == "C":
            new_item = input("Enter new item: ")
            menu.append(new_item)
            print("Our items: ", end='')
            print(*menu, sep=', ')
        else:
            menu.append('Jeans')
            if a.upper() == "R":
                print("Our items: ", end='')
                print(*menu, sep=', ')

            elif a.upper() == "U":
                number_item = len(menu)
                while True:
                    update_position = int(input("Update position? "))
                    if update_position > len(menu):
                        print("Out of index, please select again")
                    else:
                        update_item = input("New item? ")
                        menu[update_position] = update_item
                        print("Our items: ", end='')
                        print(*menu, sep=', ')
                        break

            elif  a.upper() == "D" :
                while True:
                    del_position = int(input("Delete position? "))
                    if del_position > len(menu):
                        print("Out of index, please select again")
                    else:
                        del_item = menu[del_position - 1]
                        menu.remove(del_item)
                        print("Our items: ", end='')
                        print(*menu, sep=', ')
                        break
        break
