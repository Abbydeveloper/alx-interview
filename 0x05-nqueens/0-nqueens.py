#!/usr/bin/python3
"""
N Queens
"""

import sys


def nqueens(n):
    """
    place N non-attacking queens on an NxN chessboard
    """

    col = set()
    pos_diag = set()
    neg_diag = set()

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        """
        Backtrack algorithm
        """

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

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return (res)


def get_solutions(board):
    """
    Return the list of possibilities of the solved chessboard
    """

    solutions = []

    for row in range(len(board)):
        solutions.append([])

        for col in range(len(board[row])):
            sol = [c for c in board[row][col]]

            for c in range(len(sol)):
                if sol[c] == "Q":
                    solutions[row].append([col, c])
                    break
    return (solutions)


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
    board = nqueens(n)
    solutions = get_solutions(board)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
