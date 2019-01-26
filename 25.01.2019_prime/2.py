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

	smth = result[i-x]
	
	if i-x+1 < length:
		result[i-x+1] += smth
	if i*2-x < length:
		result[i*2-x] += smth
	if i*2+1-x < length:
		result[i*2+1-x] += smth
	if i*10-x < length:
		result[i*10-x] += smth
print(result[-1])