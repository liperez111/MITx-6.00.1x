def f(s):
    return 'a' in s

def satisfiesF(L):

    u = L.copy()
    for i in u:
        if f(i) == False:
            L.remove(i)

    return len(L)

L = ['a', 'b', 'a','a','a','c','a','p','w','c','a','p','w','a', 'b', 'a','a','a','c','a','p','w','c','a','p','w','a', 'b', 'a','a','a','c','a','p','w','c','a','p','w','a', 'b', 'a','a','a','c','a','p','w','c','a','p','w']
print(satisfiesF(L))
print(L)











