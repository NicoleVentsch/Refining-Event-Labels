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
#def predecessors(Idlabel, variant):
#    Id = Idlabel[0]
#    firstId = variant[0][0]
#    head = variant[:(Id-firstId)]
#    pred = set(map(itemgetter(1), head)) 
#    return pred

#returns set of successors of a label in a variant
#def successors(Idlabel, variant):
#    Id = Idlabel[0]
#    firstId = variant[0][0]
#    rest = variant[(Id-firstId+1):]
#    succ = set(map(itemgetter(1), rest)) 
#    return succ

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
    for elem2 in successors_list:
        successors.append(set(elem2))
        
    return predecessors, successors

#the costs for the non-matched labels as sum of the number of their predecessors and successors 
def costNoMatch(variant1, variant2, mapping):
    mapped = set(mappings.common_labels(variant1, variant2)) #set of labels that were mapped
    #print("mapped:", mapped)
    unmapped1 = set(map(itemgetter(1), variant1)).difference(mapped) #set of unmapped labels in variant1
    #print("unmapped1:", unmapped1)
    unmapped2 = set(map(itemgetter(1), variant2)).difference(mapped) #set of unmapped labels in variant2
    #print("unmapped2:", unmapped2)
    firstId1 = variant1[0][0]
    firstId2 = variant2[0][0]
    pred1, succ1 = context(variant1)
    pred2, succ2 = context(variant2)
    np1 = 0
    ns1 = 0
    np2 = 0
    ns2 = 0
    for unmapped_label1 in unmapped1:
        positions1 = [x-firstId1 for x in mappings.get_position_label(unmapped_label1, variant1)]
        for p1 in positions1:
            np1 += len(pred1[p1])
            ns1 += len(succ1[p1])
    for unmapped_label2 in unmapped2:
        positions2 = [x-firstId2 for x in mappings.get_position_label(unmapped_label2, variant2)]
        for p2 in positions2:
            np1 += len(pred2[p2])
            ns1 += len(succ2[p2])
    sum = np1+np2+ns1+ns2
    return sum

#the differences in the direct/indirect neighbors of matched pairs
def costMatched(variant1, variant2, mapping):
    firstId1 = variant1[0][0]
    firstId2 = variant2[0][0]
    pred1, succ1 = context(variant1)
    pred2, succ2 = context(variant2)
    sum = 0
    for pair in mapping:
        p1 = pair[0]-firstId1
        p2 = pair[1]-firstId2
        sum += len(pred1[p1])+len(pred2[p2])-len(pred1[p1].intersection(pred2[p2])) #number of distinct predecessors
        print(sum) 
        sum += len(succ1[p1])+len(succ2[p2])-len(succ1[p1].intersection(succ2[p2])) #number of distinct successors
        print(sum)
    return sum  


#given a mapping, returns its cost
def costMapping(wm,ws,wn,variant1,variant2,mapping):
    cost_struc = costStructure(variant1, variant2, mapping)
    cost_nomatch = costNoMatch(variant1, variant2, mapping)
    cost_match = costMatched(variant1, variant2, mapping)
    return wm*cost_match + ws*cost_struc + wn*cost_nomatch


#given a list of possible mappings, returns pair (best mapping, best cost)
def optimalMapping(variant1, variant2, mappings):
    if mappings != []:
        best_mapping = mappings[0]
        cost_best = costMapping(variant1,variant2,best_mapping)
        cost_max = cost_best
        for mapping in mappings:
            cost_new = costMapping(variant1,variant2,mapping)
            if cost_new < cost_best:
                best_mapping = mapping
                cost_best = cost_new
            if cost_new > cost_max:
                cost_max = cost_new
    return best_mapping, cost_best, cost_max
            