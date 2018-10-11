# Напишите функцию sort упорядывающую массив целых чисел и программу с
# примером её использования. В коде запрещается использовать обращения к
# массиву по индексу( Arr[i] ), т.е. нужно использовать указательную арифметику.
# Эффективность в данной программе не приоритетна. Количество аргументов
# функции не должно превышать 2.

def sort(array):
	sorted_array = []

	while array != []:
		m = min(array)
		sorted_array.append(m)
		array.remove(m)

	return sorted_array

n = int(input())
a = []
for i in range(n):
	a.append(float(input()))

print(sort(a))