n = int(input())
arr = [int(input()) for _ in range(n)]

result = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            check = False
            max_num = (arr[i], arr[j], arr[k])
            
            for l in range(len(str(max_num))):
                sum = 0
                if len(str(arr[i])) - 1 >= l:
                    sum += int(str(arr[i])[-l + -1])
                if len(str(arr[j])) - 1 >= l:
                    sum += int(str(arr[j])[-l + -1])
                if len(str(arr[k])) - 1 >= l:
                    sum += int(str(arr[k])[-l + -1])
                    
                if sum >= 10:
                    check = True
                    break
            
            result = result if check else max(result, arr[i] + arr[j] + arr[k])

print(result)