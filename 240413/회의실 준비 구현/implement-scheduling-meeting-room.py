n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

count = 0
end = 0
for s, e in arr:
    if end <= s:
        end = e
        count += 1

print(count)