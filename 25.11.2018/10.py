n = int(input())
l = list(range(2, n+1))
i = 0
while i < len(l):
	element = l[i]
	for e in l[i+1:]:
		if e % element == 0:
			l.remove(e)
	i += 1

result = 1
for i in l:
	result *= i
print(result)