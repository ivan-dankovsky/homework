x_1 = int(input())
y_1 = int(input())
z_1 = int(input())

act_1 = 'ПРИБАВИТЬ 2'
act_2 = 'ПРИБАВИТЬ 4'
act_3 = 'ПРИБАВИТЬ 5'
act_4 = 'УМНОЖИТЬ НА 3'

def a_way(x, y):

	l = list(range(x, y+1))
	length = len(l)
	result = [0]*length
	programs = [[]]*length
	result[0] = 1

	for i in l:


		smth = result[i-x]
		prog = programs[i-x]
		lenn = len(prog)+1

		if i-x+2 < length and smth > 0:
			result[i-x+2] += smth
			if lenn < len(programs[i-x+2]) or programs[i-x+2] == []:
				programs[i-x+2] = programs[i-x] + [act_1]

		if i-x+4 < length and smth > 0:
			result[i-x+4] += smth		
			if lenn < len(programs[i-x+4]) or programs[i-x+4] == []:
				programs[i-x+4] = programs[i-x] + [act_2]

		if i-x+5 < length and smth > 0:
			result[i-x+5] += smth		
			if lenn < len(programs[i-x+5]) or programs[i-x+5] == []:
				programs[i-x+5] = programs[i-x] + [act_3]


		if i*3-x < length and smth > 0:
			result[i*3-x] += smth

			if lenn < len(programs[i*3-x]) or programs[i*3-x] == []:
				programs[i*3-x] = programs[i-x] + [act_4]

	return programs[-1]

way_1 = a_way(x_1, z_1)
if way_1 != []: 
	way_2 = a_way(z_1, y_1)
	if way_2 != []:
		print(way_1 + way_2)
	else:
		print('NO')
else:
	print('NO')