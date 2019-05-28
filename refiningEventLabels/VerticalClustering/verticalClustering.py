# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:18:08 2019

@author: Nicole
"""

#from graph import *
#from mappings import *
#from cost import *
import numpy as np
import networkx as nx
import itertools as it


def createConnectedComponents(graphList, candidateLabels):
    """
    creates the connected components for each imprecise label candidate

    :param graphList: a list of graphs representing each cluster
    :param candidateLabels: a list of labels that should be refined
    :return: list of event names with their corresponding connected components, i.e., a list of tuples (event name, nodes), where nodes is a list containing the IDs of the nodes in that component

    """

    connectedComponents = []
    for label in candidateLabels:
        components = []
        for subgraph in graphList:
            # only consider edges between different variants
            edges = []
            allEdges = list(subgraph.edges(data=True))
            for v, w, weight in allEdges:
                if weight['weight'] > -1:
                    edges.append((v, w))
            print(edges)

            # create the connected components
            for node, dict in list(subgraph.nodes(data=True)):
                if dict['curLabel'] == label:
                    for component in components:
                        for nodes in component:
                            if (nodes, node) in edges:
                                component.append(node)
                                break
                        else:
                            continue
                        break

                    else:
                        components.append([node])

        connectedComponents.append([label, components])

    return connectedComponents


def getMaxSizes(connectedComponents):
    """
    gives the maximal sizes of the components for each label with respect to the number of events

    :param connectedComponents: list of components that consider of lists [label, event IDs]
    :return: the maximal size of the components for each label
    """

    sizes=[]
    for label,components in connectedComponents:
        maxSize = 0
        for component in components:
            if len(component) > maxSize:
                maxSize=len(component)
        sizes.append([label, maxSize])
    return sizes


    
    
    
    

