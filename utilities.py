import testCases
def chooseCoordinates():
	print("Choose what Test Case you want to use")
	print("1. coordinatesTest_1")
	print("2. coordinatesTest_2")
	print("3. coordinatesTest_3")
	print("4. coordinatesTest_4")
	coordinates = input("Enter your choice: ")

	if coordinates == '1':
		return testCases.coordinatesTest_1
	elif coordinates == '2':
		return testCases.coordinatesTest_2
	elif coordinates == '3':
		return testCases.coordinatesTest_3
	elif coordinates == '4':
		return testCases.coordinatesTest_4
	else:
		return None

def chooseBot():
	print("What is the Bot you want to test?")
	print("1. Easy Bot")
	print("2. Medium Bot")
	print("3. Hard Bot (UNDER CONSTRUCTION)")
	print("4. Exit")
	return input("Enter your choice: ")


# Function to create map from coordinates
def create_map_from_coordinates(coordinates, rows, cols):
    shape = (rows, cols)
    map_matrix = np.zeros(shape, dtype=int)
    for coord, value in coordinates:
        x, y = coord
        map_matrix[x, y] = value
    return map_matrix

