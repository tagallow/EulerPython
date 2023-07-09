def solve():
    valid = True
    for m in range(132792561,232792561):
        for n in range(1,20):
            if m % n > 0:
                valid = False
                break
        if valid:
            print(m)
            break
        else:
            valid = True
