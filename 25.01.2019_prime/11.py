def num(seq):
	result = 0
	for i in range(1, len(seq)):
		if seq[i]/seq[i-1] < 2:
			result += 1

	return result

print(num([1,2,3,4,5, 100]))