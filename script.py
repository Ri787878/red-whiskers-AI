import socketio
import json
import numpy as np
from collections import deque

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server.")
    sio.emit('PingTest', 'Hello from the Python client!')

#"Obstacles":[{"x":0, "y":0, "tipo":1},{"x":0, "y":10, "tipo":1}]}'
@sio.on('status')
def response(data):
    coordinates = tuple(data.items())
    print("Response from the server:", data)

# Connect to the Socket.IO server
#Change IP to connect while we dont have a domain
sio.connect("http://10.72.59.25:3000")


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

    print(gameMap)

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
        print("Moved Down Left")
        updateMap(gameMap, bot, (bot[0] + 1, bot[1] - 2))
        moves.append("down-2-left")
        return
    if checkDown2Right():
        print("Moved Down Right")
        updateMap(gameMap, bot, (bot[0] + 1, bot[1] + 2))
        moves.append("down-2-right")
        return

# MEGA IMPORTANT  defines the shape of the map (needs to be fine tuned to the more complicated pathfinder AI's)
# Define the shape of the matrix (e.g., 10 rows(y) x7 columns(x) matrix)
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

