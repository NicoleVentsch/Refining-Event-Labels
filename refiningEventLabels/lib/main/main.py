from refiningEventLabels.lib.graph.graphTool import graphTool 
from refiningEventLabels.lib.objects.customParameters import customParameters
from refiningEventLabels.lib.refinement.labelRefinement import verticalRefinement, horizontalRefinement
from refiningEventLabels.lib.eventLogProcessing.DBTool import DBTool 
from refiningEventLabels.lib.eventLogProcessing.postProcessing import eventLogRenaming
from refiningEventLabels.lib.costFunction.mappings import createEventIDs, positionsOfCandidates
from refiningEventLabels.lib.costFunction.cost import bestMappings
from pm4py.objects.log.importer.xes import factory as xes_import_factory
import numpy as np

def main (cp, log):

	#REPLACE with data from local web server
	#log = xes_import_factory.apply("refiningEventLabels/lib/running-example.xes")
	#orgLog = xes_import_factory.apply("refiningEventLabels/lib/running-example.xes")
	#cp = customParameters(candidateLabels = ["decide", "examine casually"],
	#					  horizontalThreshold = 0.5,
	#					  verticalThreshold = 0.3, 
	#					  weightStructure = 0.3, 
	#					  weightMatch = 0.3, 
	#					  weightNoMatch = 0.3)


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