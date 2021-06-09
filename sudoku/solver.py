from sudoku.sudoku import Sudoku


def is_valid(sudoku, number, position):
    # check the row of the number we are trying to insert
    for i in range(9):
        if sudoku.board[position[0]][i] == number:
            if i != position[1]:  # skip over the number we are trying to insert
                return False

    # check the column of the number we are trying to insert
    for i in range(9):
        if sudoku.board[i][position[1]] == number:
            if i != position[0]:  # skip over the number we are trying to insert
                return False

    # check the 9x9 box of the number were trying to insert
    box_x = position[1] // 3
    box_y = position[0] // 3

    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if sudoku.board[y][x] == number:
                if position != (y, x):
                    return False

    return True


def find_blank(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku.board[y][x] == 0:
                return (y, x)


def solve(sudoku):
    # get the first blank that the computer can find
    blank = find_blank(sudoku)
    if not blank:
        return True
    y, x = blank

    # insert every possible number
    for i in range(9):
        i = i + 1
        if is_valid(sudoku, i, (y, x)):  # if it is possible to insert the number in the blank
            sudoku.board[y][x] = i  # insert it

            if solve(sudoku):  # use recursion to go on to the next blank
                return True

            sudoku.board[y][x] = 0

    return False
