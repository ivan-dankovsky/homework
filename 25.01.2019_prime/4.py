x = int(input())
y = int(input())
z = int(input())

l = list(range(x, y+1))
length = len(l)
result = [0]*length
result[0] = 1


for i in l:
	if i == z:
		result[i-x] = 0
 
	if i == y:
		if result[-1] == 0:
			print('NO')
		else:
			print('YES')

		break 

	smth = result[i-x]

	if i+5-x < length:
		result[i+5-x] += smth
	if i*3-x < length:
		result[i*3-x] += smth
	if i*i-x < length:
		result[i*i-x] += smth
	if int(str(i)+'2')-x < length:
		result[int(str(i)+'2')-x] += smth