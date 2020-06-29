'''
L6 Problem 2
------------
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
where every other element of the input tuple is copied, starting with the first one.
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

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