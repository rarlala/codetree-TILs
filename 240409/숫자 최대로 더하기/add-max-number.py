n = int(input())
arr = list(map(int, input().split()))
arr.sort()

while len(arr) > 1:
    a, b = arr.pop(0), arr.pop()
    b += a / 2
    arr.append(b)

print(round(arr[0], 1))