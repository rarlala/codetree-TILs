n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

while len(arr) > 1:
    a, b = arr.pop(), arr.pop(0)
    b += a / 2
    arr.append(b)
    arr.sort(reverse = True)

print(round(arr[0], 1))