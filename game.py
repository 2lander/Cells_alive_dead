import random
import copy
import time
import pygame

def create_board(n, p):
    """
    Можна самостійно вибрати розмір поля.
    """
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if random.random() < p:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    return board

def get_neighbors(board, i, j):
    """
    К-сть живих сусідів.
    """
    neighbors = 0
    for x in range(max(0, i-1), min(len(board), i+2)):
        for y in range(max(0, j-1), min(len(board), j+2)):
            if x == i and y == j:
                continue
            if board[x][y] == 1:
                neighbors += 1
    return neighbors

def next_generation(board):
    """
    Наступний стан.
    """
    new_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board)):
            neighbors = get_neighbors(board, i, j)
            if board[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[i][j] = 0
            else:
                if neighbors == 3:
                    new_board[i][j] = 1
    return new_board

def print_board(board):
    """
    Вивести на екран
    """
    for row in board:
        print(' '.join(map(str, row)))

def save_board(board, filename):
    """
    Зберегти.
    """
    with open(filename, 'w') as f:
        for row in board:
            f.write(' '.join(map(str, row)) + '\n')

n = int(input("Введіть розмір поля(50=50*50): "))
p = float(input("Введіть число від 0 до 1 (можна дробове)): "))

board = create_board(n, p)

print("Поле:")
print_board(board)

num_generations = int(input("Введіть кількість поколінь: "))
for i in range(num_generations):
    print("Покоління", i+1)
    board = next_generation(board)
    print_board(board)
    filename = "generation_" + str(i+1) + ".txt"
    save_board(board, filename)
    time.sleep(1)  # щоб краще побачити зміни

# Pygame
pygame.init()

#розмір вікна
win_width = 500
win_height = 500
white = (255, 255, 255)
black = (0, 0, 0)

#створення вікна
window = pygame.display.set_mode((win_width, win_height))

#назва вікна
pygame.display.set_caption("Гра «Життя»")

#клітинки
cell_size = 10
cell_width = win_width // cell_size
cell_height = win_height // cell_size
cells = [[random.randint(0, 1) for y in range(cell_height)] for x in range(cell_width)]

#анімація
clock = pygame.time.Clock()

#головний цикл програми
while True:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #обновлення клітинок
    new_cells = [[0 for y in range(cell_height)] for x in range(cell_width)]
    for x in range(cell_width):
        for y in range(cell_height):
            neighbors = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    elif x + dx < 0 or x + dx >= cell_width or y + dy < 0 or y + dy >= cell_height:
                        continue
                    elif cells[x + dx][y + dy] == 1:
                        neighbors += 1
            if cells[x][y] == 1 and (neighbors == 2 or neighbors == 3):
                new_cells[x][y] = 1
            elif cells[x][y] == 0 and neighbors == 3:
                new_cells[x][y] = 1
    cells = new_cells

    # відображення клітинок на екрані
    window.fill(white)
    for x in range(cell_width):
        for y in range(cell_height):
            if cells[x][y] == 1:
                pygame.draw.rect(window, black, (x * cell_size, y * cell_size, cell_size, cell_size))
    pygame.display.update()

    # обмеження кадрів на секунду
    clock.tick(5)