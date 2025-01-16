#!/usr/bin/python3
"""
N Queens
"""

import sys


def backtrack(r, n):
    """
    Backtrack algorithm
    """
    res = []
    board = [["."] * n for i in range(n)]
    col = set()
    pos_diag = set()
    neg_diag = set()


    if r == n:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return

    for c in range(n):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue

        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        board[r][c] = "Q"

        backtrack(r + 1, n)

        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        board[r][c] = "."
    return (res)

def get_solutions(board):
    """
    Return the list of possibilities of the solved chessboard
    """

    solutions = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solutions.append([row, col])
                break
    return (solutions)


def nqueens(n):
    """
    place N non-attacking queens on an NxN chessboard
    """

    res = []
    solved_board = backtrack(0, res, n)
    print(res)
    print(solved_board)
    result = get_solutions(solved_board)

    print(solved_board)
    print(result)
    return (result)


# def init_board(n):
#     """
#     Initialize a chessboard or side n x n
#     """
#     board = [["."] * n for i in range(n)]
#     print(board)
#     return board


def main():
    """
    Execute code
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    n = int(sys.argv[1])
    nqueens(n)

if __name__ == "__main__":
    main()
