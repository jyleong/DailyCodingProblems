"""
This problem was asked by Dropbox.

Given a list of words, determine whether the words can be chained to form a circle. 
A word X can be placed in front of another word Y in a circle if the last character 
of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', 'touch', 'tunic'] can form the 
following circle: chair --> racket --> touch --> height --> tunic --> chair.
"""

def build_word_graph(word_list):
    graph = {}
    for w in word_list:
        first = w[0]
        if first not in graph:
            graph[first] = set()
        graph[first].add(w)
    return graph

def is_valid(current_char, remaining_set, current_circle, word_graph):
    # Base cases
    if not remaining_set and current_char == current_circle[0][0]:
        return True

    if current_char not in word_graph or not word_graph[current_char]:
        return False

    # Recur over conditions of multiple valid word options
    for word in word_graph[current_char]:
        if word not in remaining_set:
            continue
        remaining_set.remove(word)
        current_circle.append(word)
        next_char = word[-1]
        if not is_valid(next_char, remaining_set, current_circle, word_graph):
            remaining_set.add(word)
            current_circle = current_circle[:-1]
        else:
            return True
    return False


def circular_words(word_list): 
    graph = build_word_graph(word_list)
    word_set = set(word_list)
    for word in word_set:
        curr_char = word[-1]
        if is_valid(curr_char, word_set - {word}, [word], graph):
            return True

    return False

test_1 = ['chair', 'height', 'racket', 'touch', 'tunic']
test_2 = ['chair', 'height', 'racket', 'perfect', 'touch', 'tunic']
test_3 = ['abc', 'cb', 'bca']

assert circular_words(test_1)
assert not circular_words(test_2)
assert circular_words(test_3)
