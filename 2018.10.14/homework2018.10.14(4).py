# Задание 4
# Напишите программу находящую в массиве сумму элементов делящихся либо
# на 72 либо на 27(не вместе).

n = int(input())
l = []
for i in range(n):
	l.append(int(input()))

print(sum((filter(lambda x: (x % 72 == 0 or x % 27 == 0) and x % 216 != 0, l))))