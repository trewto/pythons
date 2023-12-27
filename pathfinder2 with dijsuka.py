import pygame
import sys
import random
# Constants
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 50,50
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (255,0,0)
YELLOW= (255,255,0)
# Create grid and cellBlocked matrix
grid = [[{'x': row, 'y': col, 'is_blocked': False, 'is_visited': False, 'distance': float('inf') , 'previous' : None}
         for col in range(COLS)] for row in range(ROWS)]


#cellBlocked = [[False for _ in range(COLS)] for _ in range(ROWS)]  # Initialize all cells as unblocked
grid[2][3]['is_blocked'] = True
grid[2][2]['is_blocked'] = True
grid[2][1]['is_blocked'] = True
grid[4][0]['is_blocked'] = True
grid[4][1]['is_blocked'] = True
grid[4][2]['is_blocked'] = True
grid[2][4]['is_blocked'] = True
def display_multiline_text(window, text, position, font_size=21, color=BLACK):
    font = pygame.font.Font(None, font_size)
    lines = text.split("|")  # Split text into lines based on a separator character "|"

    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        window.blit(text_surface, (position[0], position[1] + y_offset))
        y_offset += font_size  # Adjust the Y offset for each line

print(grid)
# Pygame setup
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")

# Font setup
font = pygame.font.SysFont(None, 20)
def add_random_blocks(probability):
    for row in range(ROWS):
        for col in range(COLS):
            if random.random() < probability:  # Using probability to randomly block cells
                grid[row][col]['is_blocked'] = True
add_random_blocks(0.15)
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

            cell_info = f'({grid[row][col]["x"]}, {grid[row][col]["y"]}) | V: {grid[row][col]["is_visited"]} | D: {grid[row][col]["distance"]}'
            #display_multiline_text(window, cell_info, (col * CELL_WIDTH + 5, row * CELL_HEIGHT + 5))  # Adjust position for better alignment
   
    #pygame.display.update()

def draw_cell(x,y,color=(0,255,22)):
    pygame.draw.rect(window, color, (y * CELL_WIDTH, x * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

running = True

start = [0,0]
grid[0][0]['distance']=0
end = [ROWS-1,COLS-1]

index = start

def update_neghibour_distance(x,y,index_distance):

    grid[x][y]['is_visited'] = True 
    if x > 0 and not grid[x - 1][y]['is_blocked'] and not grid[x - 1][y]['is_visited']:
        if index_distance + 1 <grid[x - 1][y]['distance']:
            grid[x - 1][y]['distance'] =index_distance + 1 
            grid[x - 1][y]['previous'] = (x,y)
    if x < ROWS - 1 and not grid[x + 1][y]['is_blocked'] and not grid[x + 1][y]['is_visited']:
        if index_distance + 1 <grid[x + 1][y]['distance']:
            grid[x + 1][y]['distance'] =index_distance + 1 
            grid[x + 1][y]['previous'] = (x,y)
    if y > 0 and not grid[x][y - 1]['is_blocked'] and not grid[x][y - 1]['is_visited']:
         if index_distance + 1 < grid[x][y - 1]['distance']:
            grid[x][y - 1]['distance']  =index_distance + 1 
            grid[x][y - 1]['previous'] = (x,y)
    if y < COLS - 1 and not grid[x][y + 1]['is_blocked'] and not grid[x][y + 1]['is_visited']:
         if index_distance + 1 <grid[x][y + 1]['distance']:
            grid[x][y + 1]['distance'] =index_distance + 1 
            grid[x][y + 1]['previous'] = (x,y)

# Your existing code...
def backline(last):
    if grid[last[0]][last[1]]['is_visited']:
        path = []
        current = last
        while current:
            path.append(current)
            current = grid[current[0]][current[1]]['previous']

        # Drawing the shortest path
        for node in path:
            draw_cell(node[0], node[1], color=(0, 255, 0))  # Green color for the shortest path
        pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    min_distance = float('inf')
    min_node = None

    # Finding the unvisited node with the minimum distance
    for row in range(ROWS):
        for col in range(COLS):
            if not grid[row][col]['is_visited'] and grid[row][col]['distance'] < min_distance:
                min_distance = grid[row][col]['distance']
                min_node = (row, col)
                

    if min_node:
        index = min_node
        update_neghibour_distance(index[0],index[1],grid[index[0]][index[1]]['distance'])
        backline(min_node)
    draw_grid()
    draw_cell(start[0], start[1])
    draw_cell(end[0], end[1])
    backline((end[0],end[1]))
    pygame.display.update()
    