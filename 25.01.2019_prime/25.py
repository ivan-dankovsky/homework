def flm(seq):
	length = len(seq)
	result = 0

	for i in range(length-4):
		for j in range(i+4, length):
			if (seq[i] * seq[j]) % 38 == 0:
				result += 1

	return result

print(flm([2,0,0,38,19]))