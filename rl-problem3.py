#!/usr/bin/env python
from re import S
import numpy as np
from math import gamma


alpha = 0.5
gamma = 1

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
q_value = {{state : 0 for state in all_states}, {action : 0 for action in all_actions}}


k = 0
# while k < 2:
for episode in episodes:
    old_q_value = q_value.copy()
    for samples in episode:
        oldV = V.copy()
        for state in samples[0]:
            for action in samples[1]:
                for successor in samples[2]:
                    reward = samples[3]
                    V[state] = (1-alpha)*oldV[state] + (alpha * (reward + gamma * V[successor]))

    # k += 1