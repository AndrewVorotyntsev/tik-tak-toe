# Создаем двумерный массив
matrix = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
global flag_win
flag_win = 0
# Функция,  отображающая поле
def show_field(m):
    for i in [0, 1, 2]:
        print(m[i][0], m[i][1], m[i][2])


# Функция , позволяющая сделать ход
def make_move(x, y, m, team):
    if team == "o":
        m[x][y] = "O"
    if team == "x":
        m[x][y] = "X"
    return m


# Функция , проверяющая победные условия
def check_win(m):
    for i in [0, 1, 2]:
        if m[i][0] == m[i][1] == m[i][2] != "*":
            print("Конец игры")
            global flag_win
            flag_win = 1
            return flag_win

        if m[0][i] == m[1][i] == m[2][i] != "*":
            print("Конец игры")
            flag_win = 1
            return flag_win
    if m[0][0] == m[1][1] == m[2][2] != "*":
        print("Конец игры")
        flag_win = 1
        return flag_win
    if m[0][2] == m[1][1] == m[2][0] != "*":
        print("Конец игры")
        flag_win = 1
        return flag_win


print("Начало игры!")
show_field(matrix)
while flag_win != 1:
    print("Сделайте шаг O")
    print("Введите x координату.")
    x = int(input())
    print("Введите y координату.")
    y = int(input())
    make_move(x, y, matrix, "o")
    show_field(matrix)
    check_win(matrix)
    if flag_win == 1:
        print("O - победа")
    else:
        print("Сделайте шаг X")
        print("Введите x координату.")
        x = int(input())
        print("Введите y координату.")
        y = int(input())
        make_move(x, y, matrix, "x")
        show_field(matrix)
        check_win(matrix)
        if flag_win == 1:
            print("X - победа")