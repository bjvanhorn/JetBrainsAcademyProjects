N = int(input())
years = 0
while N < 700000:
    N *= 1.071
    years += 1
print(years)
