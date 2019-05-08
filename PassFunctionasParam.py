'''Passing function as a parameter'''
def f(x):
    return x * x

def modify(L,fn):
    for idx,v in enumerate(L):
        L[idx] = fn(v)

L = [2,4,6]
modify(L,f)
print(L)

