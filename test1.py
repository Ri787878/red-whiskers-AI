def extract_x_coordinates(coordinates):
    # Extract the x-coordinate (first part of each tuple) from all the tuples
    return [coord[0] for coord in coordinates]

# Original list of tuples (coordinatesTest_1)
coordinatesTest_1 = [
    ((70, COLS), -1) for COLS in range(0, 68)
] + [
    ((60, COLS), -1) for COLS in range(2, 70)
] + [
    ((50, COLS), -1) for COLS in range(0, 68)
] + [
    ((40, COLS), -1) for COLS in range(2, 70)
] + [
    ((30, COLS), -1) for COLS in range(0, 68)
] + [
    ((20, COLS), -1) for COLS in range(2, 70)
] + [
    ((10, COLS), -1) for COLS in range(0, 68)
]

# Call the function to extract all x-coordinates
x_coordinates = extract_x_coordinates(coordinatesTest_1)

# Print the list of all extracted x-coordinates
print(x_coordinates)
