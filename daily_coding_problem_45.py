'''
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 
(inclusive) with uniform probability, implement a function rand7() 
that returns an integer from 1 to 7 (inclusive).
'''
from random import randint
def rand5():
    return randint(0,4) + 1

def rand7():

    sevens = (rand5() - 1) + (rand5() - 1) * 5
    while(sevens > 21):
        sevens = (rand5() - 1) + (rand5() - 1) * 5
    return (sevens % 7) + 1

for i in range(24):
    print("Test {}: {}".format(i+1, rand7()))

