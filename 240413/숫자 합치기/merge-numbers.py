n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
while len(arr) != 1:
    a = arr.pop(0)
    b = arr.pop(0)

    value = a + b
    result += value
    arr.append(value)
    arr.sort()

print(result)