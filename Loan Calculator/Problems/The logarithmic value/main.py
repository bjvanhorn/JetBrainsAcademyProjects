from math import log

num_a, num_b = int(input()), int(input())
if num_b < 2:
    print(round(log(num_a), 2))
else:
    print(round(log(num_a, num_b), 2))
