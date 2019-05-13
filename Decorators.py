#@Decorators In python
''' A decorator takes a function, Adds some functionality and returns it.
This is also called metaprogramming as a part of the program tries to modify another program at the compile time.'''

def smart_divide(func):
    def inner(a,b):
        print("i am going to divide",a,"and ",b)
        if b == 0:
            Print("Opps! Cannot divide")
            return
        print('1')
        return func(a,b)
    print('2')
    return inner

@smart_divide
def divide(a,b):
    print('3')
    return a/b


print(divide(2,5))

#Result:
#2
#i am going to divide 2 and  5
#1
#3
#0.4

print('MULTIPLE DECORATORS: function can be decorated multiple times with different or same decorators.')
def star(func):
    def inner(*args,**kwargs):
        print("*" *30)
        func(*args,**kwargs)
        print("*" *30)
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print("%" *30)
        func(*args,**kwargs)
        print("%" *30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

#Result:
#******************************
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Hello
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#******************************

