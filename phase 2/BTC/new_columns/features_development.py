import pandas as pd
from functions import *

#open dataset
data = pd.read_excel("BTC_ichimoku_Dataset.xlsx")

# call your new functions which have been developed in functions.py:

#########################
# add calling function section
    '''
            example:
            Conversion_line(data)
    '''








#########################


#update dataset
try:
    data.to_excel('new_features_Dataset.xlsx', encoding='utf-8', index=False)
    print("updated successfully")
except:
    print("An exception occurred")
