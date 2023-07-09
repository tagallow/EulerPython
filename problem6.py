def solve():
    print(squareSum(100) - sumSquares(100))

def sumSquares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

def squareSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum * sum