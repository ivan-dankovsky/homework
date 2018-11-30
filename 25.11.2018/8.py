l = ['a', 'b', 'c', 'd']
print(''.join(l))
l = list(map(ord, l))
l_copy = l.copy()
n = len(l)
while True:
	max_j = 0
	for j in range(n):
		if j > max_j and j+1 != n and l[j+1] > l[j]:
			max_j = j
	max_l = max_j
	for j in range(n):
		if j > max_l and l[j] > l[max_j]:
			max_l = j
	l[max_j], l[max_l] = l[max_l], l[max_j]
	l = l[0:max_j+1] + list(reversed(l[max_j+1:n]))
	for i in l:
		print(chr(i), end='')

	print("")
	if list(reversed(l)) == l_copy:
		break