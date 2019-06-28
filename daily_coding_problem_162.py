'''
Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f

'''

class TrieNode(object):

    def __init__(self):
        self.visit_count = 1
        self.letter_nodes = [None] * 26
        self.end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def add_word(self, word):
        node = self.root
        for char in word:
            idx = self._char_to_index(char)

            if node.letter_nodes[idx] is None:
                node.letter_nodes[idx] = TrieNode()
            else:
                node.letter_nodes[idx].visit_count += 1
            node = node.letter_nodes[idx]
        node.end_of_word = True

    def get_prefix(self, word):
        if not word or len(word) == 0:
            return ""
        result = ""
        node = self.root
        length = len(word)
        # print('at word: ', word)
        for i in range(len(word)):
            idx = self._char_to_index(word[i])
            # print('word: {} idx: {}, char: {}'.format(word, idx, word[i]))
            if node.letter_nodes[idx].visit_count == 1:
                # print('freq is 1: word: {} idx: {}, char: {}'.format(word, idx, word[i]))
                result = word[:i+1]
                return result
            node = node.letter_nodes[idx]
                
        return result

def test(words):
    trie = Trie()
    for w in words:
        trie.add_word(w)
        
    result = []
    for w in words:
        result.append(trie.get_prefix(w))
    return result
print(test(["dog", "cat", "apple", "apricot", "fish"]))

assert test(["dog", "cat", "apple", "apricot", "fish"]) == \
    ["d", "c", "app", "apr", "f"]
            

