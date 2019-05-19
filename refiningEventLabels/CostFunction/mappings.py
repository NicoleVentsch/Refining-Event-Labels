# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:43:00 2019

@author: Bianka
"""

import itertools as it

#original variants is a list of lists
#function assigns a unque index to each event
def variants(original_variants):
    variants = original_variants
    i = 0
    for variant_index in range(len(variants)):
        for event_index in range(len(variants[variant_index])):
            variants[variant_index][event_index] = (i, str(original_variants[variant_index][event_index]))
            i += 1
    return variants


#returns true if two trace variants have common labels
def common_labels(variant1, variant2):
    var1 = [y[1] for (x, y) in enumerate(variant1)]
    var2 = [y[1] for (x, y) in enumerate(variant2)]
    return list(set(var1).intersection(var2))

#returns list of indexes of events with certain label
def get_position_label(string, variant):
    positions = []
    i = 0
    for x,y in enumerate(variant):
        if y[1] == string:
            positions.insert(i, y[0])
            i +=1
    return positions
    
#return for each common label, a list of possible matchings
def label_matchings(variant1, variant2):
    label_matchings = []
    commonlabels = common_labels(variant1, variant2)
    #l = 0
    if commonlabels != []:
        for label in commonlabels:
            pos1 = get_position_label(label, variant1)
            pos2 = get_position_label(label, variant2)
            label_mapping = list(it.product(pos1, pos2))
            label_matchings.append(label_mapping)
            #l +=1
    return label_matchings

#returns a list of all possible mappings between two trace variants
def possible_mappings(variant1, variant2, labelmatchings):
    possiblemappings = []
    #labelmatchings = label_matchings(variant1, variant2)
    l = list(it.product(*labelmatchings))
    for elem in l:
        s = set(elem)
        possiblemappings.append(s)
    return possiblemappings