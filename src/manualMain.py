
from models.utilities import chooseCoordinates, chooseBot
from models.hardBot import hardBot
from models.mediumBot import mediumBot
import views.testCases as testCases

#Changeable Map Size
ROWS = 100
COLS = 70

#Start Position
startPos = [ROWS - 1, 54]
dest = [0, 54]

coordinates = testCases.coordinatesTest_2


path = hardBot(ROWS, COLS, startPos, coordinates)
pathMedium = mediumBot(ROWS, COLS, startPos, coordinates)

if path is None:
	print("No path found!")
else:
	print("Path:", path)

if pathMedium == path:
	print("Paths are equal")
else:
	print("Paths are different")
	print("Medium Path:", pathMedium)


"""
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE), pygame.RESIZABLE)
pygame.display.set_caption("A* Pathfinding Visualization")

# Main loop
running = True
while running:
	screen.fill(BACKGROUND_COLOR)
	# Draw the grid, start position, path, and obstacles
	draw_grid(screen, ROWS, COLS, startPos, path, coordinates)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Exit on ESC
			running = False
	pygame.display.flip()

pygame.quit()



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
