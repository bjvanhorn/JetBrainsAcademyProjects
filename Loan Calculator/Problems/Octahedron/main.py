from math import sqrt

side = int(input())
area = 2 * sqrt(3) * side ** 2
volume = 1 / 3 * sqrt(2) * side ** 3
print(f'{round(area, 2)} {round(volume, 2)}')
