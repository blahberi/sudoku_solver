from sudoku.sudoku import Sudoku
from sudoku import solver
import time

board_strings = []

for i in range(9):
    while True:
        line = input(f'input line {i + 1}:')
        if len(line) == 9:
            board_strings.append(line)
            break
        print(f'line has to be 9 numbers/blanks together this line has {len(line)} numbers/blanks')

sudoku = Sudoku(board_strings)
print(sudoku)
solver.solve(sudoku, is_print=True, print_delay=0)
print('##################')
print(sudoku)
