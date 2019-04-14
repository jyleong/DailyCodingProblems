import unittest
'''Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
here should be at least one space between each word. Pad extra spaces when necessary so 
that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

def text_justify(word_list, k):
    if not word_list or len(word_list) == 0:
        str = " " * k
        return [str]

    result = []

    curr_list = word_list
    curr_count = 0
    while curr_list:
        if (len(curr_list) == 1):
            padding = " " * (k - len(curr_list[0]))
            result.append(padding + curr_list[0])
            break;
        temp_list = []
        currLen = 0
        while currLen <= k and curr_list:
            first_str_len = len(curr_list[0])
            if (currLen + first_str_len + 1 > k):
                break;
            currLen = currLen + 1 + first_str_len
            temp_list.append(curr_list[0])
            curr_list = curr_list[1:]
        # append to result
        num_spaces = k - len(''.join(temp_list))
        gaps = len(temp_list) - 1
        gap_len = num_spaces // gaps
        gap_first = num_spaces - gap_len * gaps
        rest_words = (' ' * gap_len).join(temp_list[1:])
        firstWordGap = ' ' * (gap_len + gap_first)
        result.append(temp_list[0] + firstWordGap + rest_words)

    return result




class Justify_Text_Test(unittest.TestCase):
    def test_case_1(self):
        test_case = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        k = 16
        result = ["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"]
        self.assertEqual(text_justify(test_case, k), result)

    def test_case_2(self):

        test_case = ["the"]
        k = 10
        result = ["       the"]
        self.assertEqual(text_justify(test_case, k), result)

    def test_case_3(self):

        test_case = []
        k = 3
        result = ["   "]
        self.assertEqual(text_justify(test_case, k), result)





if __name__ == '__main__':

    unittest.main()