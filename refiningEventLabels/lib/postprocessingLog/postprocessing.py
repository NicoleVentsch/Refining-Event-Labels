# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:54:06 2019

@author: Bianka
"""


def postProcessingLog(subgraphList, db, eventLog, cp):
    labels = cp.getCandidateLabels()
    
    for subgraph in subgraphList:
        for eID, data in filter(lambda node: node[1]['curLabel'] in labels, subgraph.nodes(data=True)):            
            vID = db.getEventByID(eID).VariantID
            pos = db.getEventByID(eID).Position
            traces = db.getTracesByVariantID(vID)
            for t in traces:
                eventLog[t][pos]['concept:name'] = data['newLabel']
                

#for case_index, case in enumerate(orgLog):
#    print("\n case index: %d  case id: %s" % (case_index, case.attributes["concept:name"]))
#    for event_index, event in enumerate(case):
#        print("event index: %d  event activity: %s" % (event_index, event["concept:name"]))