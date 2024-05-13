def print_board(board):
    # A function which prints the current state of the board.
    for row in board:
        for cell in row:
            print("(", cell, ") ", end="")
        print()


def finished(board):
    # A function which tells us if the game has finished, and if so, who has
    # won.

    # The game is finished if:

    for player in ["X", "O"]:
        # Check if this player has won.

        # Check rows
        for row in board:
            if row[0] == player and row[1] == player and row[2] == player:
                return player

        # Check columns
        for i in range(3):
            if (
                board[0][i] == player
                and board[1][i] == player
                and board[2][i] == player
            ):
                return player

        # Check 2 diagonals
        if (
            board[0][0] == player
            and board[1][1] == player
            and board[2][2] == player
        ):
            return player
        if (
            board[0][2] == player
            and board[1][1] == player
            and board[2][0] == player
        ):
            return player

    # nobody has won

    # Is the board filled?
    if all(all(row[i] != " " for i in range(3)) for row in board):
        return "stalemate"

    # The game continues...
    return ""


def print_finished_message(fin):
    if fin == "":
        # do nothing
        return

    print("The game has ended.")
    if fin in ["X", "O"]:
        print("Player ", fin, " won.")
    else:
        print("It's a ", fin)


def get_row_col(board):
    while True:
        rownum = -1
        while rownum < 1 or rownum > 3:
            rownum = int(input("What row (1-3) ?"))
        colnum = -1
        while colnum < 1 or colnum > 3:
            colnum = int(input("What col (1-3) ?"))
        if board[rownum - 1][colnum - 1] == " ":
            # The space is empty, we can go here.
            break
        print("That position is occupied.")

    return rownum, colnum


def run():
    # A variable called "board", which is a 2D array storing the current
    # noughts and crosses board.
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    while True:
        # Players take turns.
        for player in ["X", "O"]:
            print()
            print_board(board)
            print("It is player ", player, "'s turn.")
            rownum, colnum = get_row_col(board)
            board[rownum - 1][colnum - 1] = player
            fin = finished(board)
            if fin != "":
                print_finished_message(fin)
                return
