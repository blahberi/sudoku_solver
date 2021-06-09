from garbage.sudoku import Number


def solve(sudoku):
    solved_blocks = set()
    start_sudoku = sudoku
    runs = 0
    while True:
        for y in range(3):
            for x in range(3):
                for currentBlank in sudoku.blocks[y][x].blanks:
                    for i in range(3):
                        block = sudoku.blocks[i][x]
                        if block == sudoku.blocks[y][x]:
                            for number in block.numbers:
                                if number.number in currentBlank.possibilities:
                                    currentBlank.possibilities.remove(number.number)
                        else:
                            for number in block.numbers:
                                if number.pos[0] == currentBlank.pos[0]:
                                    if number.number in currentBlank.possibilities:
                                        currentBlank.possibilities.remove(number.number)

                    for i in range(3):
                        block = sudoku.blocks[y][i]
                        if block == sudoku.blocks[y][x]:
                            for number in block.numbers:
                                if number.number in currentBlank.possibilities:
                                    currentBlank.possibilities.remove(number.number)
                        else:
                            for number in block.numbers:
                                if number.pos[1] == currentBlank.pos[1]:
                                    if number.number in currentBlank.possibilities:
                                        currentBlank.possibilities.remove(number.number)

                    if len(currentBlank.possibilities) == 1:
                        number = currentBlank.possibilities[0]
                        number_pos = currentBlank.pos
                        sudoku.blocks[y][x].blanks.remove(currentBlank)
                        sudoku.blocks[y][x].numbers.append(
                            Number(number, number_pos)
                        )
                if not sudoku.blocks[y][x].blanks:
                    solved_blocks.add(sudoku.blocks[y][x])
        runs += 1
        if len(solved_blocks) == 9:
            return