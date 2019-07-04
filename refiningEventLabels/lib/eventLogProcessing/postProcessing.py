
def eventLogRenaming(cp, subgraphList, db, eventLog):
    """
    Rename the original eventLog based on the results of the refinement algorithm

    :param cp: a customParameters object
    :param subgraphList: a list of graphs created from the networkx library
    :param db: a DBTool object
    :param eventLog: the original event log provided by the user
    :return: the refined event log based on the results of the refinement algorithm
    """
    
    labels = cp.getCandidateLabels()
    
    for subgraph in subgraphList:
        for eID, data in filter(lambda node: node[1]['curLabel'] in labels, subgraph.nodes(data=True)):            
            vID = db.getEventByID(eID).VariantID
            pos = db.getEventByID(eID).Position
            traces = db.getTracesByVariantID(vID)
            for t in traces:
                eventLog[t][pos]['concept:name'] = data['newLabel']
    
    return eventLog
                

