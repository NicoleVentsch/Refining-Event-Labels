
from pm4py.algo.filtering.log.variants import variants_filter
import pandas as pd



class DBTool:
    """
    Virtual Database containing the main preprocessing steps and tools used to access the eventLog data
    """
    def __init__(self, eventLog):
        self.__vt = self.__variantTable(eventLog)
        self.__evt = self.__eventVariantTable(self.__vt)
        
        
    def __variantTable(self, eventLog):
        
        """
        Create a table containing the following attributes: VariantID, Variants and Traces
    
        :param eventLog: an eventLog object obtained from the pm4py library
        :return: a pandas DataFrame with the mentioned attributes
        """
        
        data = pd.DataFrame(variants_filter.get_variants_from_log_trace_idx(eventLog, parameters=None).items())
        data.columns = ['Variants','Traces']
        data['Variants'] = data['Variants'].apply(lambda r: r.split(','))
        data.index.name = 'VariantID'
        
        return data
    
    
    def __eventVariantTable(self, variantTable):
        
        """
        Create a table containing the following attributes: EventID, VariantID, Position and Event
    
        :param variantTable: a pandas DataFrame obtained from the method __variantTable
        :return: a pandas DataFrame with the mentioned attributes
        """
          
        data = self.__vt['Variants'].apply(pd.Series).reset_index() \
        .melt(id_vars = ['VariantID'], var_name='Position', value_name='Event').dropna() \
        .sort_values('VariantID', kind = 'mergesort').reset_index() \
        .drop(['index'], axis = 1)
        data.index.name = 'EventID'
        
        return data


    def getVariants(self): 
        
        """
        Get all the variants from the variantTable
    
        :return: a list of list of Strings representig all the variants
        """
        
        return list(self.__vt['Variants'])
    
    
    def getVariantByID(self, vID):       
        
        """
        Get a variant given a variantID
    
        :param vID: a variantID (integer)
        :return: a list of Strings representig a variant
        """
        
        return self.__vt.iloc[vID]['Variants']
    
    
    def getVariantByEventID(self, eID): 
        
        """
        Get a variant given an eventID
    
        :param eID: an eventID (integer)
        :return: a list of Strings representig a variant
        """
        
        vID = self.__evt.iloc[eID]['VariantID']    
        return self.getVariantByID(vID)
    
    
    def getTracesByVariantID(self, vID):
        
        """
        Get all traces within a variant given a variantID
    
        :param vID: an variantID (integer)
        :return: a list of integers representig the traces within a variant
        """
        
        return self.__vt.iloc[vID]['Traces']
    
    
    def getEventByID(self, eID):
        
        """
        Get an event given its eID
    
        :param eID: an eventID (integer)
        :return: an Object representig an event (containing:  EventID, VariantID, Position and Event)
        """
        
        return self.__evt.iloc[eID]
    
    
    def getVariantTable(self):
        
        """
        Get the variantTable
    
        :return: a pandas DataFrame representing the variantTable
        """
        
        return self.__vt
    
    
    def getEventVariantTable(self):
        
        """
        Get the eventVariantTable
    
        :return: a pandas DataFrame representing the eventVariantTable
        """
        
        return self.__evt

    




