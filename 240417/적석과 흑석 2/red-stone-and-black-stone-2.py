# 1~C 번호가 매겨진 빨간돌, 정수 1개 적혀있음 (t)
# 1~N 번호가 매겨진 검정돌, 정수 2개 적혀있음 (a,b)
# a < t < b 를 만족하도록 빨간돌과 검정돌을 1:1로 짝지으려 함
# 최대 1개씩만 짝지어질 수 있음
# 최대 몇 쌍을 할 수 있는지 구하시오

c, n = map(int, input().split())
c_arr = [int(input()) for _ in range(c)]
n_arr = [tuple(map(int, input().split())) for _ in range(n)]
c_arr.sort()
n_arr.sort()

c_idx = 0
n_idx = 0

result = 0
while c_idx < c and n_idx < n:
    a, b = n_arr[n_idx]
    t = c_arr[c_idx]

    if a <= t <= b:
        result += 1
        c_idx += 1
        n_idx += 1

    elif a > t:
        c_idx += 1
    
    elif t > b:
        n_idx += 1
    
print(result)