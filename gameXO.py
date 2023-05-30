board = [' '] * 9
def display_board():
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')

def move(player, position):# игрок ходит
    board[position] = player

def win(player):
    if (board[0] == board[1] == board[2] == player) or \
       (board[3] == board[4] == board[5] == player) or \
       (board[6] == board[7] == board[8] == player) or \
       (board[0] == board[3] == board[6] == player) or \
       (board[1] == board[4] == board[7] == player) or \
       (board[2] == board[5] == board[8] == player) or \
       (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

player = 'X'
while True: # запускаю цикл игры что бы она не закрывалась
    display_board()
    a = int(input("Выберите позицию (смотрите на numpad): ")) - 1
    if board[a] == ' ':
        move(player, a)
        if win(player):
            display_board()
            print("Победил игрок", player)
            break
        elif ' ' not in board:
            display_board()
            print("Ничья!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Неверный ход. Попробуйте еще раз.")
