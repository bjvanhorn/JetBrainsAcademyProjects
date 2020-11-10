a, b = int(input()), int(input())
divisor = 0
dividend = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        divisor += 1
        dividend += i
print(dividend / divisor)
