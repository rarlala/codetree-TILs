n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

result = 0
while len(arr) != 1:
    a = arr.pop()
    b = arr.pop()

    value = a + b 
    arr.append(value)
    arr.sort(reverse = True)
    result += value

print(result)