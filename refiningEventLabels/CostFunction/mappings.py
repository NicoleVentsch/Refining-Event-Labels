# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:25:10 2019

@author: Bianka
"""

import itertools  as it 

#Args: variants is a list of lists
#Returns: list of list of tuples having (ID,Event) where each ID is unique
def createEventIDs(variants=[]):
    seq = it.count()
    return [[(next(seq),event) for event in variant] for variant in variants]


#Args: two variants as a list of tuples (eventID, event label)
#returns list of common labels between two traces (without IDs)
def common_labels(variant1, variant2):
    var1 = [y[1] for (x, y) in enumerate(variant1)]
    var2 = [y[1] for (x, y) in enumerate(variant2)]
    return list(set(var1).intersection(var2))


#Args: two variants as a list of tuples (eventID, event label)
#Returns: number of common labels between the two variants
def getNumberOfCommonLabels(variant1=[], variant2=[]):
    return len(common_labels(variant1,variant2))

#Args: a variant as a list of tuples and an event label
#returns list of IDs of the given event label 
def get_positions_label(string, variant):
    positions = []
    i = 0
    for x,y in enumerate(variant):
        if y[1] == string:
            positions.insert(i, y[0])
            i +=1
    return positions

#Args: variant1, variant2 as a list of tuples from createEventIDs(variants)
#Returns: list of all possible mappings for variant1 and variant2 where each mapping is a set of matched pairs
def possibleMappings(variant1, variant2):
    matches = [(a,c) for (a,b) in variant1 for (c,d) in variant2 if b == d]
    n = getNumberOfCommonLabels(variant1, variant2)
    
    return [set(combi) for combi in it.combinations(matches, n)
                        if len(set(it.chain.from_iterable(combi))) == (2*n)]


#Args: variant1, variant2 as a list of tuples from createEventIDs(variants)
#return for each common label, a list of possible matchings
#def label_matchings(variant1, variant2):
#    label_matchings = []
#    commonlabels = common_labels(variant1, variant2)
#    #l = 0
#    if commonlabels != []:
#        for label in commonlabels:
#            pos1 = get_positions_label(label, variant1)
#            pos2 = get_positions_label(label, variant2)
#            label_mapping = list(it.product(pos1, pos2))
#            label_matchings.append(label_mapping)
#            #l +=1
#    return label_matchings


#Args: variant1, variant2 as a list of tuples and 
#returns a list of all possible mappings between two trace variants
#def possible_mappings(variant1, variant2, labelmatchings):
#    possiblemappings = []
#    #labelmatchings = label_matchings(variant1, variant2)
#    l = list(it.product(*labelmatchings))
#    for elem in l:
#        s = set(elem)
#        possiblemappings.append(s)
#    return possiblemappings
