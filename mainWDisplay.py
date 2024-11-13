import display

#Changeable Map Size
ROWS = 100
COLS = 70
WIDTH = 1000
HEIGHT = 800
CELL_SIZE = 10

while True:
	#Start Position
	startPos = [ROWS - 1, 54]
	choice = display.chooseBot()

	if choice == '1':
		coordinates = display.chooseCoordinates()
		display.startEasyBot(ROWS, COLS, CELL_SIZE, startPos, coordinates)
	elif choice == '2':
		coordinates = display.chooseCoordinates()
		display.startMediumBot(ROWS, COLS, CELL_SIZE, tuple(startPos), coordinates)
	elif choice == '3':
		print("Hard Bot")
		print("UNDER CONSTRUCTION")
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue
