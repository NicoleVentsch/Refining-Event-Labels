
from pm4py.algo.filtering.log.variants import variants_filter
import pandas as pd



class DBTool:

    def __init__(self, eventLog):
        self.__vt = self.__variantTable(eventLog)
        self.__evt = self.__eventVariantTable(self.__vt)
        
        
    def __variantTable(self, eventLog):
        
        data = pd.DataFrame(variants_filter.get_variants_from_log_trace_idx(eventLog, parameters=None).items())
        data.columns = ['Variants','Traces']
        data['Variants'] = data['Variants'].apply(lambda r: r.split(','))
        data.index.name = 'VariantID'
        
        return data
    
    
    def __eventVariantTable(self, variantTable):
        
        data = self.__vt['Variants'].apply(pd.Series).reset_index() \
        .melt(id_vars = ['VariantID'], var_name='Position', value_name='Event').dropna() \
        .sort_values('VariantID', kind = 'mergesort').reset_index() \
        .drop(['index'], axis = 1)
        data.index.name = 'EventID'
        
        return data


    def getVariants(self): 
        return list(self.__vt['Variants'])
    
    
    def getVariantByID(self, vID):       
        return self.__vt.iloc[vID]['Variants']
    
    
    def getVariantByEventID(self, eID): 
        vID = self.__evt.iloc[eID]['VariantID']    
        return self.getVariantByID(vID)
    
    def getTracesByVariantID(self, vID):
        return self.__vt.iloc[vID]['Traces']
    
    def getEventByID(self, eID):  
        return self.__evt.iloc[eID]
    
    
    def getVariantTable(self):
        return self.__vt
    
    def getEventVariantTable(self):
        return self.__evt

    




