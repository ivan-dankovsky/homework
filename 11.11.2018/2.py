#Напишите программу,вычисляющую сумму нечетных цифр целого числа.
print(sum(filter(lambda x: x % 2 != 0, map(int, list(input())))))
