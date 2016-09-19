""" 9/19 - elevators

Write a function that models the elevators in a building. It will take 2 arguments:

- A list of numbers representing the floor each elevator starts on
- A list of (number, boolean) pairs representing elevator moves, 
(so (3, True) would mean to move elevator #3 up one floor; False means down)

Return a list representing the ending position of each elevator.

elevators([0, 0, 0], [(0, True), (2, False), (0, True), (1, True), (0, False)])
-> [1, 1, -1] """

def elevators(start_pos, moves):
	for move in moves:
		elevator, direction = move
		if direction:
			start_pos[elevator] += 1
		else:
			start_pos[elevator] -= 1
	return start_pos


print elevators([0, 0, 0], [(0, True), (2, False), (0, True), (1, True), (0, False)])

