n = int(input())
arr = [] 
max_num = 0

for _ in range(n):
    a, b = map(int, input().split())
    max_num = max(max_num, b)
    arr.append((a, b))

time = [0] * (max_num + 1)

for a, b in arr:
    for t in range(a, b):
        time[t] += 1

idx = 0
max_count = 0

for i in range(n):
    a, b = arr[i]
    count = 0
    for t in range(a, b):
        if time[t] > 1:
            count += 1
    if max_count < count:
        max_count = count
        idx = i

for t in range(arr[idx][0], arr[idx][1]):
    time[t] -= 1

result = 0
for i in time:
    if i > 0:
        result += 1
print(result)