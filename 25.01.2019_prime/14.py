def max_c(seq):
	length = len(seq)
	result = seq[0] + seq[-1]

	for i in range(length-5):
		for j in range(i+5, length):
			if result < seq[i] + seq[j]:
				result = seq[i] + seq[j]

	return result 

print(max_c([1,0,0,4,10000,100]))