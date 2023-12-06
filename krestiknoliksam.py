def print_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")
        print('-' * 13)


def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[2][0]

    return None


def full_board(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def tick_tack_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input('Введите номер строки(0, 1, 2):'))
        col = int(input('Введите номер столбца(0, 1, 2):'))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print('Эта клетка уже занята. Выберете другую')
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f'Игрок {winner} победил')
            break

        if full_board(board):
            print_board(board)
            print('Ничья')
            break

        current_player = '0' if current_player == 'X' else 'X'
        print(f'\nХод игрока {current_player}\n')


if __name__ == "__main__":
    tick_tack_toe()
