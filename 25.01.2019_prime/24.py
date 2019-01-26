def flm(seq):
	length = len(seq)
	result = 0

	for i in range(length-1):
		for j in range(i+1, length):
			if (seq[i] + seq[j]) % 9 == 0:
				result += 1
	return result

print(flm([2,0,0,38,19, 9, 9]))