import json
import testCases
test1 =  [{'x': 29, 'y': 2, 'tipo': 2}, {'x': 4, 'y': 6, 'tipo': 2}, {'x': 86, 'y': 10, 'tipo': 2}, {'x': 34, 'y': 14, 'tipo': 2}, {'x': 49, 'y': 19, 'tipo': 1}, {'x': 79, 'y': 24, 'tipo': 2}, {'x': 76, 'y': 25, 'tipo': 2}, {'x': 85, 'y': 29, 'tipo': 2}, {'x': 27, 'y': 33, 'tipo': 2}, {'x': 88, 'y': 35, 'tipo': 1}, {'x': 43, 'y': 55, 'tipo': 2}, {'x': 29, 'y': 67, 'tipo': 2}, {'x': 93, 'y': 70, 'tipo': 2}, {'x': 43, 'y': 73, 'tipo': 2}, {'x': 99, 'y': 79, 'tipo': 2}, {'x': 3, 'y': 83, 'tipo': 2}, {'x': 17, 'y': 86, 'tipo': 2}, {'x': 86, 'y': 92, 'tipo': 2}, {'x': 61, 'y': 98, 'tipo': 2}, {'x': 82, 'y': 99, 'tipo': 2}]
test2 = [
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

print(type(test2))
print(test2)
print(type(test2[0][0]))
print("")
print("")

print(type(test1))
print(test1[0][0])

#print(json.loads(test1))
