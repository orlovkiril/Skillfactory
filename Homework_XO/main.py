field = list(range(1, 10))

def draw(field):
    for i in range(3):
        print(field[0+i*3], '|', field[1+i*3], '|', field[2+i*3])
    print('')

def check_win(field):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for i in win:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def game(field):
    counter = 0
    win = False

    while not win:
        draw(field)
        choice = int(input("Введите номер клетки: "))

        if choice not in field:
            print("Ошибка ввода! Повторите ввод.")
        elif str(field[choice - 1]) in "X0":
            print("Клетка занята! Повторите ввод.")
        else:
            if counter % 2 == 0:
                field[choice - 1] = "X"
            else:
                field[choice - 1] = "0"
            counter += 1

        player = check_win(field)
        if player:
            print(player, "выиграл!")
            break
        if counter == 9:
            print("Ничья!")
            break

game(field)