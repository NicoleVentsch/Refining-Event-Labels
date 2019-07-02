import networkx as nx
from collections import defaultdict

def connectedComponents(G, candidateLabels):
    
    """
    computes the connected components given a subgraph 
    :param G: a graph object created from the networkx library
    :param candidateLabels: a list of Strings representing the candidate lables
    :return: a dictionary containing {candidateLabel: [[comp1],[comp2],...]}
    """
    
    #Remove edges with 'weight' == -1
    G.remove_edges_from([(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == -1])
    
    #need to remove duplicated components since the function returns the component with the node itself
    """
    #1st find nodes with candidate labels, 2nd find connected components of each node, 3rd remove duplicate connected components 
    #since two connected nodes may have equal connected components  
    return {label : [list(cc) for cc in set([tuple(sorted(nx.node_connected_component(G, cnode[0])))
                                 for cnode in filter(lambda node: node[1]['curLabel'] == label, G.nodes(data=True))])]
                                     for label in candidateLabels}
    """
    
    #optimized version 
    components = [(G.node[cc[0]]['curLabel'],cc) for cc in map(list,nx.connected_components(G)) 
                                                     if G.node[cc[0]]['curLabel'] in candidateLabels]

    d = defaultdict(list)
    for k,v in components:
        d[k].append(v)
        
    return d
    
    
#def removeDupInComponents(llist):
#    
#    res = []
#
#    for i in range(len(llist)):
#        elem = llist[i]
#        new = set(elem)
#        if i == 0:
#            res.append(new)
#        else:
#            last = res[i-1]
#            if last != new:
#                res.append(new)
#    return res
#        


def sizelargestComponent(connectedComponents):
    
    """
    computes the size of the largest components for each candidateLabel
    :param connectedComponents: a dictionary containing the connected components created from the method connectedComponents()
    :return: a dictionary with the form {candidateLabel: maxSize([[comp1],[comp2],...])}
    """
    
    return {label: len(max(cc, key = len, default = [])) 
                for label, cc in connectedComponents.items()}


def averagePosition(Gi, db):
    
    """
    computes the average position of the events for a given connected component, i.e., #Gi
    :param Gi: a list representing the connected component for a given event [[comp1],[comp2],...]
    :param db: a DBTool object
    :return: a list with the average position [[avgPosComp1],[avgPosComp2],...]
    """
  
    return [sum(map(lambda eID: getPosition(eID,db), nodes))/len(nodes) 
                for nodes in Gi]


def getPosition(eID, db):   
    
    """
    get the position of an event given its eventID
    :param eID: an eventID (integer)
    :param db: a DBTool object
    :return: an integer representig the position of an event within a trace
    """
    
    event = db.getEventByID(eID)
    return event.Position
    

def sortConectedComponents(connectedComponents, db):   
    
    """
    sort the connected components in ascending order w.r.t. their average position
    :param connectedComponents:  a dictionary containing the connected components created from the method connectedComponents()
    :param db: a DBTool object
    :return: a dictionary containing the sorted components, i.e., {candidateLabel: [[comp1],[comp2],...]}
    """
    
    #sortCC = {event: sorted(zip(cc,averagePosition(cc,db)), key = lambda d: d[1]) 
     #           for event, cc in connectedComponents.items()}
        
    sortCC = {event: list(map(lambda d: d[0], sorted(zip(cc,averagePosition(cc,db)), key = lambda d: d[1])))
                 for event, cc in connectedComponents.items()}
    
    return  sortCC


def horizontalRefinement(cp, graphList):
    
    """
    perform the horizontal relabeling according to the paper
    :param cp:  a customParameters object
    :param graphList: a list of graphs created from the networkx library
    :return: the same list of graphs but with relebaled event nodes
    """
            
    candidateLabels = cp.getCandidateLabels()
    
    for i, subgraph in enumerate(graphList, start = 1):  
        for cn,_ in filter(lambda d: d[1]['curLabel'] in candidateLabels, subgraph.nodes(data=True)):
            subgraph.node[cn]['newLabel'] += str(i) 

    return graphList


def verticalRefinement(cp, graphList, db):
    
    """
    perform the vertical relabeling according to the paper
    :param cp:  a customParameters object
    :param graphList: a list of graphs created from the networkx library
    :param db: a DBTool object
    :return: the same list of graphs but with relebaled event nodes
    """    
    
    candidateLabels = cp.getCandidateLabels()
    threshold = cp.getVerticalThreshold()

    for subgraph in graphList:
        cc = connectedComponents(subgraph, candidateLabels)
        cc = sortConectedComponents(cc, db)
        mSize = sizelargestComponent(cc)
        
        for event, nG in cc.items():
            for i,G in enumerate(nG, start = 1):
                for cn in G:
                    if i == 1 or len(G) >= threshold * mSize[event]:
                        subgraph.node[cn]['newLabel'] += '.' + str(i)
                        prevLabel = subgraph.node[cn]['newLabel']
                    else:
                        subgraph.node[cn]['newLabel'] = prevLabel
                prevLabel = '' 
                        
    return graphList