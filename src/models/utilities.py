import views.testCases as testCases
import numpy as np
import simplejson


def chooseCoordinates():
	print("Choose what Test Case you want to use")
	print("1. coordinatesTest_1")
	print("2. coordinatesTest_2")
	print("3. coordinatesTest_3")
	print("4. coordinatesTest_4")
	coordinates = input("Enter your choice: ")

	if coordinates == '1':
		return testCases.coordinatesTest_1
	elif coordinates == '2':
		return testCases.coordinatesTest_2
	elif coordinates == '3':
		return testCases.coordinatesTest_3
	elif coordinates == '4':
		return testCases.coordinatesTest_4
	else:
		return None


def chooseBot():
	print("What is the Bot you want to test?")
	print("1. Easy Bot")
	print("2. Medium Bot")
	print("3. Hard Bot (UNDER CONSTRUCTION)")
	print("4. Exit")
	return input("Enter your choice: ")


# Function to create map from coordinates
def create_map_from_coordinates(coordinates, rows, cols):
	shape = (rows, cols)
	map_matrix = np.zeros(shape, dtype=int)
	for coord, value in coordinates:
		x, y = coord
		map_matrix[x, y] = value
	return map_matrix


# Define moves and directions
moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

# Updates map


def updateMap(gameMap, botPosition, new_position):
	# Set the current bot position to 0 (aka Empty)
	current_x, current_y = botPosition
	gameMap[current_x][current_y] = 0

	# Update the bot's position
	new_x, new_y = new_position
	# Set the new position of the bot to 1 (aka Occupied)
	gameMap[new_x][new_y] = 1

	# Update the bot's internal position variable
	botPosition[0] = new_x
	botPosition[1] = new_y
	return

# Bot's movement
# Check if the bot can move up


def checkUp(botPosition, gameMap):
	if botPosition[0] - 1 >= 0 and gameMap[botPosition[0] - 1][botPosition[1]] != -1:
		return True
	return False
# Check if the bot can move left


def checkLeft(botPosition, gameMap):
	if botPosition[1] - 1 >= 0 and gameMap[botPosition[0]][botPosition[1] - 1] != -1:
		return True
	return False
# Check if the bot can move right


def checkRight(botPosition, gameMap):
	if botPosition[1] + 1 < 7 and gameMap[botPosition[0]][botPosition[1] + 1] != -1:
		return True
	return False
# Frees the bot from a cone stuck position of 1 depth


def checkDown2Left(botPosition, gameMap):
	if botPosition[0] + 1 < 10 and botPosition[1] - 1 >= 0 and gameMap[botPosition[0] + 1][botPosition[1] - 1] != -1:
		return True
	return False


def checkDown2Right(botPosition, gameMap):
	if botPosition[0] + 1 < 10 and botPosition[1] + 1 < 7 and gameMap[botPosition[0] + 1][botPosition[1] + 1] != -1:
		return True
	return False


def checkSurroundingsAndMove(gameMap, botPosition, moves):
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
		updateMap(gameMap, botPosition,
				(botPosition[0] + 1, botPosition[1] - 2))
		moves.append("down-2-left")
		return moves
	if checkDown2Right(botPosition, gameMap):
		updateMap(gameMap, botPosition,
				(botPosition[0] + 1, botPosition[1] + 2))
		moves.append("down-2-right")
		return moves

#ROWS EQUALLS Y (100), COLS EQUALLS X (20)
def extractBotCoordinates(json_data):
	data = simplejson.loads(json_data)
	x, y = data["x"], data["y"]
	return (x, y)

def extractBotID(jsonData):
	data = simplejson.loads(jsonData)
	return data["idBot"]


#Still not sure if need to create my one or use past token
def extractToken(jsonData):
	data = simplejson.loads(jsonData)
	return data["token"]

def extractObstacles(jsonData):
	data = simplejson.loads(jsonData)
	coordinates = []
	for obstacle in data["obstaculos"]:
		x = obstacle["x"]
		y = obstacle["y"]
		coordinates.append(((x, y), -1))
	return coordinates
