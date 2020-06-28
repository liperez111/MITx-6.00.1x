def gcdIter(a, b):
    n = min([a,b])
    while n > 0:
        if a%n == 0 and b%n ==0:
            return n
            break
        else:
            n -= 1