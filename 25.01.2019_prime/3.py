x = int(input())
y = int(input())

l = list(range(x, y+1))
result = [0]*len(l)
result[l[0]-x] = 1
length = len(l)

for i in l:
	if i == y:
		if result[-1] == 0:
			print('NO')
		else:
			print('YES')
		break

	smth = result[i-x]
	if i-x+9 < length:
		result[i-x+9] += smth
	if i*i-x < length:
		result[i*i-x] += smth
	if i*7-x < length:
		result[i*7-x] += smth
	if int(str(i)+'1')-x < length:
		result[int(str(i)+'1')-x] += smth