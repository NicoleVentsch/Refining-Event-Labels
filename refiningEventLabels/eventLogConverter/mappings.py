# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:43:00 2019

@author: Bianka
"""



#original variants is a list of lists
#function assigns a unqie index to each event 
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
    

def generate_mappings(variant1, variant2):
    mappings = []
    label_mappings = []
    l = 0
    common_labels = common_labels(variant1, variant2)
    if common_labels != []:
        for label in common_labels:
            pos1 = get_position_label(label, variant1)
            pos2 = get_position_label(label, variant2)
            for p1 in pos1:
                for p2 in pos2:
                    label_mappings.insert(l, (p1,p2))
        l += 1
        pass