# Напишите эффективную функцию, 
# вычисляющую последнюю цифру числа,являющегося результатом возведения числа A степень B


a = int(input())
b = int(input())
last_digit = a % 10

if last_digit == 1:
	print(1)
elif last_digit == 6:
	print(6)
elif last_digit == 0:
	print(0)
elif last_digit == 5:
	print(5)
elif last_digit == 3:
	print([3,9,7,1][b % 4 - 1])
elif last_digit == 4:
	print([4, 6][b % 2 - 1])
elif last_digit == 2:
	print([2,4,8,6][b % 4 - 1])
elif last_digit == 7:
	print([7,9,3,1][b % 4 - 1])
elif last_digit == 8:
	print([8,4,2,6][b % 4 - 1])
elif last_digit == 9:
	print([9,1][b % 2 - 1])
