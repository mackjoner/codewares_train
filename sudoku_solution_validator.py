"""
    Sudoku Solution Validator
    https://www.codewars.com/kata/sudoku-solution-validator/python
"""


def validSolution(board):
    check = range(1, 10)

    def check_one_to_nine(lst):
        return set(lst) == set(check)

    for row in board:
        if not check_one_to_nine(row):
            return False

    for column in zip(*board):
        if not check_one_to_nine(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            if not check_one_to_nine(nums):
                return False

    return True


# Clever Solution
def validSolution_(board):
    blocks = [[board[x + a][y + b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return all(set(r) == set(range(1, 10)) for r in board + zip(*board) + blocks)


if __name__ == '__main__':
    valid_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    invalid_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 0, 3, 4, 8],
                     [1, 0, 0, 3, 4, 2, 5, 6, 0],
                     [8, 5, 9, 7, 6, 1, 0, 2, 0],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 0, 1, 5, 3, 7, 2, 1, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 0, 0, 4, 8, 1, 1, 7, 9]]

    print(validSolution(valid_board))
    print(validSolution(invalid_board))
    print(validSolution_(valid_board))
    print(validSolution_(invalid_board))
