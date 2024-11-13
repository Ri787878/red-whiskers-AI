import time
import noDisplay
import coordinateTests

#Changable Map Size
ROWS = 100
COLS = 70

#Start Position
start_pos = [ROWS - 1, 54]


print("What is the Bot you want to test?")
print("1. Easy Bot")
print("2. Medium Bot")
print("3. Hard Bot (UNDER CONSTRUCTION)")
print("4. Exit")
while True:
	choice = input("Enter your choice: ")
	if choice == '1':
		print("Easy Bot")
		#start_time = time.time()
		start_time = time.time()
		json_path = noDisplay.easyBot(ROWS, COLS, start_pos, coordinateTests.coordinatesTest_1)
		print("json_path = ", json_path)
		print("Time taken: ", time.time() - start_time)
	elif choice == '2':
		print("Medium Bot")
		start_time = time.time()
		json_path = noDisplay.mediumBot(ROWS, COLS, tuple(start_pos), coordinateTests.coordinatesTest_1)
		print("json_path = ", json_path)
		print("Time taken: ", time.time() - start_time)
	elif choice == '3':
		print("Hard Bot")
		print("UNDER CONSTRUCTION")
	elif choice == 'c':
		break
	else:
		print("Invalid Choice")
		continue
