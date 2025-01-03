
from models.utilities import chooseCoordinates, chooseBot
#from models.hardBot import a_star_search
import views.testCases as testCases
import pygame
import heapq

# Constants for the Pygame display
CELL_SIZE = 10
GRID_COLOR = (200, 200, 200)
START_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
PATH_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (255, 255, 255)

# A* Search Algorithm
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
	print (obstacles)
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
	return None


def draw_grid(screen, ROWS, COLS, startPos, path, coordinates):
	"""
	Draws the grid, start position, path, and obstacles.
	"""
	# Draw the grid
	for row in range(ROWS):
		for col in range(COLS):
			rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(screen, GRID_COLOR, rect, 1)  # Draw grid lines

	# Draw obstacles
	for obstacle in coordinates:
		if isinstance(obstacle, tuple) and len(obstacle) == 2:
			x, y = obstacle
			if isinstance(x, int) and isinstance(y, int):  # Ensure x, y are integers
				rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
				pygame.draw.rect(screen, OBSTACLE_COLOR, rect)
			else:
				print("Invalid obstacle coordinates:", obstacle)

	# Draw path
	if path:
		for step in path:
			print("Path Step:", step)  # Debugging output
			if isinstance(step, tuple) and len(step) == 2:
				x, y = step
				if isinstance(x, int) and isinstance(y, int):  # Ensure x, y are integers
					rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
					pygame.draw.rect(screen, PATH_COLOR, rect)
				else:
					print("Invalid path step coordinates:", step)

	# Draw start position
	if isinstance(startPos, tuple) and len(startPos) == 2:
		x, y = startPos
		if isinstance(x, int) and isinstance(y, int):  # Ensure x, y are integers
			rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(screen, START_COLOR, rect)
		else:
			print("Invalid start position coordinates:", startPos)







#Changeable Map Size
ROWS = 100
COLS = 70

#Start Position
startPos = [ROWS - 1, 54]
dest = [0, 54]

coordinates = testCases.coordinatesTest_1
path = a_star_search(ROWS, COLS, startPos, coordinates)
if path is None:
	print("No path found!")
else:
	print("Path:", path)




path = a_star_search(ROWS, COLS, startPos, coordinates)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE), pygame.RESIZABLE)
pygame.display.set_caption("A* Pathfinding Visualization")

# Main loop
running = True
while running:
	screen.fill(BACKGROUND_COLOR)
	# Draw the grid, start position, path, and obstacles
	draw_grid(screen, ROWS, COLS, tuple(startPos), path, [tuple(c) for c in coordinates])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Exit on ESC
			running = False
	pygame.display.flip()

pygame.quit()


"""
while True:
	#Start Position
	startPos = [ROWS - 1, 54]
	dest = [0, 54]
	choice = chooseBot()

	if choice == '1':
		coordinates = chooseCoordinates()
		noDisplay.startEasyBot(ROWS, COLS, startPos, coordinates)
	elif choice == '2':
		coordinates = chooseCoordinates()
		jsonMoves = noDisplay.startMediumBot(ROWS, COLS, startPos, coordinates)
	elif choice == '3':
		coordinates = chooseCoordinates()
		jsonMoves = a_star_search(ROWS, COLS, startPos, dest, coordinates)
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue
"""
