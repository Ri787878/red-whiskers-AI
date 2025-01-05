import src.models.noDisplay as noDisplay
import src.models.utilities as ut
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
	startPos = [ROWS - 1, 54]
	choice = ut.chooseBot()

	if choice == '1':
		coordinates = ut.chooseCoordinates()
		noDisplay.startEasyBot(ROWS, COLS, startPos, coordinates)
	elif choice == '2':
		coordinates = ut.chooseCoordinates()
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




try:
	sio.wait()
except KeyboardInterrupt:
	print("Disconnecting...")
	sio.disconnect()
