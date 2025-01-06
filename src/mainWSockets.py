import models.noDisplay as noDisplay
import models.utilities as ut
import socketio
sio = socketio.Client()

@sio.event
def connect():
	print("Connected to the server.")
	sio.IaSocket = '123456789987654321'
	# Broadcast the value to the server
	sio.emit('IaApiConnection', {'IaSocket': sio.IaSocket})
	#sio.emit('PingTest', 'Hello from the Python client!')



#"Obstacles":[{"x":0, "y":0, "tipo":1},{"x":0, "y":10, "tipo":1}]}'
@sio.on('status')
def response(data):
	coordinates = tuple(data.items())
	print("Response from the server:", data)

# Connect to the Socket.IO server
sio.connect("http://10.36.243.29:3000")


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
