# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:53:53 2019

@author: Bianka
"""

def isRelevant(variant, candidates):
    """
    function that checks if the given variant contains some candidate label

    :param variant: a trace variant in the original log
    :param candidates: a list of candidate labels picked by the user
    :return: True if the variant contains some candidate label
    """
    for candidate in candidates:
        if candidate in variant:
            return True
        else:
            return False
        
def getRelevant(variants, candidates):
    """
    function that returns a list containing only relevant variants

    :param variants: the list of all variants in the original log
    :param candidates: a list of candidate labels picked by the user
    :return: list of all variants which contain some candidate label and should be considered in the mappings
    """
    relevant_variants = []
    for variant in variants:
        if isRelevant(variant, candidates):
            relevant_variants.append(variant)
    return relevant_variants