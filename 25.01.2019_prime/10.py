def mult(seq):
	result = 1
	for element in seq:
		temp = str(element)
		if temp[-1] not in '02468' and sum(map(int, list(temp))) % 3 == 0:
			result *= element

	return result

print(mult([1,2,3,4,5,6,153])) 