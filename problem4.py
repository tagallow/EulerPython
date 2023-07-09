def solve():
    max = 0
    for n in range(100, 1000):
        for m in range(100, 1000):
            if str(n*m) == str(n*m)[::-1]:
                if(n*m > max):
                    max = n*m
    print(max)