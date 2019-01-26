N = int(input()) # кол-во чисел
def flm(seq):
	length = len(seq)
	result = -1

	for i in range(length-6):
		for j in range(i+6, length):
			if seq[i] % 2 == 0 or seq[j] % 2 == 0:
				if seq[i] * seq[j] > result:
					result = seq[i] * seq[j]

	return result

print(flm([1,3,3,333,5,8,4]))