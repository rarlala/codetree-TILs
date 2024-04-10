a, b = map(int, input().split())
a = a + 2

turn = 2
prev = 1
while a != b:
    turn += 1
    if b - a >= prev + 1:
        a += prev + 1
    elif b - a >= prev:
        a += prev
    else:
        a += prev - 1
    
print(turn)