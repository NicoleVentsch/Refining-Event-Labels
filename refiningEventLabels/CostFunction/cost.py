# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:37:12 2019

@author: Bianka
"""

import mappings
from itertools import combinations
from operator import itemgetter
#sum of the differences in the distances between each matched pair and other matches pairs 
def costStructure(variant1, variant2, mapping):
    cost_structure = 0
    combis = list(combinations(mapping, 2)) 
    for (pair1, pair2) in combis:
            distance1 = abs(pair1[0] - pair2[0])
            distance2 = abs(pair1[1] - pair2[1])
            cost_structure += abs(distance1 - distance2)/2
    return cost_structure


#returns set of predecessors of a label in a variant
def predecessors(Idlabel, variant):
    Id = Idlabel[0]
    firstId = variant[0][0]
    head = variant[:(Id-firstId)]
    pred = set(map(itemgetter(1), head)) 
    return pred


#returns set of successors of a label in a variant
def successors(Idlabel, variant):
    Id = Idlabel[0]
    firstId = variant[0][0]
    rest = variant[(Id-firstId+1):]
    succ = set(map(itemgetter(1), rest)) 
    return succ

#returns list of predecessors and list of successors for each label in a variant
def context(variant):
    predecessors = []
    successors = []
    em = set()
    rest = set(list(map(itemgetter(1), variant[1:])))
    predecessors.insert(0,em)
    successors.insert(0,rest)
    for index in range(1,len(variant)):
        #print(successors[index-1])
        last_label = set((variant[index-1][1], ))
        current_label = variant[index][1]
        #print("CCCCCCCCCCC: ", current_label)
        predecessors.insert(index, predecessors[index-1].union(last_label))#join last label
        succ_before = list(successors[index-1])
       # s = succ_before.remove(current_label) BUGGG
        successors.insert(index, s) #remove current label
    return predecessors, successors