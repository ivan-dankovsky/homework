n = int(input())
k = int(input())
l = []

for i in range(n):
	l.append(int(input()))

for i in l:
	n = 1
	for j in list(str(i)):
		if int(j) != 0: n *= int(j)

	if n > k:
		print(i)

# Количество действией асимптотически равно длине ответа -> алгоритм эффективен 