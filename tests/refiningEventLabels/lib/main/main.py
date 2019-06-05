# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:55:18 2019

@author: Bianka
"""
import refiningEventLabels.lib.preprocessingLog.preprocessing as pre
import refiningEventLabels.lib.costFunction.mappings as mp
import refiningEventLabels.lib.costFunction.cost as cost
import graph
import numpy as np
from itertools import combinations



#log = event log
#original_variants = getVariants(lookUpTable(log))
#variants = createEventIDs(original_variants)
#candidates = []

log = pre.xes_import_factory.apply("running-example.xes")
original_variants = pre.getVariants(pre.lookUpTable(log))
variants = mp.createEventIDs(original_variants)
candidates = ["decide", "examine casually"] 

#create a cost matrix where Ci,j = Cj,i corresponding to the cost of the best mapping between variants[i] and variants[j]
count = len(variants) 
C = np.zeros((count,count)) 

all_pairs = list(combinations(variants, 2))
for pair in all_pairs:
    best_mapping = cost.optimalMapping(pair[0],pair[1])[0]
    best_cost = cost.optimalMapping(pair[0],pair[1])[1]
    
maxElement = np.amax(C)
C = C/maxElement #each cost is normalized

G = graph.createGraph(variants)

#add edges corresponding to costs
#for pair in all_pairs:
#    
#    best_mapping = cost.optimalMapping(pair[0],pair[1])[0]
#    best_cost = cost.optimalMapping(pair[0],pair[1])[1]
#    
#    firstID1 = pair[0][0][0]
#    firstID2 = pair[1][0][0]
#    index_variant1 = variants.index(pair[0])
#    index_variant2 = variants.index(pair[1])
#    
#    for matched_pair in best_mapping:
#        node1 = pair[0][matched_pair[0]-firstID1]
#        node2 = pair[1][matched_pair[1]-firstID2]      
#        label = pair[0][matched_pair[0]-firstID1][1]
#        if label in candidates:
#            G.add_edge(node1, node2, weight = C[index_variant1][index_variant2])
#        else :
#            G.add_edge(node1, node2, weight = 0)
            
            
            
