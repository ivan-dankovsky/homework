# Напишите функции min, max, avg, med, процедуру swap принимающие в себя
# три вещественных аргумента и программу с примером из использования. min -
# находит минимальное из трех значений, max - максимальное, avg - среднее
# арифметическое, med  - медианное (гуглим, что это такое). swap - переставляет
# значения по кругу ( первое во второе, второе в третье, третье в первое).

def minimum(a: float, b: float, c: float):
	if a < b and a < c:
		return a
	elif b < a and b < c:
		return b
	else:
		return c

def maximum(a: float, b: float, c: float):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c

def avg(a: float, b: float, c: float):
	return (a+b+c)/3

def med(a: float, b: float, c: float):
	return sorted([a, b, c])[1]

def swap(a: float, b: float, c: float):
	return c, a, b

a = 1
b = 2 
c = 3

a, b, c = swap(a, b, c)

print(a, b, c)

print(avg(10,20,30), ' - среднее арифметическое 10, 20, 30')
print(maximum(10,20,30), ' - максимум из 10, 20, 30')
print(minimum(10,20,30), ' - минимум из 10, 20, 30')
print(med(10,20,30), ' - медианное значение')