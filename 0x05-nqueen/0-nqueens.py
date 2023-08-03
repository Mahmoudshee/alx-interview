#!/usr/bin/python3
"""
N queens problem solver
"""

import sys


def is_safe(board, row, col):
    for prev_row in range(row):
        if board[prev_row] == col or \
           board[prev_row] - prev_row == col - row or \
           board[prev_row] + prev_row == col + row:
            return False
    return True


def solve_nqueens(N):
    solutions = []

    def backtrack(row, board):
        if row == N:
            solutions.append([[row, col] for row, col in enumerate(board)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    backtrack(0, board)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
