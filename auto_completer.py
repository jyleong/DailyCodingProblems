'''
Implement an autocomplete system. That is, 
given a query string s and a set of all possible 
query strings, return all strings in the set that 
have s as a prefix.

For example, given the query string de and 
the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a 
more efficient data structure to speed up queries.
'''

ALPHABET_SIZE = 26
class TrieNode(object):

    # use one as the root
    def __init__(self): 
        ## trie nodes
        self.nodes = [None] * ALPHABET_SIZE
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insertTrie(self, string):
        current = self.root
        for c in string:
            index = ord(c) - ord('a')
            if (not current.nodes[index]):
                current.nodes[index] = TrieNode()
            # if present go to next char
            current = current.nodes[index]
        # how to mark end of word
        current.endOfWord = True

    def searchWord(self, string):
        current = self.root
        for c in string:
            index = ord(c) - ord('a')
            if (not current.nodes[index]):
                return False
            current = current.nodes[index]
        return current and current.endOfWord

    # returns list of matching strings
    def auto_complete_search(self, pre):

        tempNode = self.root
        temp_word = ''
        for c in pre:
            index = ord(c) - ord('a')
            if (not tempNode.nodes[index]):
                print('no suggestions')
                return
            temp_word += c
            tempNode = tempNode.nodes[index]

        emptyChildren = all(v is None for v in tempNode.nodes)
        if tempNode.endOfWord and emptyChildren:
            print('no other suggetions')
            return

        result = []
        def auto_suggest(node, word):
            if node.endOfWord:
                result.append(word)

            for i in range(len(node.nodes)):
                if node.nodes[i]:
                    new_word = word + chr(i + ord('a'))
                    auto_suggest(node.nodes[i], new_word)
        auto_suggest(tempNode, temp_word)
        for word in result:
            print(word)
        return


# trie implementation

# function to dump to tree

words = ['deal', 'deer', 'dog']
rootTrie = Trie()

for word in words:
    rootTrie.insertTrie(word)

# finish loading dictionary

test_1 = 'de' 
# -> deal, deer
test_2 = 'd'
# -> deal, deer, dog

print('search test: ')
for word in words:
    print('searching {} is {}'.format(word, rootTrie.searchWord(word)))

print('auto complete test')

rootTrie.auto_complete_search(test_1)
rootTrie.auto_complete_search(test_2)