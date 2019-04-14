'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

Implement car and cdr.
'''

def cons(a, b):
    # def pair(f):
    #     return f(a, b)
    # return pair
    return lambda f: f(a,b)

def mult(f):
    def prod(a,b):
        return a*b
    return f(prod)
    # return f(lambda a,b: a * b)

print('Test cons')
print(cons(3,4))
def car(f):
    # def first(a, b):
    #     return a
    # return f(first)
    return f(lambda a,b: a)

def cdr(f):
    # def second(a, b):
    #     return b
    # return f(second)
    return f(lambda a,b: b)

print('Test mult')
print(mult(cons(5,4)))


print('Test car')
print(car(cons(3,4)))

print('Test cdr')
print(cdr(cons(3,4)))