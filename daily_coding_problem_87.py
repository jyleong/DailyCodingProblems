'''
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
'''
oppositeDict = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}

class Marker(object):
    def __init__(self, val):
        self.val = val
        self.neighbours = {
            'N': set(),
            'S': set(),
            'E': set(),
            'W': set()
        }

class Grid(object):

    def check_rule(self, m_1, dir, m_2):
        return m_1 in m_2.neighbours[dir] or m_2 in m_1.neighbours[oppositeDict[dir]]

    def check_opposing_rule(self, m_1, dir, m_2):
        return m_2 in m_1.neighbours[dir] or m_1 in m_2.neighbours[oppositeDict[dir]]

    def add_rule(self, m_1, dir, m_2):
        for c in dir:
            if self.check_opposing_rule(m_1, c, m_2):
                raise Exception('{} already in {} at opposing direction: {} Invalid rule'.format(m_1.val, m_2.val, c))
            for marker in m_1.neighbours[c]:
                    self.add_rule(marker, c, m_2)

        for c in dir:
            if (self.check_rule(m_1, c, m_2)):
                print('{} already in {} at direction: {}'.format(m_1.val, m_2.val, c))
                continue
            m_2.neighbours[c].add(m_1)
            print('{} add {} to {}'.format(m_2.val, m_1.val,c))
            m_1.neighbours[oppositeDict[c]].add(m_2)
            print('{} add {} to {}'.format(m_1.val, m_2.val,oppositeDict[c]))

A = Marker('A')
B = Marker('B')
C = Marker('C')

g1 = Grid()
g1.add_rule(A, 'NW', B)
g1.add_rule(A, 'N', B)

# g = Grid()
# g.add_rule(A, 'N', B)
# g.add_rule(B, "NE", C)
# g.add_rule(C, 'N', A)





