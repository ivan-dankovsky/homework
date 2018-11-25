n = int(input())

if n % 2 == 0:
	i = int("1" + "0" * int(n / 2 - 1))
	while len(str(i)) == int(n / 2):
		print(str(i) + str(i)[::-1])
		i += 1
else:
	n -= 1
	for medium in range(10):
		i = int("1" + "0" * int(n / 2 - 1))

		while len(str(i)) == int(n / 2):
			print(str(i) + str(medium) + str(i)[::-1])
			i += 1


# Количество действией асимптотически равно длине ответа -> алгоритм эффективен 