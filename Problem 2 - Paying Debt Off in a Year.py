b = balance = 3926
mir = .2 / 12

n = 0
ip = 10


while b > 0:

    ip += 10
    b= balance
    while n < 12:
        b = b - ip
        b = b + mir*b
        n += 1
    n = 0

print(ip)
