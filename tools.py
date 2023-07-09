# Description: This file contains functions that are used in other files.

# getPrimes: returns a list of all prime numbers up to n
def getPrimes(n):
    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes

# isPrime: returns true if n is prime, false otherwise
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i == 0:
            return False    
    return True

def SieveEratosthenes(max):
    primes = []
    for i in range(2, max + 1):
        primes.append(i)
    for i in range(0, len(primes)):
        if primes[i] != 0:
            for j in range(i + primes[i], len(primes), primes[i]):
                primes[j] = 0
    return primes