"""
a block is a 9x9 grid of number
in a standard sudoku game there are 9 blocks
"""
from garbage.sudoku.number import Number


class Block:
    def __init__(self, numbers, blanks):
        if len(numbers) + len(blanks) == 9:
            self.numbers = numbers
            self.blanks = blanks
        else:
            raise Exception('Make sure that there are 9 objects in block')

    def __str__(self):
        all_objects = []
        for number in self.numbers:
            all_objects.append(number)

        for blank in self.blanks:
            all_objects.append(blank)
        res = ''
        obj = None
        for y in range(3):
            for x in range(3):
                for o in all_objects:
                    if o.pos == (x, y):
                        obj = o
                        break
                if isinstance(obj, Number):
                    res += f'[{str(obj)}]'
                else:
                    res += '[ ]'
            res += '\n'
        res += '\n'
        return res


