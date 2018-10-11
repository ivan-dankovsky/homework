# Напишите программу находящую минимальную сумму пары элементов массива
# отстоящих друг от друга не менее чем на 4 элемента(первый и пятый элемент
# могут подходить, а первый и третий - нет). Эффективность в данной программе
# не приоритетна

n = int(input())
a = []
for i in range(n):
	a.append(float(input()))

min_sum = a[0] + a[-1]
for i_1 in range(len(a)):
	if n < 5:
		print('ОШИБКА. ВВЕДИТЕ БОЛЬШЕЕ ЧИСЛО ЭЛЕМЕНТОВ')
		break


	i_2 = i_1 + 4
	if i_2 >= len(a): break


	while i_2 < len(a):
		if a[i_1] + a[i_2] < min_sum:
			min_sum = a[i_1] + a[i_2]

		i_2 += 1

if n > 5: print(min_sum)