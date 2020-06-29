def oddTuples(aTup):
    a = ()
    b = 0
    for i in aTup:
        if b%2 == 0:
            a = a + (i,)
            b += 1
        else:
            b += 1
    return a

print(oddTuples((1,2)))