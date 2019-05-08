''' functional programming
Python: Lambda, Map, Filter, Reduce Functions.
sample functions can be embeed in the code.
'''
#Lambda: 1 line functional. Donot use def or return keyword.
print('Simple function ')
# x is the paramter and alter : is the definition of the function.
val = lambda x:x*2
print(val(2))
print(' Lambda with 2 paramters ')
val = lambda x,y:x+y
print(val(2,5))
print(' Lambda with IF ')
val = lambda x,y: x if x > y else y
print(val(2,5))
print("type of the lambda object.")
print(type(val))
print(' Lambda with  Default paramters ')
val = lambda y = "Kandhati",x = "Hello" : x + ' ' + y
print(val("Thulasi",))
print('List Lambda')
l = [lambda x:x*2,lambda x:x*3,lambda x:x*4]
for i in l:
    print(i(2))
print(l[0](3))

#also can be written as
def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4
# Reference by name
L = [f1, f2, f3]
for f in L:
    print(f(3))
print('Nested lambda')
def sums(x):
    return (lambda xval:xval + x)
val = sums(100)
print(val(99))
action = (lambda x: (lambda newx: x + newx))
val = action(200)
print(val(99))
print("sorted")
death = [
    ('James', 'Dean', 24),
    ('Jimi', 'Hendrix', 27),
    ('George', 'Gershwin', 38),]
print(sorted(death, key=lambda age: age[2]))