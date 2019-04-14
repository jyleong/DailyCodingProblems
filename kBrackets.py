import unittest

def k_brackets(brackets):
    if not isinstance(brackets, str) or len(brackets) == 0:
        return 0
    leftParen = 0
    rightParen = len(brackets) - 1
    while (leftParen <= rightParen):
        if brackets[leftParen] != '(':
            leftParen = leftParen + 1
        elif brackets[rightParen] != ')':
            rightParen = rightParen - 1
        else:
            leftParen = leftParen + 1
            rightParen = rightParen - 1
    return leftParen


class BracketsTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(k_brackets(''), 0)

    def test_pass_none(self):
        self.assertEqual(k_brackets(None), 0)

    def test_1(self):
        self.assertEqual(k_brackets('(())))('), 4)

    def test_2(self):
        self.assertEqual(k_brackets(')())('), 3)

    def test_3(self):
        self.assertEqual(k_brackets('(()()'), 2)

    def test_4(self):
        self.assertEqual(k_brackets(')))))))))'), 9)

    def test_5(self):
        self.assertEqual(k_brackets('(((((((((((('), 0)

    def test_6(self):
        self.assertEqual(k_brackets(')('), 1)




if __name__ == '__main__':
    unittest.main()

