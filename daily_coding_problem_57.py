'''
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple texts 
such that each text has a length of k or less. You must break it up so that 
words don't break across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that 
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" 
and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
No string in the list has a length of more than 10.
'''

import unittest

def text_justify(words, k):
    if not words:
        return []
    if len(words) < k:
        return [words]

    word_list = words.split()
    curr_count = 0
    result = []
    cur_len = -1
    interm_string = []
    while curr_count < len(word_list):
        w = word_list[curr_count]
        if (len(w) > k):
            raise Exception('Cannot format text with words greater than length: ', k)
        if (cur_len + len(w) + 1 <= k):
            cur_len += len(w) + 1
            interm_string.append(w)
            curr_count += 1
        else:
            result.append(" ".join(interm_string))
            interm_string = []
            cur_len = -1
    result.append(" ".join(interm_string))


    return result




class Justify_Text_Test(unittest.TestCase):
    def test_case_1(self):
        test_case = "the quick brown fox jumps over the lazy dog"
        k = 10
        result = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
        self.assertEqual(text_justify(test_case, k), result)

    def test_case_2(self):

        test_case = test_case = "the quick brown fox jumps over the lazy dog"
        k = 15
        result = ["the quick brown", "fox jumps over", "the lazy dog"]
        self.assertEqual(text_justify(test_case, k), result)

    def test_case_3(self):

        test_case = ["the quick brown fox jumps over the lazy dog"]
        k = 3
        result = ["   "]
        self.assertRaises(Exception, text_justify(test_case, k))





if __name__ == '__main__':

    unittest.main()