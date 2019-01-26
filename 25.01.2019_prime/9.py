N = int(input())
x = int(input())
y = int(input())

result = []
for i in [-1, 1]:
	for j in [-2, 2]:
		x_1 = x+i
		y_1 = y+j

		x_2 = x+j
		y_2 = x+i 

		if x_1 >= 1 and x_1 <= N and y_1 >= 1 and y_1 <= N:
			if [x_1, y_1] not in result:
				result.append([x_1, y_1])

		if x_2 >= 1 and x_2 <= N and y_2 >= 1 and y_2 <= N:
			if [x_2, y_2] not in result:
				result.append([x_2, y_2])

print(result)