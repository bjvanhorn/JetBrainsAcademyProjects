n = int(input())
nums = list()
for _ in range(n):
    m = int(input())
    if m % 7 == 0:
        nums.append(m)
for i in nums:
    print(i ** 2)
