import pygame
import sys
import random
import math

# Constants
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 50, 50
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Create grid and cellBlocked matrix
grid = [[{'x': row, 'y': col, 'is_blocked': False, 'is_visited': False, 'distance': float('inf'), 'previous': None}
         for col in range(COLS)] for row in range(ROWS)]

# Function to randomly add blocks
def add_random_blocks(probability):
    for row in range(ROWS):
        for col in range(COLS):
            if random.random() < probability:
                grid[row][col]['is_blocked'] = True

add_random_blocks(0.15)

def display_multiline_text(window, text, position, font_size=21, color=BLACK):
    font = pygame.font.Font(None, font_size)
    lines = text.split("|")
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        window.blit(text_surface, (position[0], position[1] + y_offset))
        y_offset += font_size

def draw_grid():
    window.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]['is_blocked']:
                pygame.draw.rect(window, RED, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
            else:
                pygame.draw.rect(window, GREY, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 1)
            
            if grid[row][col]['is_visited']:
                pygame.draw.rect(window, YELLOW, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 1)

def draw_cell(x, y, color=(0, 255, 22)):
    pygame.draw.rect(window, color, (y * CELL_WIDTH, x * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

def calculate_heuristic(x, y, end):
    return math.sqrt((x - end[0]) ** 2 + (y - end[1]) ** 2)

def update_neighbor_distance(x, y, index_distance, end):
    grid[x][y]['is_visited'] = True 
    if x > 0 and not grid[x - 1][y]['is_blocked'] and not grid[x - 1][y]['is_visited']:
        if index_distance + 1 < grid[x - 1][y]['distance']:
            grid[x - 1][y]['distance'] = index_distance + 1
            grid[x - 1][y]['previous'] = (x, y)
    if x < ROWS - 1 and not grid[x + 1][y]['is_blocked'] and not grid[x + 1][y]['is_visited']:
        if index_distance + 1 < grid[x + 1][y]['distance']:
            grid[x + 1][y]['distance'] = index_distance + 1
            grid[x + 1][y]['previous'] = (x, y)
    if y > 0 and not grid[x][y - 1]['is_blocked'] and not grid[x][y - 1]['is_visited']:
        if index_distance + 1 < grid[x][y - 1]['distance']:
            grid[x][y - 1]['distance'] = index_distance + 1
            grid[x][y - 1]['previous'] = (x, y)
    if y < COLS - 1 and not grid[x][y + 1]['is_blocked'] and not grid[x][y + 1]['is_visited']:
        if index_distance + 1 < grid[x][y + 1]['distance']:
            grid[x][y + 1]['distance'] = index_distance + 1
            grid[x][y + 1]['previous'] = (x, y)

def backline(last):
    if grid[last[0]][last[1]]['is_visited']:
        path = []
        current = last
        while current:
            path.append(current)
            current = grid[current[0]][current[1]]['previous']
        for node in path:
            draw_cell(node[0], node[1], color=(0, 255, 0))
        pygame.display.update()

# Pygame setup
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Algorithm Visualization")

running = True

start = [0, 0]
grid[0][0]['distance'] = 0
end = [ROWS - 1, COLS - 1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    min_distance = float('inf')
    min_node = None

    for row in range(ROWS):
        for col in range(COLS):
            if not grid[row][col]['is_visited'] and grid[row][col]['distance'] < min_distance:
                min_distance = grid[row][col]['distance']
                min_node = (row, col)
    
    if min_node:
        index = min_node
        update_neighbor_distance(index[0], index[1], grid[index[0]][index[1]]['distance'], end)
        backline(min_node)
    
    draw_grid()
    draw_cell(start[0], start[1])
    draw_cell(end[0], end[1])
    backline((end[0], end[1]))
    pygame.display.update()
