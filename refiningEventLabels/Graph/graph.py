# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:04:20 2019

@author: Bianka
"""

import mappings
import cost
import numpy as np
import networkx as nx
import itertools  as it 

def createGraph(variants):
    """
    gives a graph where the vertices correspond to all unique pairs (eventID, event label) appearing in the variants

    :param variants: list of variants given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    :return: graph with vertices of the form (eventID, event label)
    """
    G = nx.Graph()
    for variant in variants:
        for pair in variant:
            G.add_node(pair)
    return G



#Might be a good idea to make a Graph class but we can see that later
G = nx.Graph()


#Args: edges as a list of tuples, where edges = [(ID,ID)...])
#Returns: list of edges with weight
def createEdgeList(edges = [], weight = -1):
    """
    creates a list of tuples of edges with the corresponding weights given a list of edges and weights

    :param edges: edges given as a list of tuples (eventID1,eventID2)
    :param weight: a weight
    :return: a list of tuples (eventID1, eventID2, weight) of edges together with their weight
    """
    return [(a,b,{'weight': weight}) for (a,b) in edges]


#Auxiliary function
def pairwise(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


#Args: variant as a list of tuples, where variant = [(EventID,"Label")...]
#Returns: list of variant  with attributes 'curLabel' and 'newLabel
def createNodeListFromVariant(variant = []):
    """
    assigns the current label ('curLabel') and an empty placeholder for the new label ('newLabel') as attributes to the events of a given variant

    :param variant: variant given as a list of tuples (eventID, event label)
    :return: list of variants with the attributes 'curLabel' (previously event label) and 'newLabel' (as am empty string)
    """

    return [(a,{'curLabel':b, 'newLabel':''}) for (a,b) in variant]


#Args: variant as a list of tuples, where variant = [(EventID,"Label")...])
#Returns: list of edges with weight for a given variant
def createEdgeListFromVariant(variant = [], weight = -1):
    """
    creates a list of edges together with their weight for a given variant and weight

    :param variant: variant given as a list of tuples (eventID, event label)
    :param weight: a weight
    :return: a list of edges together with their weight
    """
    edges,_ = zip(*variant)
    return createEdgeList(pairwise(edges), weight)


#Args: list of variants, where variants [[(EvenID,"Label"),(...)],[...]]
#Returns: creates a graph with the initial variants
def createGraphFromVariants(variants = []):
    """
    updates an empty graph, such that it becomes a weighted graph containing vertices of the form (eventID, event label) and edges of the form (eventID1, eventID2, weight) based on a given list of variants

    :param variants: list of variants, where a variant is given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    """
    for variant in variants:
        G.add_nodes_from(createNodeListFromVariant(variant))
        G.add_edges_from(createEdgeListFromVariant(variant))


#Args: optimal mapping as a list, normalized cost as floating point
#Returns: updates the graph by adding edges from the optimal mapping
def addOptimalMapping(optimalMapping = [], normalizedCost = -1):
    """
    updates the graph using a given optimal mapping between two variants and the normalized cost for this mapping

    :param optimalMapping: a mapping as a set of matched pairs (ID1,ID2), where the event label corresponding to ID1 is the same as that corresponding to ID2; ID1 is from the first variant and ID2 from the second variant
    :param normalizedCost: the cost of the mapping
    """
    G.add_edges_from(createEdgeList(optimalMapping , normalizedCost))
#Question here, should we add those edges which are not candidate labels with weight 0?    


    
    
    
    

