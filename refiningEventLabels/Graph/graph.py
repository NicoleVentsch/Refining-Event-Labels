# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:04:20 2019

@author: Bianka
"""

import mappings
import cost
import numpy as np
import networkx as nx


#returns a Graph where the vertex correspond to all unique pairs (Id, event label) appearing in the variants
def createGraph(variants):
    G = nx.Graph()
    for variant in variants:
        for pair in variant:
            G.add_node(pair)
    return G