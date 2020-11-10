n = int(input())
nums = list()
for _ in range(n):
    nums.append(int(input()))
mean = 0
for i in nums:
    mean += i
print(mean / n)
