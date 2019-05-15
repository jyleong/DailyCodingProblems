import unittest

def collision(speed, pos):
    # Write your code here
    count = 0

    for i in range(len(speed)):
        if (i == pos):
            continue
        cur_posi = i
        pos_posi = pos

        if (cur_posi > pos_posi):
            if (speed[pos] > speed[i]): # has potential to pass, need to find exact collision
                count += 1
        else:
            if (speed[i] > speed[pos]):
                count += 1

    return count


class Collision_Test(unittest.TestCase):
    def test_case_1(self):
        test = [6, 6, 1, 6, 3, 4, 6, 8]
        position = 2
        
        expected = 2
        self.assertEqual(collision(test, position), expected)

    def test_case_2(self):
        test = [2, 1]
        position = 1
        
        expected = 1
        self.assertEqual(collision(test, position), expected)

if __name__ == '__main__':

    unittest.main()

