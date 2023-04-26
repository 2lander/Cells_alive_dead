import random
import copy
import time

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
