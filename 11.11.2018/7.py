# Напишите функцию, заполняющую двумерный прямоугольный массив 
# последовательными составными числами
# змейкой по часовой стрелке, начиная с нижнего левого угла


y = int(input())
x = int(input())

primes = [2]
next_int = 3
complex_numbers = []

while len(complex_numbers) <= x*y:
	is_next_int_prime = True

	for i in primes:
		if next_int % i == 0:
			is_next_int_prime = False
			break

	if not is_next_int_prime:
		complex_numbers.append(next_int)
	else:
		primes.append(next_int)
	next_int += 1

matrix = ['*'] * y
for i in range(y):
	matrix[i] = ["*"] * x

x_position = 0
y_position = y
direction = 'up'
print(complex_numbers)

for whatever in range(x*y):
	
	if direction == 'up' and y_position != 0 and matrix[y_position-1][x_position] == '*':
		y_position -= 1
		
	elif direction == 'up':
		direction = 'right'

	is_ok_to_use_x = True
	if x_position+1 == x: is_ok_to_use_x = False

	if is_ok_to_use_x and direction == 'right' and x_position < x and matrix[y_position][x_position+1] == '*':
		x_position += 1
		
	elif direction == 'right':
		direction = 'down'

	is_ok_to_use_y = True
	if y_position+1 == y: is_ok_to_use_y = False

	if is_ok_to_use_y and direction == 'down' and y_position < y and matrix[y_position+1][x_position] == '*':
		y_position += 1
		
	elif direction == 'down':
		direction = 'left'

	if direction == 'left' and x_position != 0 and matrix[y_position][x_position-1] == '*':
		x_position -= 1
		
	elif direction == 'left':
		direction = 'up'
		if y_position != 0 and matrix[y_position-1][x_position] == '*':
			y_position -= 1

	matrix[y_position][x_position] = complex_numbers[whatever]

for line in matrix:
	print(line)
