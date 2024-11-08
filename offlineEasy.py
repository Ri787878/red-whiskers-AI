import numpy as np
from collections import deque


# Example coordinates and values (x, y) -> value
#Variant 1
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

#Variant 2
coordinates2 = [
    ((6, 3), 1),
    ((0, 4), -1),
    ((8, 5), 1),
    ((1, 6), 1),
    ((1, 0), 1),
    ((4, 0), 1),
    ((2, 6), 1),
    ((8, 3), 1)
]

#Variant 3
coordinates3 = [
    ((6, 4), 1),
    ((0, 4), -1),
    ((4, 3), -1),
    ((0, 6), -1),
    ((6, 3), -1),
    ((7, 4), 1),
    ((4, 0), 1),
    ((2, 2), 1)
]

#Variant 4
coordinates4 = [
    ((3, 5), -1),
    ((7, 6), -1),
    ((4, 6), -1),
    ((2, 6), -1),
    ((5, 5), 1),
    ((5, 4), -1),
    ((2, 4), 1),
    ((0, 1), 1)
]

#Variant 5
coordinates5 = [
    ((6, 2), -1),
    ((0, 1), -1),
    ((9, 2), 1),
    ((2, 0), -1),
    ((2, 6), -1),
    ((4, 4), 1),
    ((7, 0), 1),
    ((9, 1), -1)
]

#Variant 6
coordinates6 = [
    ((7, 5), -1),
    ((9, 6), -1),
    ((1, 0), -1),
    ((5, 6), 1),
    ((0, 2), 1),
    ((8, 3), 1),
    ((8, 1), -1),
    ((3, 2), -1)
]
# Define the coordinates and their values

coordinates = coordinates1



def create_map_from_coordinates(coordinates, shape):
    # Initialize the matrix with zeros
    map_matrix = np.zeros(shape, dtype=int)

    # Fill the matrix based on the coordinates and their values
    for coord, value in coordinates:
        x, y = coord
        map_matrix[x, y] = value

    return map_matrix

#Bot's movement
#Check if the bot can move up
def checkUp():
    if bot[0] - 1 >= 0 and gameMap[bot[0] - 1][bot[1]] != -1:
        return True
    return False
#Check if the bot can move left
def checkLeft():
    if bot[1] - 1 >= 0 and gameMap[bot[0]][bot[1] - 1] != -1:
        return True
    return False
#Check if the bot can move right
def checkRight():
    if bot[1] + 1 < 7 and gameMap[bot[0]][bot[1] + 1] != -1:
        return True
    return False

#Frees the bot from a cone stuck position of 1 depth
def checkDown2Left():
    if bot[0] + 1 < 10 and bot[1] - 1 >= 0 and gameMap[bot[0] + 1][bot[1] - 1] != -1:
        return True
    return False
def checkDown2Right():
    if bot[0] + 1 < 10 and bot[1] + 1 < 7 and gameMap[bot[0] + 1][bot[1] + 1] != -1:
        return True
    return False

#Draws and updates map for debugging purposes
def updateMap(gameMap, bot, new_position):
    # Set the current bot position to 0 (aka Empty)
    current_x, current_y = bot
    gameMap[current_x][current_y] = 0

    # Update the bot's position
    new_x, new_y = new_position
    gameMap[new_x][new_y] = 1  # Set the new position of the bot to 1 (aka Occupied)

    # Update the bot's internal position variable
    bot[0] = new_x
    bot[1] = new_y

    #print(gameMap)

#Main movement function
def start():
    if checkUp():
        print("Moved Up")
        updateMap(gameMap, bot, (bot[0] - 1, bot[1]))
        moves.append("up")
        return

    if checkLeft():
        print("Moved Left")
        updateMap(gameMap, bot, (bot[0], bot[1] - 1))
        moves.append("left")
        return

    if checkRight():
        print("Moved Right")
        updateMap(gameMap, bot, (bot[0], bot[1] + 1))
        moves.append("right")
        return
    if checkDown2Left():
        print("Moved Down 2 Left")
        updateMap(gameMap, bot, (bot[0] + 1, bot[1] - 2))
        moves.append("down-2-left")
        return
    if checkDown2Right():
        print("Moved Down 2 Right")
        updateMap(gameMap, bot, (bot[0] + 1, bot[1] + 2))
        moves.append("down-2-right")
        return

# MEGA IMPORTANT  defines the shape of the map (needs to be fine tuned to the more complicated pathfinder AI's)
# Define the shape of the matrix (e.g., 10 rows(y) x7 columns(x) matrix)
shape = (10, 7)

# Create the map
gameMap = create_map_from_coordinates(coordinates, shape)

# Print the Starting matrix
print(gameMap)

bot = [9, 3]  # Bot's starting position

moves = deque()
counter = 0

while bot[0] != 0:
    start()


    if counter >= 20:
        break
    counter += 1
print(moves)
print(gameMap)




"""
gameMap = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
])
"""

