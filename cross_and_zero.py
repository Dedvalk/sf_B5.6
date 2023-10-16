def print_table(data):
    print(' ', *range(size))
    for i in range(size):
        print(i, *data[i])

def check_step(x, y):
    if x >= size or \
       y >= size or \
       x < 0 or \
       y < 0:
        print('Некорректные координаты')
        return False
    if table[x][y] != '-':
        print('Данное поле уже занято')
        return False
    return True

def check_draw():
    return '-' not in ''.join([''.join(x) for x in table])

def check_victory():
    #проверка вертикалей и горизонталей
    for i in range(size):
        if ''.join(table[i]) == table[i][0] * size and table[i][0] != '-':
            return True
        column = ''.join([table[j][i] for j in range(size)])
        if column == table[i][i] * size and table[i][i] != '-':
            return True
    #проверка диагоналей
    primary_d = ''.join([table[i][i] for i in range(size)])
    if primary_d == table[0][0] * size and table[0][0] != '-':
        return True
    second_d = ''.join([table[i][size - i - 1] for i in range(size)])
    if second_d == table[size - 1][0] * size and table[size - 1][0] != '-':
        return True

    return False

def step(symbol):
    while True:
        x, y = tuple(map(int, input(f'Ход игрока "{symbol}": ').split()))
        if check_step(x, y):
            table[x][y] = symbol
            break

def play():
    print_table(table)
    print('Вводите координаты через пробел поочередно')
    player = ''

    while not check_victory():
        if check_draw():
            print('Ничья!')
            break
        player = 'x' if player in ('', '0') else '0'
        step(player)
        print_table(table)
    else:
        print(f'Победа {player}!')

size = 3
table = [['-'] * size for i in range(size)]

play()
