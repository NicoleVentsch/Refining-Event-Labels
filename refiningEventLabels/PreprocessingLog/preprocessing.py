import pm4py
from pm4py.objects.log.importer.xes import factory as xes_importer



# get the variants with the corresponding IDs (-> lookup-map)
# input: log (imported with xes_importer)
# stored as a dicctionary with variants as key and as value the list of case IDs that share the variant
from pm4py.algo.filtering.log.variants import variants_filter

def lookUpTable(log):
    variant=variants_filter.get_variants_from_log_trace_idx(log, parameters=None)
    return variant

# get the variants from the dicctionary created with lookUpTable() and omit the IDs
# input: dicctionary with variants as keys and case IDs as values
# stored as a list containing the variants as lists (-> list of lists)
def getVariants(dicctionary):
    variants=list(dicctionary.keys())
    return [variant.split(',') for variant in variants]
