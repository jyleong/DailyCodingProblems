'''
Find an efficient algorithm to find the smallest distance (measured in number of words) 
between any two given words in a string.

For example, given words "hello", and "world" and a text content of 
"dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" 
in between the two words.
'''

import unittest

def smallest_distance(text, word_1, word_2):
    if len(text) == 0:
        return -1
    words = text.split(" ")
    w1_idx = -1
    w2_idx = -1
    min_dist = -1
    for i in range(len(words)):
        if words[i] == word_1:
            w1_idx = i
            if w2_idx != -1:
                if min_dist == -1:
                    min_dist = abs(w1_idx - w2_idx) - 1
                else:
                    min_dist = math.min(abs(w1_idx - w2_idx), min_dist)
        if words[i] == word_2:
            w2_idx = i
            if w1_idx != -1:
                if min_dist == -1:
                    min_dist = abs(w1_idx - w2_idx) - 1
                else:
                    min_dist = math.min(abs(w1_idx - w2_idx) - 1, min_dist)
    return min_dist

class DailyCodingProblemsTest(unittest.TestCase):

    def test_case_1(self):
        text = "dog cat hello cat dog dog hello cat world"
        word_1 = 'hello'
        word_2 = 'world'
        result = 1
        
        self.assertEqual(smallest_distance(text, word_1, word_2), result)

    def test_case_2(self):
        text = "dog cat hello cat dog dog hello cat world"
        word_1 = 'text'
        word_2 = 'world'
        result = -1
        
        self.assertEqual(smallest_distance(text, word_1, word_2), result)

    def test_case_3(self):
        text = ""
        word_1 = 'hello'
        word_2 = 'world'
        result = -1
        
        self.assertEqual(smallest_distance(text, word_1, word_2), result)

    def test_case_4(self):
        text = "dog cat hello cat dog dog hello cat world star"
        word_1 = 'star'
        word_2 = 'world'
        result = 0
        
        self.assertEqual(smallest_distance(text, word_1, word_2), result)


if __name__ == '__main__':
    unittest.main()