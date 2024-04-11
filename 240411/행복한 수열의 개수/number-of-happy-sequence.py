n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = list(map(list, zip(*arr)))

result = 0

for temp in range(2):
    arr = arr if temp == 0 else new_arr
    
    for i in range(n):
        max_cnt = 0
        cnt = 1
        prev = arr[i][0]
        for j in arr[i]:
            if prev == j:
                cnt += 1
            else:
                cnt = 1
            prev = j
            max_cnt = max(max_cnt, cnt)
        if max_cnt >= m:
            result += 1
            break

print(result)