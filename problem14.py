def solve():
    max = 0
    max_i = 0
    for i in range(1, 1000000):
        count = 1
        n = i
        while n != 1:
            n = collatz(n)
            count += 1
        if count > max:
            max = count
            max_i = i
    print(max_i)

def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1