n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
while len(arr) != 1:
    value = 0
    for i in range(2):
        a = arr.index(min(arr))
        value += arr.pop(a)

    arr.append(value)
    result += value

print(result)