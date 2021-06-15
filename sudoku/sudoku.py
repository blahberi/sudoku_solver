class Sudoku:
    def __init__(self, board_strings):
        self.board = []
        self.board_strings = board_strings
        self.__build_board(board_strings)

    def __build_board(self, board_strings):
        for i in range(9):
            self.board.append([])
            for char in board_strings[i]:
                if char.isdigit():
                    self.board[i].append(int(char))
                else:
                    self.board[i].append(0)

    def __str__(self):
        res = ''
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                res += "- - - - - - - - - - - - \n"

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    res += " | "

                if j == 8:
                    res += str(self.board[i][j]) + '\n'
                else:
                    res += str(self.board[i][j]) + " "

        return res
