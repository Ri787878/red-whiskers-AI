

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


coordinatesTest_2 = [
    ((5, 10), -1), ((12, 45), -1), ((20, 30), -1), ((25, 60), -1),
    ((33, 15), -1), ((40, 65), -1), ((45, 25), -1), ((52, 50), -1),
    ((55, 40), -1), ((60, 55), -1), ((65, 35), -1), ((70, 60), -1),
    ((75, 20), -1), ((80, 10), -1), ((85, 25), -1), ((90, 45), -1),
    ((95, 50), -1), ((22, 30), -1), ((28, 55), -1), ((34, 60), -1),
    ((38, 11), -1), ((42, 50), -1), ((49, 33), -1), ((53, 24), -1),
    ((57, 35), -1), ((63, 40), -1), ((69, 37), -1), ((76, 55), -1),
    ((83, 49), -1), ((88, 65), -1), ((13, 30), -1), ((19, 17), -1),
    ((27, 40), -1), ((31, 64), -1), ((35, 21), -1), ((47, 36), -1),
    ((59, 45), -1), ((61, 47), -1), ((78, 18), -1), ((96, 22), -1),
    ((14, 55), -1), ((21, 35), -1), ((29, 20), -1), ((37, 45), -1),
    ((43, 30), -1), ((51, 10), -1), ((58, 60), -1), ((64, 45), -1),
    ((71, 30), -1), ((77, 35), -1), ((84, 35), -1), ((91, 20), -1),
    ((97, 10), -1), ((15, 45), -1), ((23, 55), -1), ((30, 10), -1),
    ((36, 30), -1), ((41, 15), -1), ((48, 50), -1), ((54, 40), -1),
    ((62, 25), -1), ((68, 60), -1), ((74, 35), -1), ((79, 45), -1),
    ((86, 55), -1), ((92, 40), -1), ((98, 30), -1), ((16, 30), -1),
    ((24, 45), -1), ((32, 55), -1), ((39, 20), -1), ((46, 35), -1),
    ((50, 50), -1), ((56, 60), -1), ((66, 45), -1), ((72, 30), -1),
    ((81, 40), -1), ((87, 55), -1), ((93, 40), -1), ((99, 30), -1),
    ((17, 45), -1), ((26, 55), -1), ((44, 35), -1), ((67, 45), -1),
    ((73, 30), -1), ((82, 40), -1), ((94, 40), -1), ((18, 30), -1),
    ((38, 45), -1), ((55, 60), -1), ((68, 45), -1), ((74, 30), -1),
    ((83, 40), -1), ((95, 40), -1), ((19, 30), -1), ((27, 45), -1),
    ((3, 13), -1), ((8, 27), -1), ((14, 50), -1), ((21, 42), -1),
    ((25, 18), -1), ((27, 22), -1), ((33, 29), -1), ((36, 43), -1),
    ((40, 19), -1), ((43, 24), -1), ((48, 62), -1), ((53, 53), -1),
    ((58, 21), -1), ((61, 15), -1), ((64, 54), -1), ((67, 32), -1),
    ((72, 13), -1), ((75, 48), -1), ((77, 58), -1), ((80, 28), -1),
    ((83, 59), -1), ((87, 32), -1), ((90, 12), -1), ((92, 53), -1),
    ((94, 16), -1), ((99, 27), -1), ((4, 52), -1), ((6, 25), -1),
    ((12, 33), -1), ((14, 22), -1), ((20, 47), -1), ((23, 13), -1),
    ((29, 62), -1), ((31, 47), -1), ((34, 23), -1), ((37, 32), -1),
    ((41, 51), -1), ((46, 48), -1), ((50, 29), -1), ((54, 53), -1),
    ((58, 15), -1), ((60, 62), -1), ((65, 41), -1), ((69, 21), -1),
    ((72, 50), -1), ((78, 40), -1), ((81, 23), -1), ((84, 62), -1),
    ((89, 34), -1), ((93, 26), -1), ((96, 35), -1), ((98, 16), -1),
    ((2, 45), -1), ((7, 32), -1), ((11, 23), -1), ((16, 18), -1),
    ((19, 54), -1), ((24, 27), -1), ((28, 36), -1), ((32, 14), -1),
    ((38, 25), -1), ((41, 19), -1), ((47, 60), -1), ((52, 23), -1),
    ((55, 14), -1), ((59, 18), -1), ((63, 55), -1), ((66, 28), -1),
    ((71, 44), -1), ((74, 50), -1), ((76, 16), -1), ((82, 52), -1),
    ((85, 14), -1), ((88, 18), -1), ((91, 29), -1), ((95, 18), -1),
    ((0, 35), -1), ((9, 42), -1), ((13, 12), -1), ((17, 26), -1),
    ((22, 37), -1), ((26, 12), -1), ((30, 20), -1), ((33, 38), -1),
    ((35, 50), -1), ((39, 33), -1), ((45, 28), -1), ((49, 60), -1),
    ((56, 22), -1), ((60, 19), -1), ((64, 29), -1), ((70, 42), -1),
    ((73, 38), -1), ((78, 25), -1), ((80, 36), -1), ((86, 41), -1),
    ((92, 24), -1), ((98, 19), -1), ((1, 60), -1), ((4, 23), -1),
    ((10, 17), -1), ((15, 50), -1), ((18, 43), -1), ((22, 58), -1),
    ((28, 24), -1), ((32, 60), -1), ((35, 12), -1), ((40, 25), -1),
    ((44, 20), -1), ((51, 27), -1), ((57, 52), -1), ((62, 48), -1),
    ((65, 27), -1), ((69, 50), -1), ((74, 12), -1), ((79, 29), -1),
    ((85, 52), -1), ((88, 38), -1), ((91, 12), -1), ((96, 18), -1),
]