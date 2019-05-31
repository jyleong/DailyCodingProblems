'''
Given a real number n, find the square root of n.
For example, given n = 9, return 3.

'''
TOLERANCE_VAL = 10 ** -5

def tol(n1, n2):
    return abs(n1-n2) < TOLERANCE_VAL

def square_root(n):
    if not n:
        return n
    if n < 0:
        print('Can not square root a negative number')
        return
    return sqrt_helper(n, 0, n)

def sqrt_helper(num, start, end):
    mid = start + ((end-start)/2)
    guess = mid * mid
    if tol(guess, num):
        return mid

    if (guess > num):
        return sqrt_helper(num, start, mid)
    else:
        return sqrt_helper(num, mid, end)




print('Square root 9: ', square_root(9))
print('Square root 10: ', square_root(10))
print('Square root 25: ', square_root(25))
print('Square root 38: ', square_root(38))

print('Square root 49: ', square_root(49))

print('Square root 2: ', square_root(2))
print('Square root 100: ', square_root(100))

print('Square root 225: ',square_root(225))
print('Square root 300: ', square_root(300))
print('Square root 10000: ', square_root(10000))

