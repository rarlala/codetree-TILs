n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    if len(set(arr[i])) == n - m + 1:
       cnt += 1 
    
    if i == 0:
        c_list = []
        for j in range(n):
            c_list.append(arr[i][j])
        if len(set(c_list)) == n - m + 1:
            cnt += 1 

print(cnt)