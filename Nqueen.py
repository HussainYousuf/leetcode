def genSolutions(n, board=None):
    # workaround, see https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    board = board or [[False] * n for _ in range(n)]

    queens = 0

    for i in range(n):
        for j in range(n):
            if checkPosition(board, i, j):
                genSolutions(n, board)
                board[i][j] = (i, j)
                genSolutions(n, board)
                queens += 1

    if queens == n:
        return board


def checkPosition(board, row, col):
    for i in range(len(board)):
        if board[row][i]:
            return False
        if board[i][col]:
            return False

    i = row
    j = 0
    while i < len(board):
        if col + j < len(board) and board[i][col + j]:
            return False
        if col - j < len(board) and board[i][col - j]:
            return False
        i += 1
        j += 1

    i = row
    j = 0
    while i >= 0:
        if col + j < len(board) and board[i][col + j]:
            return False
        if col - j < len(board) and board[i][col - j]:
            return False
        i -= 1
        j += 1

    return True


def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


for solution in queens(5, 0, [], [], []):
    print(solution)


import pygame
import sys


# Funktion zum Zeichnen des Schachbretts und der Königinnen
def draw_board(queens):
    for row in range(n):
        for col in range(n):
            color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(
                screen, color, (col * cell_size, row * cell_size, cell_size, cell_size)
            )
            if (row, col) in queens:
                pygame.draw.circle(
                    screen,
                    (255, 0, 0),
                    (
                        col * cell_size + cell_size // 2,
                        row * cell_size + cell_size // 2,
                    ),
                    cell_size // 2 - 5,
                )


# Funktion zum Lösen des N-Queens-Problems (Backtracking)
def solve_n_queens(n, queens, row):
    if row == n:
        return True

    for col in range(n):
        if all(
            row != r and col != c and abs(row - r) != abs(col - c) for r, c in queens
        ):
            queens.append((row, col))
            if solve_n_queens(n, queens, row + 1):
                return True
            queens.pop()

    return False


# Pygame-Initialisierung
pygame.init()

# Brettgröße und Zellengröße
n = 8
cell_size = 60

# Fenstergröße berechnen
width, height = n * cell_size, n * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("N-Queens Problem")

queens = []

# Hauptprogrammschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    draw_board(queens)
    draw_board(queens)
    pygame.display.flip()

    if len(queens) < n:
        if not solve_n_queens(n, queens, 0):
            print("Keine Lösung gefunden.")
            running = False

pygame.quit()
sys.exit()

# genSolutions(8)
