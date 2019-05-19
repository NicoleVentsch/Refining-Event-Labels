import itertools  as it 

#Test Variants
v = [['A','B','B','C','D'],['A','B','C','C','D']]


#Args: variants is a list of lists
#Returns: list of list of tuples having (ID,Event) where each ID is unique
def createEventIDs(variants=[]):
    seq = it.count()
    return [[(next(seq),event) for event in variant] for variant in variants]


#Args: variant1, variant2 as a list of tuples from createEventIDs(variants)
#Returns: number of unique events in variant1 and variant2
def getNumberOfCommonLabels(variant1=[], variant2=[]):
    s1 = set([b for (a,b) in variant1])
    s2 = set([b for (a,b) in variant2])
    
    return len(s1.intersection(s2))


#Args: variant1, variant2 as a list of tuples from createEventIDs(variants)
#Returns: list of lists with all possible mappings for variant1 and variant2
def possibleMappings(variant1=[], variant2=[]):
    matches = [(a,c) for (a,b) in variant1 for (c,d) in variant2 if b == d]
    n = getNumberOfCommonLabels(variant1, variant2)
    
    return [list(combi) for combi in it.combinations(matches, n)
                        if len(set(it.chain.from_iterable(combi))) == (2*n)]