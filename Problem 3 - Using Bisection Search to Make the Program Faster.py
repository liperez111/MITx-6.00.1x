balance = 320000
mir = .2 / 12
b= 1000
n = 0
lo = balance / 12
up = (balance*(1+ mir)**12)/12
c = 1000

while abs(b-0) > .00001:

    ip = (lo + up) / 2
    b = balance
    while n < 12:
        b = b - ip
        b = b + mir * b
        n += 1
    n = 0

    if b <= 0:
        up = ip
    elif b >= 0:
        lo = ip


print(round(ip,2))




