x = int(input())
y = int(input())

l = list(range(x, y+1))
length = len(l)
result = [0]*length
programs = [[]]*length
result[0] = 1

act_1 = 'ПРИБАВИТЬ 1'
act_2 = 'ПРИБАВИТЬ 4'
act_3 = 'ПРИБАВИТЬ 5'
act_4 = 'УМНОЖИТЬ НА 2'

for i in l:
	smth = result[i-x]
	prog = programs[i-x]
	lenn = len(prog)+1

	if i-x+1 < length and smth > 0:
		result[i-x+1] += smth
		if lenn < len(programs[i-x+1]) or programs[i-x+1] == []:
			programs[i-x+1] = programs[i-x] + [act_1]

	if i-x+4 < length and smth > 0:
		result[i-x+4] += smth		
		if lenn < len(programs[i-x+4]) or programs[i-x+4] == [] :
			programs[i-x+4] = programs[i-x] + [act_2]

	if i-x+5 < length and smth > 0:
		result[i-x+5] += smth		
		if lenn < len(programs[i-x+5]) or programs[i-x+5] == []:
			programs[i-x+5] = programs[i-x] + [act_3]


	if i*2-x < length and smth > 0:
		result[i*2-x] += smth

		if lenn < len(programs[i*2-x]) or programs[i*2-x] == []:
			programs[i*2-x] = programs[i-x] + [act_4]


print(programs[-1])