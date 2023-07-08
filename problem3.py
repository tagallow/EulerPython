import tools

def solve():
    primes = tools.getPrimes(10000)
    a = 600851475143
    for n in range(2, int(a**.5)):
        if primes.count(n) > 0:
            if a % n == 0:
                print(n)