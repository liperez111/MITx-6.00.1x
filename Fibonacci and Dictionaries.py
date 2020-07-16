def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:3, 2:2}

print(fib_efficient(1,d))