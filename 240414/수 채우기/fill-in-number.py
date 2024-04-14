n = int(input())

result = 0
for i in [5, 2]:
    num = n // i
    n -= (num * i)
    result += num

print(result if n == 0 else -1)