#!/usr/bin/env python
from math import gamma


alpha = 0.5
gamma = 1

all_states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'O']
all_actions = ['r', 'l', 'u', 'd', 'e']

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

Qmax = {}
Q = {}
for state in all_states:
    for action in all_actions:
        Qmax[state,action] = 0
        Q[state,action] = 0

k = 0
while k < 54:
    for episode in episodes:
        for samples in episode:
            Old_Q = Q.copy()
            for state in samples[0]:
                for action in samples[1]:
                    for successor in samples[2]:
                        reward = samples[3]
                        Q[state,action] = (1-alpha)*Old_Q[state,action] + alpha*(reward + gamma * Qmax[successor,action])
                        for act in all_actions:
                            if Q[state,act] > Qmax[state,action]:
                                Qmax[state,action] = Q[state,act]
                    print(Q)
    k += 1