n = int(input())
ans = 1e9

for i in range(0, n):
    remainder = n - (5 * i)
    if remainder >= 0 and remainder % 2 == 0:
        ans = min(ans, i + (remainder // 2))

if ans == 1e9:
    ans = -1

print(ans)