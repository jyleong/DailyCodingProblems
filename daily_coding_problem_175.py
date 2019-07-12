'''
You are given a starting state start, a list of transition probabilities for a Markov chain, 
and a number of steps num_steps. Run the Markov chain starting from start for num_steps and 
compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.

'''
from random import uniform
from bisect import bisect
import unittest

def init_state(state_transitions):
    result_state = dict()
    for s in state_transitions:
        if s[0] not in result_state:
            result_state[s[0]] = ([],[])
        result_state[s[0]][0].append(s[1])
        if not result_state[s[0]][1]:
            result_state[s[0]][1].append(s[2])
        else:
            prev_prob = result_state[s[0]][1][-1]
            result_state[s[0]][1].append(prev_prob + s[2])
    return result_state

def init_counter(state_transitions):
    counter = dict()
    for s in state_transitions:
        counter[s[0]] = 0
    return counter

def next_state(state_mapping, cur_state):
    r = uniform(0, 1)
    state_tuple = state_mapping[cur_state]
    idx = bisect(state_tuple[1], r)
    return state_tuple[0][idx]

def markov_chain(state_transitions, steps):
    initial_state = init_state(state_transitions)
    counter = init_counter(state_transitions)

    cur_state = state_transitions[0][0]
    for s in range(steps):
        counter[cur_state] += 1

        cur_state = next_state(initial_state, cur_state)

    
    return counter

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        states = [
          ('a', 'a', 0.9),
          ('a', 'b', 0.075),
          ('a', 'c', 0.025),
          ('b', 'a', 0.15),
          ('b', 'b', 0.8),
          ('b', 'c', 0.05),
          ('c', 'a', 0.25),
          ('c', 'b', 0.25),
          ('c', 'c', 0.5)
        ]
        steps = 5000
        result = markov_chain(states, steps)
        print('markov results: ', result)
        self.assertTrue(result['a'] > result['b'])
        self.assertTrue(result['a'] > result['c'])
        self.assertTrue(result['b'] > result['c'])

if __name__ == '__main__':

    unittest.main()




        