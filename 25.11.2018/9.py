n = int(input())

l = list(range(2, n*2+2))

i = 0
while i < len(l):
	prime = l[i]

	for number in l[i+1:]:
		if number % prime == 0:
			l.remove(number)
	i += 1

result = []

for prime in l:
	if prime*2 + 1 in l:
		result.append(prime)
print(result)