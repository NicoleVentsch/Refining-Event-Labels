# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:25:10 2019

@author: Bianka
"""

import itertools  as it 
from operator import itemgetter


def createEventIDs(variants=[]):

    """
    assigns a unique ID to each event of a variant given a list of variants

    :param variants: list of variants, i.e., a list of lists
    :return: a list of list of tuples (ID,Event), where each ID is unique
    """

    seq = it.count()
    return [[(next(seq),event) for event in variant] for variant in variants]


def commonLabels(variant1, variant2):

    """
    creates a list of common event labels between two variants

    :param variant1: first variant as a list of tuples (eventID, event label)
    :param variant2: second variant as a list of tuples (eventID, event label)
    :return: a list of common event labels (without IDs) between the two variants
    """

    var1 = [y[1] for (x, y) in enumerate(variant1)]
    var2 = [y[1] for (x, y) in enumerate(variant2)]
    return list(set(var1).intersection(var2))



def getNumberOfCommonLabels(variant1=[], variant2=[]):

    """
    gives the number of common event labels between two variants

    :param variant1: first variant as a list of tuples (eventID, event label)
    :param variant2: second variant as a list of tuples (eventID, event label)
    :return: number of common event labels of the two variants
    """

    return len(commonLabels(variant1,variant2))



def getPositionsLabel(string, variant):

    """
    gives a list of all IDs corresponding to a given event label within a given variant

    :param string: event label
    :param variant: variant as a list of tuples (eventID, event label)
    :return: a list of all IDs corresponding to the given event label within the variant
    """

    positions = []
    i = 0
    for x,y in enumerate(variant):
        if y[1] == string:
            positions.insert(i, y[0])
            i +=1
    return positions

#Args: variant1, variant2 as a list of tuples from createEventIDs(variants)
#Returns: list of all possible mappings for variant1 and variant2 where each mapping is a set of matched pairs
def possibleMappings(variant1 = [], variant2 = []):
    """
    gives a list of all possible mappings between two given variants

    :param variant1: first variant as a list of tuples (eventID, event label)
    :param variant2: second variant as a list of tuples (eventID, event label)
    :return: a list of all possible mappings between the two variants where a mapping is a set of matched pairs (ID1,ID2), where the event label corresponding to ID1 is the same as that corresponding to ID2; ID1 is from the first variant and ID2 from the second variant
    """
	
    matches = [(a,c) for (a,b) in variant1 for (c,d) in variant2 if b == d]
    n = getNumberOfCommonLabels(variant1, variant2)
    
    return [list(combi) for combi in it.combinations(matches, n)
                        if len(set(it.chain.from_iterable(combi))) == (2*n)]

#Args: set of candidate labels for refinement, list of all trace variants in event log
#Returns: a list with all event IDs whose label is in the candidate set, we use this later for edge creation in the graph
def positionsOfCandidates(candidates, variants):
    """
    gives a list of all IDs referring to some candidate label

    :param candidates: set of candidate labels for refinement chosen by the user
    :param variants: list of all trace variants in event log where each label has unique ID
    :return: a list with all event IDs whose label is in the candidate set
    """
    positionsOfCandidates = []
    for variant in variants:
        labels = set(map(itemgetter(1), variant))
        for label in labels:
            if label in candidates:
                positions = getPositionsLabel(label, variant)
                positionsOfCandidates.extend(positions)
    return positionsOfCandidates

#Args: variant1, variant2 as a list of tuples from createEventIDs(variants)
#return for each common label, a list of possible matchings
#def label_matchings(variant1, variant2):
#    label_matchings = []
#    commonlabels = commonLabels(variant1, variant2)
#    #l = 0
#    if commonlabels != []:
#        for label in commonlabels:
#            pos1 = getPositionsLabel(label, variant1)
#            pos2 = getPositionsLabel(label, variant2)
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
