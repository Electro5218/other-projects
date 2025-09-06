from random import randint

def display_board_actual_status(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def enter_move(board,signplayer):
    while True:
        ruch = int(input("Wybierz wolne pole: "))
        if ruch < 0 or ruch > 8:
            print("Nie ta wartość")
        elif board[ruch] == 0 or board[ruch] == 1 or board[ruch] == 2 or board[ruch] == 3 or board[ruch] == 4 or board[ruch] == 5 or board[ruch] == 6 or board[ruch] == 7 or board[ruch] == 8:
            board[ruch] = signplayer
            break
        else:
            print("Pole zajęte spróbuj ponownie")

def enter_move_computer(board,signcomputer):
    while True:
        ruchkomputera = randint(0, 8)
        if board[ruchkomputera] == 0 or board[ruchkomputera] == 1 or board[ruchkomputera] == 2 or board[ruchkomputera] == 3 or board[ruchkomputera] == 4 or board[ruchkomputera] == 5 or board[ruchkomputera] == 6 or board[ruchkomputera] == 7 or board[ruchkomputera] == 8:
            board[ruchkomputera] = signcomputer
            break


def victory_for(board, signplayer, signcomputer):
    if board[0] == board[4] == board[8] == signplayer:
        print("Wygrałeś")
        board[0] = f"\033[4m{board[0]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[8] = f"\033[4m{board[8]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[0] == board[4] == board[8] == signcomputer:
        print("Wygrał komputer")
        board[0] = f"\033[4m{board[0]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[8] = f"\033[4m{board[8]}\033[0m"
        display_board_actual_status(board)
        return
    elif board[2] == board[4] == board[6] == signplayer:
        print("Wygrałeś")
        board[2] = f"\033[4m{board[2]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[6] = f"\033[4m{board[6]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[2] == board[4] == board[6] == signcomputer:
        print("Wygrał komputer")
        board[2] = f"\033[4m{board[2]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[6] = f"\033[4m{board[6]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[0] == board[1] == board[2] == signplayer:
        print("Wygrałeś")
        board[0] = f"\033[4m{board[0]}\033[0m"
        board[1] = f"\033[4m{board[1]}\033[0m"
        board[2] = f"\033[4m{board[2]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[0] == board[1] == board[2] == signcomputer:
        print("Wygrał komputer")
        board[0] = f"\033[4m{board[0]}\033[0m"
        board[1] = f"\033[4m{board[1]}\033[0m"
        board[2] = f"\033[4m{board[2]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[3] == board[4] == board[5] == signplayer:
        print("Wygrałeś")
        board[3] = f"\033[4m{board[3]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[5] = f"\033[4m{board[5]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[3] == board[4] == board[5] == signcomputer:
        print("Wygrał komputer")
        board[3] = f"\033[4m{board[3]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[5] = f"\033[4m{board[5]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[6] == board[7] == board[8] == signplayer:
        print("Wygrałeś")
        board[6] = f"\033[4m{board[6]}\033[0m"
        board[7] = f"\033[4m{board[7]}\033[0m"
        board[8] = f"\033[4m{board[8]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[6] == board[7] == board[8] == signcomputer:
        print("Wygrał komputer")
        board[6] = f"\033[4m{board[6]}\033[0m"
        board[7] = f"\033[4m{board[7]}\033[0m"
        board[8] = f"\033[4m{board[8]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[0] == board[3] == board[6] == signplayer:
        print("Wygrałeś")
        board[0] = f"\033[4m{board[0]}\033[0m"
        board[3] = f"\033[4m{board[3]}\033[0m"
        board[6] = f"\033[4m{board[6]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[0] == board[3] == board[6] == signcomputer:
        print("Wygrał komputer")
        board[0] = f"\033[4m{board[0]}\033[0m"
        board[3] = f"\033[4m{board[3]}\033[0m"
        board[6] = f"\033[4m{board[6]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[1] == board[4] == board[7] == signplayer:
        print("Wygrałeś")
        board[1] = f"\033[4m{board[1]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[7] = f"\033[4m{board[7]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[1] == board[4] == board[7] == signcomputer:
        print("Wygrał komputer")
        board[1] = f"\033[4m{board[1]}\033[0m"
        board[4] = f"\033[4m{board[4]}\033[0m"
        board[7] = f"\033[4m{board[7]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[2] == board[5] == board[8] == signplayer:
        print("Wygrałeś")
        board[2] = f"\033[4m{board[2]}\033[0m"
        board[5] = f"\033[4m{board[5]}\033[0m"
        board[8] = f"\033[4m{board[8]}\033[0m"
        display_board_actual_status(board)
        return True
    elif board[2] == board[5] == board[8] == signcomputer:
        print("Wygrał komputer")
        board[2] = f"\033[4m{board[2]}\033[0m"
        board[5] = f"\033[4m{board[5]}\033[0m"
        board[8] = f"\033[4m{board[8]}\033[0m"
        display_board_actual_status(board)
        return True
    else:
        return False

def is_occupied(board):
    flag = True
    for element in board:
        if element == 0 or element == 1 or element == 2 or element == 3 or element == 4 or element == 5 or element == 6 or element == 7 or element == 8:
            flag = False
    if flag == False:
        return False
    else:
        return True

def tic_tac_toe():
    board = [i for i in range(9)]
    while True:
        signplayer = input("Kółko czy krzyżyk?(x albo o): ")
        if signplayer == 'x' or signplayer == 'o':
            break
        else:
            print("Niepoprawna wartość, spróbuj ponownie")
    if signplayer == 'x':
        signcomputer = 'o'
    elif signplayer == 'o':
        signcomputer = 'x'
    while not victory_for(board, signplayer, signcomputer):
        display_board_actual_status(board)
        enter_move(board, signplayer)
        if is_occupied(board) and not victory_for(board, signplayer, signcomputer):
            print("Nie ma już miejsca na planszy")
            display_board_actual_status(board)
            break
        enter_move_computer(board,signcomputer)

if __name__ == '__main__':
    tic_tac_toe()