n = int(input())
arr = list(map(int, input().split()))
results = []
count = 0

for i in range(n):
    for j in range(i, n):
        if i == j:
            count += 1
        else:
            num = sum(arr[i:j + 1]) / len(arr[i: j + 1])
            if num in arr[i:j + 1]:
                count += 1

print(count)