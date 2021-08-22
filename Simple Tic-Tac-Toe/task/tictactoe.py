cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

X_Counter = 0
O_Counter = 0
Void_Counter = 9
X_turn = True


def game_print():
    print("---------")
    print("| " + cells[0][0] + " " + cells[0][1] + " " + cells[0][2] + " |")
    print("| " + cells[1][0] + " " + cells[1][1] + " " + cells[1][2] + " |")
    print("| " + cells[2][0] + " " + cells[2][1] + " " + cells[2][2] + " |")
    print("---------")


def coords_input():
    while True:
        try:
            x0, y0 = input("Enter the coordinates: ").split()
            x0 = int(x0)
            y0 = int(y0)
        except ValueError:
            print("You should enter numbers!")
            continue
        if 4 > x0 > 0 and 4 > y0 > 0:
            if cells[x0 - 1][y0 - 1] == ' ':
                return x0, y0
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("coordinates should be from 1 to 3")


def status():
    global Void_Counter
    x_wins = ((cells[0][0] == "X" and cells[0][1] == "X" and cells[0][2] == "X"
               or cells[1][0] == "X" and cells[1][1] == "X"
               and cells[1][2] == "X"
               or cells[2][0] == "X" and cells[2][1] == "X"
               and cells[2][2] == "X")
              or (cells[0][0] == "X" and cells[1][0] == "X"
                  and cells[2][0] == "X"
                  or cells[0][1] == "X" and cells[1][1] == "X"
                  and cells[2][1] == "X"
                  or cells[0][2] == "X" and cells[1][2] == "X"
                  and cells[2][2] == "X")
              or (cells[0][0] == "X" and cells[1][1] == "X"
                  and cells[2][2] == "X"
                  or cells[2][0] == "X" and cells[1][1] == "X"
                  and cells[0][2] == "X"))
    o_wins = ((cells[0][0] == "O" and cells[0][1] == "O" and cells[0][2] == "O"
               or cells[1][0] == "O" and cells[1][1] == "O"
               and cells[1][2] == "O"
               or cells[2][0] == "O" and cells[2][1] == "O"
               and cells[2][2] == "O")
              or (cells[0][0] == "O" and cells[1][0] == "O"
                  and cells[2][0] == "O"
                  or cells[0][1] == "O" and cells[1][1] == "O"
                  and cells[2][1] == "O"
                  or cells[0][2] == "O" and cells[1][2] == "O"
                  and cells[2][2] == "O")
              or (cells[0][0] == "O" and cells[1][1] == "O"
                  and cells[2][2] == "O"
                  or cells[2][0] == "O" and cells[1][1] == "O"
                  and cells[0][2] == "O"))
    if x_wins and o_wins:
        return "Impossible"
    elif not x_wins and o_wins:
        return "O wins"
    elif x_wins:
        return "X wins"
    elif Void_Counter == 0:
        return "Draw"
    else:
        return "Game not finished"


game_print()
while True:
    x, y = coords_input()
    if X_turn:
        cells[x - 1][y - 1] = 'X'
        Void_Counter -= 1
    else:
        cells[x - 1][y - 1] = 'O'
        Void_Counter -= 1
    game_print()
    state = status()
    if not state == 'Game not finished':
        print(state)
        break
    X_turn = not X_turn
