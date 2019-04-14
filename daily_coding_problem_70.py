'''
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''
import unittest

def n_perfect_num(n):
    # starting num at 19
    count = 0
    i = 19
    print(n, "test case")
    while(count < n):
        print("count: ", count)
        candidate = i
        sum = 0
        while(candidate != 0):
            sum += candidate%10
            candidate = int(candidate/10)
        if sum == 10:
            count += 1
        if (count == n): return i
        i += 9
    return i
    


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        case = 2
        
        expected = 28
        self.assertEqual(n_perfect_num(case), expected)

    def test_case_2(self):

        case = 1
        
        expected = 19
        self.assertEqual(n_perfect_num(case), expected)

    def test_case_3(self):

        case = 9
        
        expected = 91
        self.assertEqual(n_perfect_num(case), expected)

    def test_case_4(self):

        case = 11
        
        expected = 118
        self.assertEqual(n_perfect_num(case), expected)

if __name__ == '__main__':

    unittest.main()
