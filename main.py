import noDisplay

#Changeable Map Size
ROWS = 100
COLS = 70

while True:
	#Start Position
	startPos = [ROWS - 1, 54]
	choice = noDisplay.chooseBot()

	if choice == '1':
		coordinates = noDisplay.chooseCoordinates()
		noDisplay.startEasyBot(ROWS, COLS, startPos, coordinates)
	elif choice == '2':
		coordinates = noDisplay.chooseCoordinates()
		noDisplay.startMediumBot(ROWS, COLS, startPos, coordinates)
	elif choice == '3':
		print("Hard Bot")
		print("UNDER CONSTRUCTION")
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue
