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

#returns a Graph where the vertex correspond to all unique pairs (Id, event label) appearing in the variants
def createGraph(variants):
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
    return [(a,b,{'weight': weight}) for (a,b) in edges]


#Auxiliary function
def pairwise(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


#Args: variant as a list of tuples, where variant = [(EventID,"Label")...]
#Returns: list of variant  with attributes 'curLabel' and 'newLabel
def createNodeListFromVariant(variant = []):
    return [(a,{'curLabel':b, 'newLabel':''}) for (a,b) in variant]


#Args: variant as a list of tuples, where variant = [(EventID,"Label")...])
#Returns: list of edges with weight for a given variant
def createEdgeListFromVariant(variant = [], weight = -1):
    edges,_ = zip(*variant)
    return createEdgeList(pairwise(edges), weight)


#Args: list of variants, where variants [[(EvenID,"Label"),(...)],[...]]
#Returns: creates a graph with the initial variants
def createGraphFromVariants(variants = []): 
    for variant in variants:
        G.add_nodes_from(createNodeListFromVariant(variant))
        G.add_edges_from(createEdgeListFromVariant(variant))


#Args: optimal mapping as a list, normalized cost as floating point
#Returns: updates the graph by adding edges from the optimal mapping
def addOptimalMapping(optimalMapping = [], normalizedCost = -1):
    G.add_edges_from(createEdgeList(optimalMapping , normalizedCost))
#Question here, should we add those edges which are not candidate labels with weight 0?    


    
    
    
    

