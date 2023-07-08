def solve():
    a = 1
    b = 1
    c = 0
    sum = 0
    for n in range(100):
        if c % 2 == 0:
            sum += c
        c = a + b
        a = b
        b = c
        if(c > 4000000):
            break
        
    print(sum)