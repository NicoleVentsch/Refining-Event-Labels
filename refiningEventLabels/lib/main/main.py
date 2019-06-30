from refiningEventLabels.lib.graph.graphTool import graphTool
from refiningEventLabels.lib.objects.customParameters import customParameters
from refiningEventLabels.lib.refinement.labelRefinement import verticalRefinement, horizontalRefinement
from refiningEventLabels.lib.eventLogProcessing.DBTool import DBTool
#from refiningEventLabels.lib.eventLogProcessing.filtering import getRelevant
from refiningEventLabels.lib.eventLogProcessing.postProcessing import eventLogRenaming
from refiningEventLabels.lib.costFunction.mappings import createEventIDs, positionsOfCandidates
from refiningEventLabels.lib.costFunction.cost import bestMappings
from pm4py.objects.log.importer.xes import factory as xes_import_factory
import numpy as np

def main (cp, log):

	#PreProcessing Step
#    candidates = cp.getCandidateLabels()
#    db = DBTool(log)
#    all_variants = db.getVariants()
#    relevant_variants = getRelevant(all_variants, candidates)
#    variants = createEventIDs(relevant_variants)
#    count = len(variants) 
#    C = np.zeros((count,count)) 
    
    #PreProcessing Step
    db = DBTool(log)
    variants = createEventIDs(db.getVariants())
    count = len(variants) 
    C = np.zeros((count,count)) 
	  
	#Computing best mappings and MAX(cost)
    best_mappings = bestMappings(cp, variants, C)
    max_cost = np.amax(C)
    C = C/max_cost

	#Intermediate steps before creating the graph
    candidates = cp.getCandidateLabels()
    pos_candidates = positionsOfCandidates(candidates, variants)

	#Graph creation 
    G = graphTool()
    G.createGraphFromVariants(variants)
    G.addOptimalMappings(best_mappings, max_cost, pos_candidates)

	#Refinement Steps
    subgraphs = G.clusterDetection(cp)
    horizontalRefinement(cp, subgraphs)
    verticalRefinement(cp, subgraphs, db)

	#PostProcessing Step
    return eventLogRenaming(cp, subgraphs, db, log)