'''
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 
1 and k (inclusive), where k is an input, write a function that shuffles 
a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''
from random import randint

def random_k(k):
    return randint(0,k)

'''
inputs array of cards, easy case just int array
and k int
'''

def shuffle_deck(deck, k):
    for i in range(len(deck)):
        card_idx = random_k(k)
        # swap
        temp = deck[i]
        deck[i] = deck[card_idx]
        deck[card_idx] = temp
    return deck

NUM_CARDS = 52
cards_arr = []
for i in range(NUM_CARDS):
    cards_arr.append(i+1)

print(cards_arr)

print('Shuffle test 1')

print(shuffle_deck(cards_arr, NUM_CARDS-1))

print('Shuffle test 2')

print(shuffle_deck(cards_arr, NUM_CARDS-1))