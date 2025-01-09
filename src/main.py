#import src.models.botsPathfinding as BP
from models.easyBot import easyBot
from models.mediumBot import mediumBot
from models.hardBot import hardBot
import models.utilities as ut
import socketio
sio = socketio.Client()

#Declaring Global Variables
botID = 0
botType = 0
token = ""
obstacles = []
botStartingPosition = (0, 0)


@sio.event
def connect():
	print("Connected to the server.")
	sio.IaSocket = '123456789987654321'
	# Broadcast the value to the server
	sio.emit('IaApiConnection', {'IaSocket': sio.IaSocket})
	#sio.emit('PingTest', 'Hello from the Python client!')

@sio.on('status')
def handleConnection(data):
	print("Response  the server (status):", data)


@sio.on("JsonMoves")
def handleJsonMoves(data):
	global botID
	global botType
	global token
	global obstacles
	global botStartingPosition


	print("Response from the server (JasonMoves):", data)

	botID = ut.extractBotID(data)
	botType = ut.extractBotType(data)
	token = ut.extractToken(data)
	obstacles = ut.extractObstacles(data)
	botStartingPosition = ut.extractBotCoordinates(data)

	#Change event that i send to server
	#Maybe Create a token for IA like i can make it so it is like id plus typeBot plus token received from server

	if botType == 1:
		moves = easyBot()
		print(moves)

		jsonMoves = ut.compileJson(token, botID, moves)
		sio.emit('JsonMoves', jsonMoves)

		print(jsonMoves)
	elif botType == 2:
		moves = mediumBot(ROWS, COLS, botStartingPosition, obstacles)
		jsonMoves = ut.compileJson(token, botID, moves)
		sio.emit('JsonMoves', jsonMoves)
	elif botType == 3:
		moves =hardBot(ROWS, COLS, botStartingPosition, obstacles)
		jsonMoves = ut.compileJson(token, botID, moves)
		sio.emit('JsonMoves', jsonMoves)

# Connect to the Socket.IO server
#Change IP to connect while we dont have a domain
sio.connect("http://192.168.1.77:3000")


#Changeable Map Size
ROWS = 100
COLS = 20





try:
	sio.wait()
except KeyboardInterrupt:
	print("Disconnecting...")
	sio.disconnect()
