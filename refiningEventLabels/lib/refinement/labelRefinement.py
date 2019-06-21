import networkx as nx

#Get Connected components given a subgraph G
#Return a dictionary with the form {label: [{comp1},{comp2}...]}
def connectedComponents(G, candidateLabels):
    
    #Remove edges with 'weight' == -1
    G.remove_edges_from([(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == -1])
    
    #1st find nodes with candidate labels, 2nd find connected components of each node, 3rd remove duplicate connected components 
    #since two connected nodes may have equal connected components   
    return {label : [list(cc) for cc in set([tuple(nx.node_connected_component(G, cnode[0]))
                                 for cnode in filter(lambda node: node[1]['curLabel'] == label, G.nodes(data=True))])]
                                     for label in candidateLabels}


#Get the size of the largest component given a connectedComponents dictionary
#Return a dictionary with the form {label: maxSize[{comp1},{comp2},...]}
def sizelargestComponent(connectedComponents):  
    return {label: len(max(cc, key=len, default=[])) 
                for label, cc in connectedComponents.items()}

#Get the average position of the events for a given connectedComponent, i.e., #Gi
#Return a list with the avg position [[avgPosComp1],[avgPosComp2],...]
def averagePosition(Gi, db):    
    return [sum(map(lambda eID: getPosition(eID,db), nodes))/len(nodes) 
                for nodes in Gi]

#Get the position of an event given its eventID
def getPosition(eID, db):   
    event = db.getEventByID(eID)
    return event.Position
    
#Sort the Connected components in ascending order
#Return a dictionary with sorted components having the form {label: [{comp1},{comp2}...]}
def sortConectedComponents(connectedComponents, db):   
    #sortCC = {event: sorted(zip(cc,averagePosition(cc,db)), key = lambda d: d[1]) 
     #           for event, cc in connectedComponents.items()}
        
    sortCC = {event: list(map(lambda d: d[0], sorted(zip(cc,averagePosition(cc,db)), key = lambda d: d[1])))
                 for event, cc in connectedComponents.items()}
    
    return  sortCC



def horizontalRefinement(cp, graphList):
        
    candidateLabels = cp.getCandidateLabels()
    
    for i, subgraph in enumerate(graphList, start = 1):  
        for cn,_ in filter(lambda d: d[1]['curLabel'] in candidateLabels, subgraph.nodes(data=True)):
            subgraph.node[cn]['newLabel'] += str(i) 

    return graphList

#For each subgraph relabel candidateLabels according to the paper
def verticalRefinement(graphList, candidateLabels, db, threshold):
    
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