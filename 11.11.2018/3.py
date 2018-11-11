# Сверхпростым числом будем называть такое простое число, что его номер
# в последовательности простых чисел –тоже прост. Напишите программу, 
# находящую k-ое сверхпростое число


k = int(input())
l = [2]
super_primes = []

next_int = 1
while len(super_primes) < k:
	next_int += 1
	is_next_int_prime = True
	for i in l:
		if next_int % i == 0:
			is_next_int_prime = False
			break

	if is_next_int_prime:
		l.append(next_int)

		if len(l) in l:
			super_primes.append(next_int)

print(super_primes[-1])