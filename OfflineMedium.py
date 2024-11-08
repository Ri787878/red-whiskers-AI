import numpy as np
from collections import deque
import time
import pygame
import random
import sys

#Start timer
start_time = time.time()


def create_map_from_coordinates(coordinates, shape):
    # Initialize the matrix with zeros
    map_matrix = np.zeros(shape, dtype=int)

    # Fill the matrix based on the coordinates and their values
    for coord, value in coordinates:
        x, y = coord
        map_matrix[x, y] = value

    return map_matrix


# Variables to receive start_pos and coordinates1
"""
# Define the game map
coordinates1 = [
    ((1, 3), -1),
    ((1, 4), -1),
    ((2, 0), -1),
    ((3, 1), -1),
    ((5, 2), -1),
    ((5, 5), -1),
    ((7, 3), -1),
    ((9, 3), 1),
]

coordinates1 = [
    ((1, 3), -1),
    ((2, 5), -1),
    ((3, 7), -1),
    ((4, 2), -1),
    ((5, 10), -1),
    ((6, 4), -1),
    ((7, 8), -1),
    ((8, 1), -1),
    ((9, 5), -1),
    ((10, 11), -1),
    ((11, 6), -1),
    ((12, 3), -1),
    ((13, 9), -1),
    ((14, 12), -1),
    ((15, 2), -1),
    ((16, 7), -1),
    ((18, 4), 1)   # Bot position
]
"""
coordinates1 = [
    ((5, 10), -1), ((12, 45), -1), ((20, 30), -1), ((25, 60), -1),
    ((33, 15), -1), ((40, 80), -1), ((45, 25), -1), ((52, 70), -1),
    ((55, 40), -1), ((60, 85), -1), ((65, 50), -1), ((70, 90), -1),
    ((75, 20), -1), ((80, 10), -1), ((85, 35), -1), ((90, 55), -1),
    ((95, 65), -1), ((22, 44), -1), ((28, 77), -1), ((34, 89), -1),
    ((38, 11), -1), ((42, 67), -1), ((49, 33), -1), ((53, 24), -1),
    ((57, 58), -1), ((63, 72), -1), ((69, 37), -1), ((76, 81), -1),
    ((83, 49), -1), ((88, 91), -1), ((13, 54), -1), ((19, 17), -1),
    ((27, 82), -1), ((31, 64), -1), ((35, 21), -1), ((47, 36), -1),
    ((59, 74), -1), ((61, 47), -1), ((78, 18), -1), ((96, 22), -1),
]

#IMPORTANT  Game Information
# Creates the game map
shape = (100, 100)
gameMap = create_map_from_coordinates(coordinates1, shape)
start_pos = (99, 50)

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 100, 100
CELL_SIZE = WIDTH // COLS
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BFS Pathfinding")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Grid initialization
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
obstacles = 40  # Number of obstacles

# Define obstacles and bot/target positions
def place_obstacles():
    for _ in range(obstacles):
        x, y = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
        grid[x][y] = -1  # -1 represents an obstacle

def draw_grid():
    SCREEN.fill(WHITE)
    for x in range(ROWS):
        for y in range(COLS):
            color = WHITE
            if grid[x][y] == -1:  # Obstacle
                color = BLACK
            elif grid[x][y] == 1:  # Bot
                color = GREEN
            elif grid[x][y] == 2:  # Target
                color = RED
            elif grid[x][y] == 3:  # Visited
                color = BLUE
            pygame.draw.rect(SCREEN, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))




#Prints Starting Map
#print(gameMap)


# Define the directions and their corresponding moves
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Find the bot's starting position (position with '1')
#Will be replaced when connected to the magic wonder world that is WebSockets


# BFS to find the shortest path to the top row
queue = deque([(start_pos, [])])  # (position, path)
visited = set()
visited.add(start_pos)

while queue:
    (x, y), path = queue.popleft()

    # Check if we've reached the top row
    if x == 0:
        for px, py in path:
            	#testing can and need to be removed
                grid[px][py] = 3  # Mark path as visited
                draw_grid()
                pygame.display.flip()
                pygame.time.delay(10)
                #Stops useless visualization code
        print("Path to top row:", path)
        break

    # Explore all possible moves
    for move_name, (dx, dy) in moves.items():
        nx, ny = x + dx, y + dy

        # Check boundaries and obstacles
        if 0 <= nx < gameMap.shape[0] and 0 <= ny < gameMap.shape[1]:
            if gameMap[nx, ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [move_name]))
                #testing can and need to be removed
                grid[nx][ny] = 3  # Mark as visited
                draw_grid()
                pygame.display.flip()
                pygame.time.delay(1)  # Slow down for visualization
                #Stops useless visualization code

# Solved Map
#print(gameMap)


# Variable to send: path



#time to run
print("--- %s seconds ---" % (time.time() - start_time))

