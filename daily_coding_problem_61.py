'''This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, 
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''
import math

def pow(x,y):
    if y == 0:
        return 1
    newY = math.floor(y/2)
    val = pow(x,newY)
    if y % 2 == 0:
        return val * val
    else:
        return x * val * val

print('Test 2^10: ', pow(2,10))

print('Test 5^2: ', pow(5,2))

print('Test 3^3: ', pow(3,3))