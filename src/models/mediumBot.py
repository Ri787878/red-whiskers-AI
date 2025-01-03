from collections import deque
from models.utilities import create_map_from_coordinates, checkSurroundingsAndMove
import json



# Medium Bot

def mediumBot(ROWS, COLS, start_pos, coordinates):
	gameMap = create_map_from_coordinates(coordinates, ROWS, COLS)
	moves = deque()
	while start_pos[1] != 0:
		moves = checkSurroundingsAndMove(gameMap, start_pos, moves)
	return json.dumps(list(moves))
