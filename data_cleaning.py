import pandas as pd
import numpy as np

def load_data():
    '''
    The load_data() function reads a specific .csv file (i.e. data.csv) into a
    pandas dataframe (data).
    
    Use as following:
    >> data = load_data()
    '''
    print('Reading data... ')
    data = pd.read_csv('data.csv')
    print('Alright! Good to go.')
    return data

def data_cleaning():
   '''
   The data_cleaning() functions uses load_data() to obtain pandas dataframe 'data' and
   proceeds to the cleaning job. Retuns a convinient pandas dataframe named 'cdata'.
   add desc
   
   Use as following:
   >> cdata = data_cleaning()
   '''
   data = load_data()
   
   

data = load_data()
print(data) 