"""
import socketio
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ipv4 = os.getenv('Ipv4')
port = os.getenv('Port')

# Initialize Socket.IO client
sio = socketio.Client()

# Define username variable
username = input("Enter your username: ")

# Connect to the server
sio.connect(f'http://{ipv4}:{port}')

# Handle the 'news' event from the server
@sio.on('news')
def on_news(data):
    print('Received news from server:', data)

# Handle the 'status' event from the server
@sio.on('status')
def on_status(data):
    print('Received news from server1:', data)

    if data.get('text') == "Todos os jogadores estão ready! O jogo vai começar!":
        a = 0
        while True:
            # Emit 'Ping' event to the server with specified data
            sio.emit('Ping', {'text': f'{{"Username":"{username}", "x":0, "y":0}}'})
            time.sleep(1)  # Wait for 1 second
            print(f"Ping {a}")
            a += 1

# Emit 'NewPlayer' event to the server
sio.emit('NewPlayer', {'text': f'{{"Username":"{username}"}}'})

# Keep the script running to maintain the connection
sio.wait()





#!/usr/bin/env python

import asyncio
from webs ockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()



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
import numpy as np
from collections import deque


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
