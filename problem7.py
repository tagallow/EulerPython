import tools

def solve():
    primes = tools.prime_sieve(200000)
    count = 0
    for i in range(0, len(primes)):
        if(primes[i] != 0):
            count += 1
            if(count == 10001):
                print(primes[i])
                break


