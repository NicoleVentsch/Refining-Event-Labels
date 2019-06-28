
import networkx as nx
import itertools  as it 



class graphTool:
    """ graph class containing the main functionalities we need for the algorithm"""
    
    
    def __init__(self):
        """
        initialization of a graph
        """
        self.__G = nx.Graph()
        

    def createEdgeList(self, edges = [], weight = -1):
        
        """
        creates a list of tuples of edges with the corresponding weights given a list of edges and weights
    
        :param edges: edges given as a list of tuples (eventID1,eventID2)
        :param weight: a weight
        :return: a list of tuples (eventID1, eventID2, weight) of edges together with their weight
        """
        
        return [(a,b,{'weight': weight}) for (a,b) in edges]
    
    
    def __pairwise(self, iterable):
        
        """ auxiliary function to create pairs"""
        
        a, b = it.tee(iterable)
        next(b, None)
        return zip(a, b)
    

    def __createNodeListFromVariant(self, variant = []):
       
        """
        assigns the current label ('curLabel') and an empty placeholder for the new label ('newLabel') as attributes to the events of a given variant
    
        :param variant: variant given as a list of tuples (eventID, event label)
        :return: list of variants with the attributes 'curLabel' (current event label) and 'newLabel' (initialized as event label)
        """
    
        return [(a,{'curLabel':b, 'newLabel':b}) for (a,b) in variant]
    
        
    def __createEdgeListFromVariant(self, variant = [], weight = -1):
       
        """
        creates a list of edges together with their weight for a given variant and weight
    
        :param variant: variant given as a list of tuples (eventID, event label)
        :param weight: a weight
        :return: a list of edges together with their weight
        """
       
        edges,_ = zip(*variant)
        return self.createEdgeList(self.__pairwise(edges), weight)
    
    
    def createGraphFromVariants(self, variants = []):
       
        """
        updates an empty graph, such that it becomes a weighted graph containing vertices of the form (eventID, event label) and edges of the form (eventID1, eventID2, weight) based on a given list of variants
    
        :param variants: list of variants, where a variant is given as a list of tuples (eventID, event label), i.e., a list of lists of tuples
        """
        
        for variant in variants:
            self.__G.add_nodes_from(self.__createNodeListFromVariant(variant))
            self.__G.add_edges_from(self.__createEdgeListFromVariant(variant))
    

    """
    def addOptimalMapping(self, optimalMapping = [], normalizedCost = -1):
        
        updates the graph using a given optimal mapping between two variants and the normalized cost for this mapping
    
        :param optimalMapping: a mapping as a set of matched pairs (ID1,ID2), where the event label corresponding to ID1 is the same as that corresponding to ID2; ID1 is from the first variant and ID2 from the second variant
        :param normalizedCost: the cost of the mapping
       
        self.__G.add_edges_from(self.createEdgeList(optimalMapping , normalizedCost))
    """  
        
    def clusterDetection(self, customParams):
        
        """
        clusters the variants based on a given threshold; to do so, edges with a weight above the threshold are deleted from the given graph respresenting the optimal mappings
    
        :param threshold: the variant threshold the algorithm should use
        :return: list of subgraphs where each subgraph represents a cluster of variants
    
        """
        
        horizontalTreshold = customParams.getHorizontalThreshold()

        filteredEdges = [(u, v) for (u, v, d) in self.__G.edges(data=True) if (d['weight'] > horizontalTreshold and d['weight'] != -1)]
        self.__G.remove_edges_from(filteredEdges)
    
        return [nx.Graph(self.__G.subgraph(c)) for c in nx.k_edge_subgraphs(self.__G, k = 1)] #or also use nx.connected_components(G)


    def getGraph(self):
        
        """
        returns the graph object
        param: none
        return: nx.Graph() object
        """
       
        return self.__G
    
    
    def addOptimalMappings(self, bestMappingsList, maxCost, candidatePositions):
        
        """
		updates the graph using a given optimal mapping between two variants and the normalized cost for this mapping

		:param optimalMapping: a mapping as a set of matched pairs (ID1,ID2), where the event label corresponding to ID1 is the same as that corresponding to ID2; ID1 is from the first variant and ID2 from the second variant
		:param normalizedCost: the cost of the mapping
		"""
        
        for mapp in bestMappingsList:
            normalized_cost = mapp[1]/maxCost
            mapped_pairs = mapp[0]
            candidate_pairs = []
            #non_candidate_pairs = []
            for(x,y) in mapped_pairs:
                if x in candidatePositions:
                    candidate_pairs.append((x,y))
                else:
                    candidate_pairs.append((x,y))
                    self.__G.add_edges_from(self.createEdgeList(candidate_pairs, normalized_cost))
                    #self.__G.add_edges_from(self.createEdgeList(non_candidate_pairs, 0))

    

