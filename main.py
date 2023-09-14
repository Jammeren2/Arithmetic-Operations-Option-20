import math

a = float(input('Введите a: '))
B = float(input('Введите B: '))

z1 = (math.sin(a) + math.cos(2 * B - a)) / (math.cos(a) + math.sin(2 * B - a))
z2 = (1 + math.sin(2 * B)) / math.cos(2 * B)

print (f'z1 = {z1}')
print (f'z2 = {z2}')