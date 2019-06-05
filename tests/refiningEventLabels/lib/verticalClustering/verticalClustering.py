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


def inSameVariant(component1, component2, variants):
    """
    Auxiliary function to determine if two connected components corresponding to the same label are in the same variant (according to section 5.4 in the paper)

    :param component1: first component given as a list of event IDs
    :param component2: second component given as a list of event IDs
    :param variants: list of variants given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    :returns: boolean; True if the connected components are in the same variant, False otherwise
    """
    for event1 in component1:
        for event2 in component2:
            for variant in variants:
                contains1 = False
                contains2 = False
                for eventID, _ in variant:
                    if event1 == eventID:
                        contains1 = True
                    if event2 == eventID:
                        contains2 = True
                if contains1 and contains2:
                    return True

    return False

def ComponentsInSameVariant(connectedComponents, variants):
    """
    Gives the connected Components in the same variants based on a list of connected components

    :param connectedComponents: a list of the connected components that consists of lists [label, event IDs]
    :param variants: list of variants given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    :return: a list of the connected components in the same variant that consists of lists [label, event IDs]

    """
    newConnectedComponents=[]

    for component in connectedComponents:
        label=component[0]
        sameVariant=component[1]
        noMatch=[]
        for a, b in it.combinations(sameVariant, 2):
            if inSameVariant(a, b, variants):
                continue
            else:
                sameVariant.remove(b)
                noMatch.append(b)
        newConnectedComponents.append([label, sameVariant])
        if len(noMatch)>1:
            newConnectedComponents.append(ComponentsInSameVariant([[label,noMatch]], variants))
        if len(noMatch)==1:
            newConnectedComponents.append([label, noMatch])


    return newConnectedComponents

def getPosition(event, variants):
    """
    Auxiliary function to determine the position of an event given its event ID

    :param event: event ID of the event we need the position of
    :param variants: list of variants given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    :returns: integer representing the position of the event in its corresponding variant
    """

    for variant in variants:
        for eventID, _ in variant:
            if event == eventID:
                return event - variant[0][0] + 1

def getAveragePositions(connectedComponents, variants):
    """
    Gives the average positions in the respective variants for each connected component and sorts the components according to their average position

    :param connectedComponents: a list of the connected components that consists of lists [label, event IDs]
    :param variants: variants: list of variants given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    :return: a sorted list of average positions of the connected components, i.e. a list of sorted lists [label, [average posotion component 1, average position component 2,...]]
    """
    averagePositions=[]
    for Labelcomponents in connectedComponents:
        label=Labelcomponents[0]
        components=Labelcomponents[1]
        averages=[]
        for component in components:
            positions = []
            for event in component:
                positions.append(getPosition(event, variants))
            averages.append((component, np.average(positions)))

        averages = sorted(averages, key = lambda x: x[1])

        averagePositions.append([label, averages])
    return averagePositions


def getMaxSizes(connectedComponents):
    """
    gives the maximal sizes of the components for each label with respect to the number of events

    :param connectedComponents: list of list of average positions of the connected components, i.e. a list of sorted lists [label, [average posotion component 1, average position component 2,...]]
    :return: the maximal size of the components for each label
    """

    sizes=[]
    for label,components in connectedComponents:
        maxSize = 0
        for component in components:
            if len(component[0]) > maxSize:
                maxSize=len(component[0])
        sizes.append([label, maxSize])
    return sizes


def verticalRefinement(graphList, candidateLabels, variants, threshold):
    """
    performs the vertical refinement of given candidate labels for a given graph list based on given variants and a threshold

    :param graphList: a list of graphs representing each cluster
    :param candidateLabels: a list of labels that should be refined
    :param variants: list of variants given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
    :param threshold: the unfolding threshold the algorithm should use
    :return: a list of refined subgraphs, where the attribute 'newLabel' is changed for each candidate label according to the vertical clustering algorithm

    """
    # first, get the connected components
    connectedComponents = createConnectedComponents(graphList, candidateLabels)

    # then, get the connected components in the same variant
    sameVariants = ComponentsInSameVariant(connectedComponents, variants)

    # get the sorted components with their average position
    averagePositions = getAveragePositions(sameVariants, variants)

    # get the maximal sizes for the connected components in the same variant
    maxSizes = getMaxSizes(averagePositions)

    # start the refinement for each set of connected components in the same variant
    counter = 0
    lengthComponents = len(averagePositions)
    for i in range(lengthComponents):
        pairs = averagePositions[i]
        label = pairs[0]
        eventPosition = pairs[1]
        maxSize = maxSizes[i]
        length = len(eventPosition)

        for j in range(length):
            if j == 0 or len(eventPosition[j][1]) >= threshold * maxSize:
                counter += 1

            for subgraph in graphList:
                for node, dict in list(subgraph.nodes(data=True)):
                    for event in eventPosition[j][0]:

                        if node == event:
                            dict['newLabel'] += "." + str(counter)

    return graphList

    
    

