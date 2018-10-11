# Задание 1.
# Напишите программу проверяющую является ли число составным. В
# программе гарантируется, что число - натуральное

import math

number = int(input())
if number == 1:
	print('UNIT')

elif number not in [2, 5] and str(number)[-1] in '024568':
	print('COMPOSITE')

else:
	sqr_root = math.ceil(math.sqrt(number))

	list_of_primes = range(2, sqr_root+1)

	i = 0
	while i < len(list_of_primes):
		prime_number = list_of_primes[i]

		list_of_primes = list(filter(lambda x: x == prime_number or x % prime_number != 0, list_of_primes))

		i += 1


	is_prime = True
	for a in list_of_primes:
		if number % a == 0:
			print('COMPOSITE')
			is_prime = False

	if is_prime:
		print('PRIME')