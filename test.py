import simplejson

def extractBotCoordinates(json_data):
	data = simplejson.loads(json_data)
	x, y = data["x"], data["y"]
	return (x, y)

def extractBotID(jsonData):
	data = simplejson.loads(jsonData)
	return data["idBot"]

def extractToken(jsonData):
	data = simplejson.loads(jsonData)
	return data["token"]


def extractObstacles(jsonData):
	data = simplejson.loads(jsonData)
	coordinates = []
	for obstacle in data["obstaculos"]:
		x = obstacle["x"]
		y = obstacle["y"]
		tipo = obstacle["tipo"]
		coordinates.append(((x, y), -1))
	return coordinates
# Example usage
json_message = '''
{
	"idBot": 38,
	"typeBot": 1,
	"token": "68c184312b6b8fa09f2c0ab8b3f94436064b503385116e17249f5e1b3a2636df4db9404e415e5f70",
	"obstaculos": [
		{"y": 3, "x": 13, "tipo": 1},
		{"y": 3, "x": 11, "tipo": 1},
		{"y": 4, "x": 1, "tipo": 1},
		{"y": 7, "x": 15, "tipo": 1},
		{"y": 10, "x": 5, "tipo": 1},
		{"y": 14, "x": 9, "tipo": 1},
		{"y": 17, "x": 14, "tipo": 1},
		{"y": 25, "x": 11, "tipo": 1},
		{"y": 30, "x": 13, "tipo": 1},
		{"y": 33, "x": 17, "tipo": 1},
		{"y": 38, "x": 17, "tipo": 1},
		{"y": 40, "x": 17, "tipo": 1},
		{"y": 51, "x": 4, "tipo": 1},
		{"y": 54, "x": 4, "tipo": 1},
		{"y": 58, "x": 17, "tipo": 1},
		{"y": 65, "x": 11, "tipo": 1},
		{"y": 69, "x": 4, "tipo": 1},
		{"y": 74, "x": 1, "tipo": 1},
		{"y": 95, "x": 8, "tipo": 1},
		{"y": 96, "x": 9, "tipo": 1}
	],
	"x": 10,
	"y": 0
}
'''
token = extractToken(json_message)
coordinates = extractBotCoordinates(json_message)
bot_id = extractBotID(json_message)
obstacles = extractObstacles(json_message)

print(f"{json_message}")

print(f"Coordinates: {coordinates}")
print(f"Bot ID: {bot_id}")
print(f"Token: {token}")
print(f"Obstacles: {obstacles}")
