import heapq

def a_star_search(ROWS, COLS, startPos, coordinates):
	# Ensure all inputs are tuples
	startPos = tuple(startPos)
	coordinates = [tuple(coord) for coord in coordinates]

	def heuristic(a):
		"""Heuristic function: Manhattan distance to row 0."""
		return a[0]  # Distance to row 0 is simply the row index

	# Directions for moving in 4 possible directions (up, down, left, right)
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

	# Initialize open list (priority queue) and closed set
	open_list = []
	heapq.heappush(open_list, (0, startPos))  # (f-score, position)
	came_from = {}  # To reconstruct the path
	g_score = {startPos: 0}
	f_score = {startPos: heuristic(startPos)}  # Heuristic to row 0
	closed_set = set()

	# Mark obstacles
	obstacles = set(coordinates)

	while open_list:
		_, current = heapq.heappop(open_list)

		if current in closed_set:
			continue

		# If any position in row 0 is reached
		if current[0] == 0:
			path = []
			while current in came_from:
				path.append(current)
				current = came_from[current]
			path.append(startPos)
			return path[::-1]  # Reverse the path

		closed_set.add(current)

		# Explore neighbors
		for dx, dy in directions:
			neighbor = (current[0] + dx, current[1] + dy)

			# Check if neighbor is within bounds and not an obstacle
			if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and neighbor not in obstacles:
				tentative_g_score = g_score[current] + 1

				if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, float('inf')):
					continue

				if tentative_g_score < g_score.get(neighbor, float('inf')):
					came_from[neighbor] = current
					g_score[neighbor] = tentative_g_score
					f_score[neighbor] = tentative_g_score + heuristic(neighbor)
					heapq.heappush(open_list, (f_score[neighbor], neighbor))

	return None  # Return None if no path is found







"""
def hardBot(ROWS, COLS, start_pos, coordinates):
	gameMap = create_map_from_coordinates(coordinates, ROWS, COLS)
	return json.dumps(list(moves))

#Hard Bot

def heuristic(a, b):
	return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)



def hardBot(ROWS, COLS, start_pos, coordinates):
	dest = [0, 54]
	a_star_search(coordinates, start_pos, dest)
	return json.dumps(list(moves))
"""
