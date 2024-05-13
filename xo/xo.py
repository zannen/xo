

# A global variable called "board", which is a 2D array storing the current
# noughts and crosses board.
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def print_board():
    # A function which prints the current state of the board.
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="")
        print("|")


def finished():
    # A function which tells us if the game has finished, and if so, who has
    # won.

     The game is finished if:

    # X has won


print_board()





# Topics to teach, in approximate order of complexity
#
# - Comments
#       lines beginning with "#", and from "#" to the end of the line.
# - print statement
#       output something on the screen, with/without a newline character.
# - Strings
#       a piece of text, zero or more characters, surrounded by double quotes.
# - Functions
#       blocks of code which can be called from anywhere. They may return some
#       information, but don't have to.
# - For loops
#       Iterate through a list of things, setting a temporary variable to the
#       current list item.