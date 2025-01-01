# Import necessary libraries
from collections import deque
import utilities as ut
import testCases
import numpy as np
import time
import json

# Define moves and directions
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


#Updates map
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


def start(gameMap, botPosition, moves):
    if checkUp(botPosition, gameMap):
        updateMap(gameMap, botPosition, (botPosition[0] - 1, botPosition[1]))
        moves.append("up")
        return moves

    if checkLeft(botPosition, gameMap):
        updateMap(gameMap, botPosition, (botPosition[0], botPosition[1] - 1))
        moves.append("left")
        return moves

    if checkRight(botPosition, gameMap):
        updateMap(gameMap, botPosition, (botPosition[0], botPosition[1] + 1))
        moves.append("right")
        return moves
    if checkDown2Left(botPosition, gameMap):
        updateMap(gameMap, botPosition, (botPosition[0] + 1, botPosition[1] - 2))
        moves.append("down-2-left")
        return moves
    if checkDown2Right(botPosition, gameMap):
        updateMap(gameMap, botPosition, (botPosition[0] + 1, botPosition[1] + 2))
        moves.append("down-2-right")
        return moves

# Easy Bot

def startEasyBot(ROWS, COLS, start_pos, coordinates):
	print("Easy Bot")
	#startTime = time.time()
	startTime = time.time()
	jsonPath = easyBot(ROWS, COLS, start_pos, coordinates)
	print("jsonPath = ", jsonPath)
	print("Time taken: ", time.time() - startTime)


def easyBot(ROWS, COLS, start_pos,coordinates):
    gameMap = ut.create_map_from_coordinates(coordinates, ROWS, COLS)
    moves = deque()
    while start_pos[1] != 0:
        moves = start(gameMap, start_pos, moves)

    return json.dumps(list(moves))



# Medium Bot

def startMediumBot(ROWS, COLS, start_pos, coordinates):
	print("Medium Bot")
	startTime = time.time()
	jsonPath = mediumBot(ROWS, COLS, tuple(start_pos), coordinates)
	print("jsonPath = ", jsonPath)
	print("Time taken: ", time.time() - startTime)
	return jsonPath

def mediumBot(ROWS, COLS, start_pos,coordinates):
    gameMap = ut.create_map_from_coordinates(coordinates, ROWS, COLS)

    bfs_path = []
    visited = set()
    queuedPositions = deque([(start_pos, [])])  # (position, path)
    visited.add(start_pos)

    while queuedPositions:
        (x, y), path = queuedPositions.popleft()
        # Check if reached the top row
        if x == 0:
            bfs_path = path  # store final path
            break

        # Explore neighbors
        for move_name, (dx, dy) in moves.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and gameMap[nx, ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queuedPositions.append(((nx, ny), path + [move_name]))  # Store the coordinate in the path

    # Convert path to JSON
    path_json = json.dumps(list(bfs_path))

    return path_json
