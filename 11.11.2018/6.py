# Известно, что у дракона может быть несколько голов, и его сила определяется 
# числом голов. Но как определить силу драконьей стаи, в которой несколько 
# драконов и у каждого из них определенное число голов? Вероятно, вы считаете, 
# что это значение вычисляется, как сумма сил драконов. Это далеко не так. 
# Оказывается, что искомое значение равно произведению значений числа голов 
# каждого из драконов. Например.сила стаи состоящей из трёхглавого, 
# четырехглавого и пятиглавого драконов равна 60.
# Напишите программу, вычисляющую наибольшую возможную силу стаи, если дано количество голов в стае.
from functools import reduce

def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

print(max([reduce(lambda x,y: x * y, list(i)) for i in partitions(int(input()))]))