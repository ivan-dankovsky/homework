x_0 = 731
y_0 = 38144

i = -1
while True:
	i += 1
	x = x_0 + i*2019
	y = y_0 - i*2018
	if x < 0 or y < 0:
		break
	print('x_', i, ' = ', x)
	print('y_', i, ' = ', y)