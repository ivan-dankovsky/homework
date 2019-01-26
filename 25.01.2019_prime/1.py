x = int(input())
y = int(input())

l = list(range(x, y+1))
result = [0]*len(l)
result[l[0]-x] = 1
length = len(l)-1

for i in l:
	smth = result[i-x]
	if i-x+1 <= length:
		result[i-x+1] += smth
	if i*2-x <= length:
		result[i*2-x] += smth
	if i*3-x <= length:
		result[i*3-x] += smth
print(result[-1])