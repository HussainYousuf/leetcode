import pygame
import sys


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


def draw_board(queens_list):
    for queens in queens_list:
        for row, col in queens:
            pygame.draw.circle(
                screen,
                (255, 0, 0),
                (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2),
                cell_size // 2 - 5,
            )


# Rest des Codes bleibt unverändert ...

# Pygame-Initialisierung
pygame.init()

n = 8
cell_size = 60
width, height = n * cell_size, n * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("N-Queens Problem")

solutions = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    if not solutions:
        queens = []
        solve_n_queens(n, queens, 0)

    solutions.append(queens.copy())

    draw_board(solutions)

    pygame.display.flip()

pygame.quit()
sys.exit()
