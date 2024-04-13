import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []
result = 0

for elem in arr:
    heapq.heappush(heap, elem)

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    value = a + b
    result += value
    heapq.heappush(heap, value)

print(result)