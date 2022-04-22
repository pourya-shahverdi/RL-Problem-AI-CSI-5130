#!/usr/bin/env python
from math import gamma

alpha = 0.5
gamma = 0.5

all_states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'O']
all_actions = ['r', 'l', 'u', 'd', 'e']

# episode1 = [['A', 'r', 'B', 1], 
#             ['B', 'r', 'C', -10],
#             ['C', 'd', 'D', -10],
#             ['D', 'd', 'E', 50]]

# episode2 = [['A', 'r', 'B', 1],
#             ['B', 'l', 'A', 1],
#             ['A', 'r', 'B', 1],
#             ['B', 'r', 'C', -10],
#             ['C', 'd', 'D', -10],
#             ['D', 'd', 'E', 50]]

# episode3 = [['A', 'd', 'H', 1], 
#             ['H', 'd', 'G', 1],
#             ['G', 'r', 'F', 1],
#             ['F', 'r', 'E', 1]]

# episode4 = [['A', 'd', 'H', 1], 
#             ['H', 'u', 'A', 1],
#             ['A', 'd', 'H', 1],
#             ['H', 'd', 'G', 1],
#             ['G', 'u', 'H', 1],
#             ['H', 'd', 'G', 1],
#             ['G', 'r', 'F', 1],
#             ['F', 'l', 'G', 1],
#             ['G', 'r', 'F', 1],
#             ['F', 'r', 'E', 1]]

episodes = [[['A', 'r', 'B', 1], 
             ['B', 'r', 'C', -10],
             ['C', 'd', 'D', -10],
             ['D', 'd', 'E', 50]],
            [['A', 'r', 'B', 1],
             ['B', 'l', 'A', 1],
             ['A', 'r', 'B', 1],
             ['B', 'r', 'C', -10],
             ['C', 'd', 'D', -10],
             ['D', 'd', 'E', 50]],
            [['A', 'd', 'H', 1], 
             ['H', 'd', 'G', 1],
             ['G', 'r', 'F', 1],
             ['F', 'r', 'E', 1]],
            [['A', 'd', 'H', 1], 
             ['H', 'u', 'A', 1],
             ['A', 'd', 'H', 1],
             ['H', 'd', 'G', 1],
             ['G', 'u', 'H', 1],
             ['H', 'd', 'G', 1],
             ['G', 'r', 'F', 1],
             ['F', 'l', 'G', 1],
             ['G', 'r', 'F', 1],
             ['F', 'r', 'E', 1]]]

V = {state : 0 for state in all_states}

k = 0
for episode in episodes:
    for samples in episode:
        oldV = V.copy()
        for state in samples[0]:
            for action in samples[1]:
                for successor in samples[2]:
                    reward = samples[3]
                    V[state] = (1-alpha)*oldV[state] + (alpha * (reward + gamma * V[successor]))
                    print('Value of States:',V)
                    print('Value of',successor,'as the successor for',state,'is:',V[successor])