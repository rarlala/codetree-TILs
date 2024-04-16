import heapq

MAX_T = 10000

n = int(input())
bombs = []

for _ in range(n):
    p, t = tuple(map(int, input().split()))
    bombs.append((t, p))

def get_time_limit(bomb_idx):
    time_limit, _ = bombs[bomb_idx]
    return time_limit

def get_score(bomb_idx):
    _, score = bombs[bomb_idx]
    return score

bombs.sort()

pq = []
bomb_idx = n - 1
ans = 0

for time in range(MAX_T, 0, -1):
    while bomb_idx >= 0 and get_time_limit(bomb_idx) >= time:
        heapq.heappush(pq, -get_score(bomb_idx))
        bomb_idx -= 1
    
    if pq:
        ans += -heapq.heappop(pq)

print(ans)