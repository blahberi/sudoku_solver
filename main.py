from sudoku.sudoku import Sudoku
from sudoku import solver

board_strings = []
for i in range(9):
    line = input(f'input line {i + 1}:')
    board_strings.append(line)

sudoku = Sudoku(board_strings)
print(sudoku)
solver.solve(sudoku)
print('##################')
print(sudoku)