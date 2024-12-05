import noDisplay
import testCases
import socketio
import pandas as pd
import time
import json
sio = socketio.Client()


def convertNative(obstaculos):
    native_format = []

    for obstacle in obstaculos:
        # Extract coordinates and ignore the 'tipo' field as per the native format
        x, y = obstacle[0], obstacle[1]
        native_format.append(((x, y), -1))

    return native_format


#create function to identify dificulty  in username of bots
@sio.event
def connect():
    sio.emit('TestObject')
    print("Connected to the server.")

#"Obstacles":[{"x":0, "y":0, "tipo":1},{"x":0, "y":10, "tipo":1}]}'
@sio.on('status')
def handle_bot(data):
    startPos = [ROWS - 1, 54]

    json_data = json.loads(data)
    obstacles = json_data['data'][0]['Obstaculos']
    print(json_data)
    coordinates = []
    for obstacle in obstacles:
        # Append the tuple ((x, y), type)
        coordinates.append(((obstacle['x'], obstacle['y']), obstacle['tipo']))

    coordinates = coordinates[:-2]
    print(type(coordinates[0][0]))
    print(coordinates)

    botDificulty = json_data['data'][0]["UserBot"]


    if botDificulty == 'BotE1':
        noDisplay.startEasyBot(ROWS, COLS, startPos, coordinates)
        sio.emit('TestJson', jsonMoves)
    elif botDificulty == 'BotM1':
        jsonMoves = noDisplay.startMediumBot(ROWS, COLS, startPos, coordinates)
        sio.emit('TestJason', jsonMoves)
    elif botDificulty == 'Bot1H':
        print("Hard Bot")
        print("UNDER CONSTRUCTION")
    else:
        print("Invalid Choice")


def response(data):
    coordinates = tuple(data.items())
    print("Response from the server:", data)



# Connect to the Socket.IO server
#Change IP to connect while we dont have a domain
sio.connect("http://172.20.10.2:3000")

#Changeable Map Size
ROWS = 70
COLS = 100

sio.on('bot1', handle_bot)



try:
    sio.wait()
except KeyboardInterrupt:
    print("Disconnecting...")
    sio.disconnect()


"""if choice == '1':
		coordinates = noDisplay.chooseCoordinates()
		noDisplay.startEasyBot(ROWS, COLS, startPos, coordinates)
	elif choice == '2':
		coordinates = noDisplay.chooseCoordinates()
		jsonMoves =noDisplay.startMediumBot(ROWS, COLS, startPos, coordinates)
		sio.emit('PingTest', jsonMoves)
	elif choice == '3':
		print("Hard Bot")
		print("UNDER CONSTRUCTION")
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue
"""
