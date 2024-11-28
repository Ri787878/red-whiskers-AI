# Import necessary libraries
from collections import deque
import testCases
import json
import numpy as np
import time
import pygame
import sys

startTime = time.time()


# Initialize Pygame and screen
def initPygame(ROWS, COLS, CELL_SIZE, string):
	pygame.init()
	WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(string)
	return SCREEN



# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (192, 192, 192)
DARK_GREY = (169, 169, 169)

# Define moves and directions
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Function to create map from coordinates
def create_map_from_coordinates(coordinates, shape):
    map_matrix = np.zeros(shape, dtype=int)
    for coord, value in coordinates:
        x, y = coord
        map_matrix[x, y] = value
    return map_matrix



def draw_grid(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, path=None, visited=None):
    route = []
    SCREEN.fill(DARK_GREY)  # Background color for the grid
    for x in range(ROWS):
        for y in range(COLS):
            # Default color for cells
            color = GREY
            if gameMap[x, y] == -1:
                color = RED  # Obstacles
            elif visited and (x, y) in visited:
                color = BLUE  # Visited cells
            elif path and (x, y) in path:
                color = GREEN  # Final path chosen

            # Draw the cell with slight padding for visible grid lines
            pygame.draw.rect(SCREEN, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
    pygame.display.update()  # Refresh the screen with all drawn cells

def draw_path(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, path):
    for (px, py) in path:
        draw_grid(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, path=path)
        pygame.display.flip()

# Define normalized moves for final path visualization
normmoves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

###EASY BOT
def startEasyBot(ROWS, COLS, CELL_SIZE, start_pos, coordinates):
	print("Easy Bot")
	start_time = time.time()
	easyBot(ROWS, COLS, CELL_SIZE, start_pos, coordinates)
	print("Time taken: ", time.time() - start_time)

def easyBot(ROWS, COLS, CELL_SIZE, start_pos, coordinates):
	SCREEN = initPygame(ROWS, COLS, CELL_SIZE, "Easy Difficulty Bot Pathfinding")

	# Create the map
	gameMap = create_map_from_coordinates(coordinates, (ROWS, COLS))

	moves = deque()
	visited = set()
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				return

		if start_pos[0] >= 0 :
			moves = start(gameMap, start_pos, moves)
			visited.add(tuple(start_pos))
			# Update start_pos after each move
			direction = moves[-1]  # Last move made
			if direction == "up":
				start_pos[0] -= 1
			elif direction == "down":
				start_pos[0] += 1
			elif direction == "left":
				start_pos[1] -= 1
			elif direction == "right":
				start_pos[1] += 1
			# Draw grid and visualize bot's path
			draw_grid(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, visited, tuple(start_pos))
			pygame.display.flip()
			pygame.time.delay(100)  # Add a slight delay for visualization

		if start_pos[0] == 0:
			running = False

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()
	return moves

def updateMap(gameMap, botPosition, new_position):
    # Set the current bot position to 0 (aka Empty)
    current_x, current_y = botPosition
    gameMap[current_x][current_y] = 0

    # Update the bot's position
    new_x, new_y = new_position
    gameMap[new_x][new_y] = 1  # Set the new position of the bot to 1 (aka Occupied)

    # Update the bot's internal position variable
    botPosition[0] = new_x
    botPosition[1] = new_y
    return

##Bot's movement
#Check if the bot can move up
def checkUp(botPosition, gameMap):
    if botPosition[0] - 1 >= 0 and gameMap[botPosition[0] - 1][botPosition[1]] != -1:
        return True
    return False
#Check if the bot can move left
def checkLeft(botPosition, gameMap):
    if botPosition[1] - 1 >= 0 and gameMap[botPosition[0]][botPosition[1] - 1] != -1:
        return True
    return False
#Check if the bot can move right
def checkRight(botPosition, gameMap):
    if botPosition[1] + 1 < 7 and gameMap[botPosition[0]][botPosition[1] + 1] != -1:
        return True
    return False
#Frees the bot from a cone stuck position of 1 depth
def checkDown2Left(botPosition, gameMap):
    if botPosition[0] + 1 < 10 and botPosition[1] - 1 >= 0 and gameMap[botPosition[0] + 1][botPosition[1] - 1] != -1:
        return True
    return False
def checkDown2Right(botPosition, gameMap):
    if botPosition[0] + 1 < 10 and botPosition[1] + 1 < 7 and gameMap[botPosition[0] + 1][botPosition[1] + 1] != -1:
        return True
    return False

def start(gameMap, start_pos, moves):
    # Define possible moves and corresponding check functions
    moveSet = {
        "up": (-1, 0, checkUp),
        "left": (0, -1, checkLeft),
        "right": (0, 1, checkRight),
        "down2left": (1, -1, checkDown2Left),
        "down2right": (1, 1, checkDown2Right),
    }

    # Determine next move
    for move_name, (dx, dy, check_func) in moveSet.items():
        if check_func(start_pos, gameMap):  # Use the corresponding check function
            nx, ny = start_pos[0] + dx, start_pos[1] + dy
            if 0 <= nx < len(gameMap) and 0 <= ny < len(gameMap[0]) and gameMap[nx][ny] == 0:
                moves.append(move_name)
                return moves

    return moves


###MEDIUM BOT
def startMediumBot(ROWS, COLS, CELL_SIZE, startPos, coordinates):
	print("Medium Bot")
	startTime = time.time()
	jsonPath = mediumBot(ROWS, COLS, CELL_SIZE, startPos, coordinates)
	print("Time taken: ", time.time() - startTime)


	# Keep window open until user closes it
	running = True
	while running:
		elapsed_time = time.time() - startTime

		"""
		# Check if 45 seconds have passed
		if elapsed_time > 45:
			print("45 seconds elapsed. Exiting...")
			running = False
			pygame.quit()
			sys.exit()
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()

def mediumBot(ROWS, COLS, CELL_SIZE, startPos, coordinates):
	SCREEN = initPygame(ROWS, COLS, CELL_SIZE, "Medium Difficulty Bot Pathfinding")
	gameMap = create_map_from_coordinates(coordinates, (ROWS, COLS))
	bfs_path = []
	visited = set()
	queuedPositions = deque([(startPos, [])])  # Start with (position, path of coordinates)
	visited.add(startPos)

	while queuedPositions:
		(x, y), path = queuedPositions.popleft()

		# Draw the current state with the visited cells
		draw_grid(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, path=path, visited=visited)

		# Update the display
		pygame.display.flip()

		# Check if reached the top row
		if x == 0:
			bfs_path = path  # store final path of coordinates
			break

		# Explore neighbors
		for move_name, (dx, dy) in moves.items():
			nx, ny = x + dx, y + dy
			if 0 <= nx < ROWS and 0 <= ny < COLS and gameMap[nx, ny] == 0 and (nx, ny) not in visited:
				visited.add((nx, ny))
				queuedPositions.append(((nx, ny), path + [(nx, ny)]))  # Append the coordinate to path

	draw_path(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, bfs_path)
	return bfs_path

def chooseCoordinates():
	print("Choose what Test Case you want to use")
	print("1. coordinatesTest_1")
	print("2. coordinatesTest_2")
	print("3. coordinatesTest_3")
	print("4. coordinatesTest_4")
	coordinates = input("Enter your choice: ")

	if coordinates == '1':
		return testCases.coordinatesTest_1
	elif coordinates == '2':
		return testCases.coordinatesTest_2
	elif coordinates == '3':
		return testCases.coordinatesTest_3
	elif coordinates == '4':
		return testCases.coordinatesTest_4
	else:
		return None

def chooseBot():
	print("What is the Bot you want to test?")
	print("1. Easy Bot")
	print("2. Medium Bot")
	print("3. Hard Bot (UNDER CONSTRUCTION)")
	print("4. Show Test Cases")
	print("c. Close Program")
	return input("Enter your choice: ")

def showStartingMap(ROWS, COLS, CELL_SIZE, startPos, coordinates):
	if coordinates == testCases.coordinatesTest_1:
		title = "Test Case 1"
	elif coordinates == testCases.coordinatesTest_2:
		title = "Test Case 2"
	elif coordinates == testCases.coordinatesTest_3:
		title = "Test Case 3"
	elif coordinates == testCases.coordinatesTest_4:
		title = "Test Case 4"
	SCREEN = initPygame(ROWS, COLS, CELL_SIZE, title)
	gameMap = create_map_from_coordinates(coordinates, (ROWS, COLS))
	draw_grid(SCREEN, gameMap, ROWS, COLS, CELL_SIZE, visited=None, path=None)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()
