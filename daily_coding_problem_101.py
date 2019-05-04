'''
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
'''

def prime_sum(n):
    prime_arr = sieve_primes(n)
    for i in range(n):
        if (prime_arr[i] and prime_arr[n-i]):
            return (i, n-i)

def sieve_primes(n):
    prime_arr = [True]*n
    prime_arr[0] = False
    prime_arr[1] = False
    p = 2
    while(p*p <= n):
        i = p*p
        while(i < n):
            prime_arr[i] = False
            i += p
        p += 1
    return prime_arr

print("prime sum of 82: ", prime_sum(82))

print("prime sum of 14: ", prime_sum(14))

print("prime sum of 4: ", prime_sum(4))

print("prime sum of 764: ", prime_sum(764))





    

