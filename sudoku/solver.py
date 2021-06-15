from sudoku.sudoku import Sudoku
import time
import math
recursion_amount = 0
recursion_number = 0


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


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


def __erase_sudoku():
    for i in range(12):
        print('\033[F', end='')
        print('\033[K', end='')


def solve(sudoku, is_print=False, print_delay=0.05):
    global recursion_amount
    global recursion_number
    recursion_number = 0
    if is_print:
        sudoku_copy = Sudoku(sudoku.board_strings)
        print('solving sudoku:')
        print(sudoku)
        __solve(sudoku_copy, False, print_delay)
        recursion_amount = recursion_number
        recursion_number = 0
        print()
    __solve(sudoku, is_print, print_delay)


def __solve(sudoku, is_print, print_delay):
    global recursion_amount
    global recursion_number
    spaces = ''
    end_spaces = ''
    percent = 0
    if is_print:
        if print_delay >= 0.05:
            time.sleep(print_delay)
        else:
            time.sleep(0.01)
        percent = round_half_up(recursion_number / recursion_amount * 100, 2)
        for i in range(int(percent)):
            spaces += ' '
        for i in range(100 - int(percent)):
            end_spaces += ' '


    # get the first blank that the computer can find
    blank = find_blank(sudoku)
    if not blank:
        # there is no blank to find so the sudoku is solved
        return True

    y, x = blank

    # insert every possible number in the blank
    for i in range(9):
        i = i + 1
        if is_valid(sudoku, i, (y, x)):  # if it is possible to insert the number in the blank
            sudoku.board[y][x] = i  # insert it
            if is_print:
                print('\r', end='')
                __erase_sudoku()
                print(sudoku)
                print(f'\u001b[47;1m{spaces} \u001b[0m{end_spaces}|{percent}%', end='')

            recursion_number += 1
            if __solve(sudoku, is_print, print_delay):  # use recursion to go on to the next blank
                return True

            sudoku.board[y][x] = 0

    return False
