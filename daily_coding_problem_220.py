'''
In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.

'''

import unittest

def get_max_coins(coins):
    if not coins or len(coins) == 0:
        return 0
    max_score = 0
    first_play = True
    while coins and len(coins) > 0:

        left = coins[0]
        right = coins[-1]
        if left > right:
            max_num = left
            coins = coins[1:]
        else:
            max_num = right
            coins = coins[:-1]
        if first_play:
            max_score += max_num
        first_play = not first_play
    return max_score


class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        coins = [5, 4, 2, 3, 1, 6]
        expected = 13
        self.assertEqual(expected, get_max_coins(coins))

    def test_case_2(self):
        coins = [1, 2, 3, 4, 5, 6]
        expected = 12
        self.assertEqual(expected, get_max_coins(coins))

    def test_case_3(self):
        coins = []
        expected = 0
        self.assertEqual(expected, get_max_coins(coins))

    def test_case_4(self):
        coins = [9, 4, 6, 3, 5, 7]
        expected = 20
        self.assertEqual(expected, get_max_coins(coins))

    def test_case_5(self):
        coins = [5, 3, 7]
        expected = 10
        self.assertEqual(expected, get_max_coins(coins))

    def test_case_6(self):
        coins = [6]
        expected = 6
        self.assertEqual(expected, get_max_coins(coins))

if __name__ == '__main__':

    unittest.main()
