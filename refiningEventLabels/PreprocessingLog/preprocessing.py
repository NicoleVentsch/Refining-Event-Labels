import pm4py
from pm4py.objects.log.importer.xes import factory as xes_importer



# get the variants with the corresponding IDs (-> lookup-map)
from pm4py.algo.filtering.log.variants import variants_filter

def lookUpTable(log):

    """

    given an event log it will give the unique variants with the corresponding IDs that share the variant

    :param log:  an event log imported using xes_importer
    :return: variants with the corresponding IDs stored as a dicctionary with variants as key and as value the list of case IDs

    """

    variant=variants_filter.get_variants_from_log_trace_idx(log, parameters=None)
    return variant


def getVariants(dicctionary):

    """

    get the variants from the dicctionary created with lookUpTable() and omit the IDs

    :param dicctionary: a dicctionary with variants as key and as value the list of case IDs
    :return: list of unique variants stored as lists (list of lists)

    """
    variants=list(dicctionary.keys())
    return [variant.split(',') for variant in variants]
