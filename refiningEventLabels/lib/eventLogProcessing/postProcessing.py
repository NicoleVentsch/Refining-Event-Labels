
def eventLogRenaming(cp, subgraphList, db, eventLog):
    labels = cp.getCandidateLabels()
    
    for subgraph in subgraphList:
        for eID, data in filter(lambda node: node[1]['curLabel'] in labels, subgraph.nodes(data=True)):            
            vID = db.getEventByID(eID).VariantID
            pos = db.getEventByID(eID).Position
            traces = db.getTracesByVariantID(vID)
            for t in traces:
                eventLog[t][pos]['concept:name'] = data['newLabel']
    
    return eventLog
                
                
                
