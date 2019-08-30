'''

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
'''

def collatz_sequence(n):
    if n <= 0:
        raise ValueError('Input must be a positive integer')
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def simulation():
    longest = -1
    num = 0
    for i in range(1, 1000001):
        times = collatz_sequence(i)
        if times > longest:
            longest = times
            num = i
        longest = max(longest, times)
    return num, longest


print('Running collatz sequence from 1 to 1000000!!!')
num, longest = simulation()
print('Longest sequence is: {} with {} times'.format(num, longest))
