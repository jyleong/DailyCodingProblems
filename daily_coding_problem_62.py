'''
Given a 2D matrix of characters and a target word, 
write a function that returns whether the word can 
be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, 
since it's the leftmost column. Similarly, given the 
target word 'MASS', you should return true, since it's the last row.
'''

def word_search(grid, word):
    if len(word) > len(grid) and len(word) > len(grid[0]):
        return false
    first_char = word[0]

    # go through each row in grid
    for i in range(len(grid)):
        try:
            firstIdx = grid[i].index(first_char)
        except ValueError:
            print('No value of {} in this row'.format(first_char))
            continue
        else:
            # search horizontal
            if len(grid[i]) - firstIdx >= len(word): # can search here
                possible_word = grid[i][firstIdx:firstIdx + len(word)]
                if (''.join(possible_word) == word):
                    return True
            # search vertical
            if (len(grid) - i >= len(word)):
                possible_word = []
                for j in range(len(word)):
                    possible_word.append(grid[i+j][firstIdx])
                if (''.join(possible_word) == word):
                    return True
    return False

GRID = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
print('FOAM', word_search(GRID, 'FOAM'))
print('MASS', word_search(GRID, 'MASS'))
print('ABN', word_search(GRID, 'ABN'))
print('FAKE', word_search(GRID, 'FAKE'))


