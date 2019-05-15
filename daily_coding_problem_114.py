'''
Given a string and a set of delimiters, 
reverse the words in the string while maintaining the 
relative order of the delimiters. For example, 
given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the 
following cases: "hello/world:here/", "hello//world:here"
'''

import unittest

def reverse_words(words, delimiters):
    if not words or len(words) == 0:
        return ""
    i = 0
    start = 0
    delimiter_list = []
    delimiter_indexes = []
    word_list = []
    while(i < len(words)):
        c = words[i]

        if c in delimiters:
            w = words[start:i]
            if len(w) >= 1:
                word_list.append(w)
            start = i + 1
            delimiter_list.append(c)
            delimiter_indexes.append(len(word_list) + len(delimiter_list)-1)

        i += 1

    if (i - start) > 1:
        word_list.append(words[start:i])
    # end of first while loop
    word_list.reverse()
    # for each word, fill in with delimiters
    reversed_string = ""
    word_index = 0
    delim_index = 0

    # merging the reversed words and the delimiters
    for i in range(len(word_list) + len(delimiter_list)):
        if delim_index < len(delimiter_indexes) and delimiter_indexes[delim_index] == i:
            # insert next delimiter if the position is saved for a delimiter
            reversed_string += delimiter_list[delim_index]
            delim_index += 1
        else:
            reversed_string += word_list[word_index]
            word_index += 1

    return reversed_string

class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        words = 'hello/world:here'
        delimiters = set(['/', ':'])
        expected = 'here/world:hello'
        self.assertEqual(reverse_words(words, delimiters), expected)

    def test_case_2(self):
        words = 'hello/world:here/'
        delimiters = set(['/', ':'])
        expected = 'here/world:hello/'
        self.assertEqual(reverse_words(words, delimiters), expected)

    def test_case_3(self):
        words = 'hello//world:here'
        delimiters = set(['/', ':'])
        expected = 'here//world:hello'
        self.assertEqual(reverse_words(words, delimiters), expected)

if __name__ == '__main__':

    unittest.main()