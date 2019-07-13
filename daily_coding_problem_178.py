'''
Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. 
Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? 
Write a program to simulate the two games and calculate their expected value.
'''

from random import randint
def count_rolls(dice_choices):
    prev = False
    end = False
    count = 0
    roll = randint(1, 6)
    while True:
        next = randint(1, 6)
        count += 1
        if roll == dice_choices[0] and next == dice_choices[1]:
            return count

        roll = next 
    

def simulate(times, dice_choices):
    total_count = 0
    for i in range(times):
        total_count += count_rolls(dice_choices)
    return total_count // times

simulate_1 = simulate(100000, (5, 5)) 
print('5-5: ', simulate_1)

simulate_2 = simulate(100000, (5, 6)) 
print('5-6: ', simulate_2)
assert simulate_2 < simulate_1

