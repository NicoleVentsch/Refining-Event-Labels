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

#returns a pair (x,y) where x and y are lists, and x[i] is the set of predecessors of label on position i and y[i] the set of successors of label on position i
def context(variant):
    predecessors_list = []
    successors_list = []
    predecessors = []
    successors = []
    empty = []
    rest = list(map(itemgetter(1), variant[1:]))
    predecessors_list.insert(0,empty)
    successors_list.insert(0,rest)
    for index in range(1,len(variant)):
        pred_before = predecessors_list[index-1]
        succ_before = successors_list[index-1]
        last_label = [variant[index-1][1]]
        current_label = variant[index][1]
        #predecessors of current label are the predecessors of the last label plus last label
        predecessors_list.insert(index, pred_before + last_label)
        s_temp = succ_before.copy()
        s_temp.remove(current_label)
        #successors of current label are the successors of the last label minus current label
        successors_list.insert(index, s_temp) 
    for elem in predecessors_list:
        predecessors.append(set(elem))
        successors.append(set(elem))
        
    return predecessors, successors