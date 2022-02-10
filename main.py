def hello():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show_table():
    print()
    print("    0 1 2")
    for i, row in enumerate(table):
        row_str = f"  {i} {' '.join(row)}"
        print(row_str)
    print()

def ask_coordinate():
    while True:
        cords = input("Ваш ход: ").split()
        
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" Координаты вне диапазона! ")
            continue
        
        if table[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y
            
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(table[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

hello()
table = [[" "] * 3 for i in range(3)]
count = 0
while count < 9:
    count += 1
    show_table()
    if count % 2 == 1:
        print(" Ходит X")
    else:
        print(" Ходит 0")
    
    x, y = ask_coordinate()
    
    if count % 2 == 1:
        table[x][y] = "X"
    else:
        table[x][y] = "0"
    
    if check_win():
        break
    
if count == 9:
    print(" Ничья!")
