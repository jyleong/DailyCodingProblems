'''
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
'''
from random import randint
from math import ceil, log

def num_rounds_simulation(n):
    if n <= 0:
        return 0
    rounds = 0
    while(n > 1):
        i = 0
        tails = 0
        while(i < n):
            tails += randint(0, 1)
            i += 1
        n -= tails
        rounds += 1
    return rounds

def expected_rounds(n):
    return ceil(log(n, 2))


print('5 coins simulation: {}, expected: {}'.format(num_rounds_simulation(5), expected_rounds(5)))

print('10 coins simulation: {}, expected: {}'.format(num_rounds_simulation(10), expected_rounds(10)))

print('20 coins simulation: {}, expected: {}'.format(num_rounds_simulation(20), expected_rounds(20)))

print('25 coins simulation: {}, expected: {}'.format(num_rounds_simulation(25), expected_rounds(25)))

print('50 coins simulation: {}, expected: {}'.format(num_rounds_simulation(50), expected_rounds(50)))

print('100 coins simulation: {}, expected: {}'.format(num_rounds_simulation(100), expected_rounds(100)))

print('150 coins simulation: {}, expected: {}'.format(num_rounds_simulation(150), expected_rounds(150)))

print('200 coins simulation: {}, expected: {}'.format(num_rounds_simulation(200), expected_rounds(200)))

print('500 coins simulation: {}, expected: {}'.format(num_rounds_simulation(500), expected_rounds(500)))

print('1000 coins simulation: {}, expected: {}'.format(num_rounds_simulation(1000), expected_rounds(1000)))



