# Напишите программу, определяющую количество нулей в числе N!
# Известно, что N помещается в тип unsigned int

n = int(input()) 
result = 0
i = 5
while (n/i>=1): 
    result += int(n/i) 
    i *= 5

print(result)
