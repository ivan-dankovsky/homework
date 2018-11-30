def ternary (n):
    if n == 0:
        return [0]
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(int(r))
    return list(reversed(nums))

def func(elements, k):
	result = 0
	for element in elements:
		e = ternary(element)
		n = e.count(2)
		if n < k:
			print(element)
		result += n
	return result

k = int(input())
l = [1, 2, 3, 4, 5, 6, 11, 15, 17]
func(l, k)