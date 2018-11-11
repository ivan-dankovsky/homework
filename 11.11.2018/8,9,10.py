# Программа для игры в Сапера

import random

def map_gen(m, n, p):
	# m - "ширина" карты
	# n - "высота" карты
	# p - вероятность появления мины в данной клетке

	field = [""] * n

	for y in range(n):
		field[y] = ["*"]*m
		for x in range(m):
			if random.random() <= p:	
				field[y][x] = -1


	return field

def map_bombs(m, n, field):
	for y in range(n):
		for x in range(m):
			if field[y][x] == "*":
				field [y][x] = 0
				for y_1 in range(y-1, y+2):
					for x_1 in range(x-1, x+2):
						if (0 <= x_1 < m and 0 <= y_1 < n) and (x_1 != x or y_1 != y):
							if field[y_1][x_1] == -1:
								field[y][x] += 1

	return field

def plant_bomb(x, y, field):
	field[y][x] = -1
	return field



chance = input("Введите вероятность: ")
m = int(input("Введите ширину поля: "))
n = int(input("Введите высоту поля: "))

field = map_gen(m,n,float(chance))
field = map_bombs(m,n,field)
player_field = ["*"] * m

bombs = 0
for y in range(n):
	for x in range(m):
		if field[y][x] == -1:
			bombs += 1
for i in range(n):
	player_field[i] = ["*"] * m

while True:
	print([" "] + list(range(1,m+1)))
	for y in range(n):
		print([y+1] + player_field[y])
	x = int(input())-1
	y = int(input())-1

	if field[y][x] == -1:
		print("ВЫ ПРОИГРАЛИ")
		break
	else:
		player_field[y][x] = field[y][x]

	unopened_cells = n * m
	for y in range(n):
		for x in range(m):
			if player_field[y][x] != '*':
				unopened_cells -= 1

	if unopened_cells == bombs:
		print("ПОБЕДА")
		break
