#import src.models.botsPathfinding as BP
from models.easyBot import easyBot
from models.mediumBot import mediumBot
from models.hardBot import hardBot
import models.utilities as ut
import socketio
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
sio.connect("http://10.72.98.20:3000")


#Changeable Map Size
ROWS = 100
COLS = 70

while True:
	#Start Position
	#Change to get position from server message
	startPos = [ROWS - 1, 54]
	#same
	choice = ut.chooseBot()
	#Change so coordinates are received from server

	if choice == '1':
		coordinates = ut.chooseCoordinates()
		jsonMoves = easyBot()
		sio.emit('PingTest', jsonMoves)
	elif choice == '2':
		coordinates = ut.chooseCoordinates()
		jsonMoves = mediumBot(ROWS, COLS, startPos, coordinates)
		sio.emit('PingTest', jsonMoves)
	elif choice == '3':
		coordinates = ut.chooseCoordinates()
		jsonMoves =hardBot(ROWS, COLS, startPos, coordinates)
		sio.emit('PingTest', jsonMoves)
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue




try:
	sio.wait()
except KeyboardInterrupt:
	print("Disconnecting...")
	sio.disconnect()
