n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for a in arr:
    s, e = a

    if end <= s:
        count += 1
        end = e

print(n - count)