import noDisplay

#Changeable Map Size
ROWS = 100
COLS = 70

while True:
	#Start Position
	start_pos = [ROWS - 1, 54]
	choice = noDisplay.chooseBot()

	if choice == '1':
		coordinates = noDisplay.chooseCoordinates()
		noDisplay.easyBot(ROWS, COLS, start_pos, coordinates)
	elif choice == '2':
		coordinates = noDisplay.chooseCoordinates()
		noDisplay.mediumBot(ROWS, COLS, start_pos, coordinates)
	elif choice == '3':
		print("Hard Bot")
		print("UNDER CONSTRUCTION")
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue
