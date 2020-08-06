"""
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""

class NumPad(object):
    def __init__(self):
        self.used = [False] * 9

    def is_valid(self, current: int, next: int) -> bool:
        # starting position
        if current == -1: return True
        # vertical/horizontal/horse pattern
        elif (abs(next-current) % 2 == 1):
            return True
        # vertical two hops
        elif (abs(next-current) == 6 and self.used[(next+current)//2]):
            return True
        # horizontal two hops
        elif (abs(next-current) == 2 and (next+current) % 6 == 2
            and self.used[(next+current)//2]):
            return True
        # diagonal two hops
        elif ((next + current) == 8 and current%2 == 0 and self.used[4]):
            return True
        # diagonal one hop
        elif (abs(next-current) == 4 and (next + current) != 8):
            return True
        elif (abs(next-current) == 2 and (next + current) % 6 != 2):
            return True
        else:
            return False

    def total_patterns(self, m, n) -> int:
        result = 0
        for i in range(m, n+1):
            result += self.calc_patterns(position=-1, remaining=i)
        return result

    def calc_patterns(self, position: int, remaining: int) -> int:
        if remaining == 0:
            return 1
        result = 0
        for i in range(0, 9):
            if not self.used[i] and self.is_valid(current=position, next=i):
                self.used[i] = True
                result += self.calc_patterns(position=i, remaining=remaining-1)
                self.used[i] = False
        return result

if __name__ == '__main__':

    num_pad = NumPad()
    print('Total patterns between 3 and 6 keys %s' % num_pad.total_patterns(3, 6))
    print('Total patterns between 2 and 4 keys %s' % num_pad.total_patterns(2, 4))
    print('Total patterns between 1 and 2 keys %s' % num_pad.total_patterns(1, 2))
