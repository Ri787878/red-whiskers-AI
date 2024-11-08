import socketio
import json
import numpy as np
from collections import deque

# Establish a standard Socket.IO client
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server.")
    sio.emit('PingTest', 'Hello from the Python client!')

#"Obstaculos":[{"x":0, "y":0, "tipo":1},{"x":0, "y":10, "tipo":1}]}'
@sio.on('status')
def response(data):
    coordinates = tuple(data.items())
    print("Response from the server:", data)

# Connect to the Socket.IO server
sio.connect("http://10.72.59.25:3000")

# Keep the client running
try:
    sio.wait()
except KeyboardInterrupt:
    print("Disconnecting...")
    sio.disconnect()






def create_map_from_coordinates(coordinates, shape):
    # Initialize the matrix with zeros
    map_matrix = np.zeros(shape, dtype=int)

    # Fill the matrix based on the coordinates and their values
    for coord, value in coordinates:
        x, y = coord
        map_matrix[x, y] = value

    return map_matrix


def checkUp():
    if bot[0] - 1 >= 0 and gameMap[bot[0] - 1][bot[1]] != -1:
        return True
    return False
def checkLeft():
    if bot[1] - 1 >= 0 and gameMap[bot[0]][bot[1] - 1] != -1:
        return True
    return False
def checkRight():
    if bot[1] + 1 < 7 and gameMap[bot[0]][bot[1] + 1] != -1:
        return True
    return False
def checkDown2Left():
    if bot[0] + 1 < 10 and bot[1] - 1 >= 0 and gameMap[bot[0] + 1][bot[1] - 1] != -1:
        return True
    return False
def checkDown2Right():
    if bot[0] + 1 < 10 and bot[1] + 1 < 7 and gameMap[bot[0] + 1][bot[1] + 1] != -1:
        return True
    return False


def updateMap(gameMap, bot, new_position):
    # Set the current bot position to 0 (empty space)
    current_x, current_y = bot
    gameMap[current_x][current_y] = 0

    # Update the bot's position
    new_x, new_y = new_position
    gameMap[new_x][new_y] = 1  # Set the new position to 1 (bot's position)

    # Update the bot's internal position variable
    bot[0] = new_x
    bot[1] = new_y  # Update bot's coordinates

    # Print updated map for visual checking
    print(gameMap)

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
        print("Moved Down Left")
        updateMap(gameMap, bot, (bot[0] + 1, bot[1] - 2))
        moves.append("down-2-left")
        return
    if checkDown2Right():
        print("Moved Down Right")
        updateMap(gameMap, bot, (bot[0] + 1, bot[1] + 2))
        moves.append("down-2-right")
        return


# Define the shape of the matrix (e.g., 10x7 matrix)
shape = (10, 7)

# Create the map
gameMap = create_map_from_coordinates(coordinates, shape)

# Print the resulting matrix
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

"""
# Example coordinates and values (x, y) -> value
coordinates = [
    ((1, 3), -1),  # At position (1, 3) place -1
    ((1, 4), -1),  # At position (1, 4) place -1
    ((2, 0), -1),
    ((3, 1), -1),  # At position (3, 1) place -1
    ((5, 2), -1),
    ((5, 5), -1),  # At position (5, 5) place -1
    ((7, 3), -1),  # At position (7, 3) place -1
    ((9, 3), 1),   # At position (9, 3) place 1
]

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

