from math import sqrt

side_a, side_b, side_c = int(input()), int(input()), int(input())
p = (side_a + side_b + side_c) / 2
print(sqrt(p * (p - side_a) * (p - side_b) * (p - side_c)))
