from collections import deque
import json
import random

# Easy Bot

def easyBot():
	moves = deque()
	i = 0
	while i < 80:
		x = random.randint(0, 3)
		if x == 0:
			moves.append("down")
		elif x == 1:
			moves.append("up")
		elif x == 2:
			moves.append("left")
		elif x == 3:
			moves.append("right")
		i += 1
	return json.dumps(list(moves))
