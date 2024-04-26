n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_time = 0

for i in range(n):    
    time = set()

    for j in range(n):
        if i == j:
            continue
  
        for t in range(arr[j][0], arr[j][1]):
            time.add(t)
     
    max_time = max(len(time), max_time)

print(max_time)