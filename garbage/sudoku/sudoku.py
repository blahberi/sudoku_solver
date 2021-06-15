from garbage.sudoku.number import Number
from garbage.sudoku.blank import Blank
from garbage.sudoku.block import Block


def __reshape(mat, dim):
    res = []
    if isinstance(mat[0], list):
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                res.append(mat[y][x])
    else:
        for y in range(dim[0]):
            res.append([])
            for x in range(dim[1]):
                res[y].append(mat[y * (dim[0]) + x])
    return res


def create_blocks(blocks):
    res = []
    start = 0
    end = 9
    for i in range(9):
        res.append(__string_to_block(blocks[start:end]))
        start += 9
        end += 9
    return __reshape(res, (3, 3))


class Sudoku:
    def __init__(self, blocks):
        self.blocks = create_blocks(blocks)

    def __str__(self):
        res = ''
        for row_blocks in self.blocks:
            for block in row_blocks:
                res += str(block)
                res += '\n'
        return res


def __string_to_block(string_block):
    res_numbers = []
    res_blanks = []
    y = 0
    x = 0
    i = 0
    for y in range(3):
        for x in range(3):
            number = string_block[i]
            if number == ' ':
                # number is a blank
                res_blanks.append(
                    Blank((x, y))
                )
            else:
                # number is a given number and not a blank
                if number.isdigit():
                    res_numbers.append(
                        Number(
                            int(number),
                            (x, y)
                        )
                    )
                else:
                    return
            i += 1

    res = Block(
        res_numbers,
        res_blanks
    )
    return res