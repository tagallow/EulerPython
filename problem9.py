def solve():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if(isPythTriple(a, b, c)):
                    if(a + b + c == 1000):
                        print(a*b*c)
                        return

def isPythTriple(a, b, c):
    valid = True
    if a > b:
        valid = False
    if b > c:
        valid = False
    if a > c:
        valid = False
    if(valid):
        valid = (a**2 + b**2 == c**2)
    return valid