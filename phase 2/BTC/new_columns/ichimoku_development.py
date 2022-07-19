import pandas as pd
from functions import *

#open dataset
data = pd.read_excel("BTC_Dataset.xlsx")

# call functions:
#########################

Conversion_line(data)
Base_line(data)
Lagging_Span_befor25(data)
Leading_Span_A_t0(data)
Leading_Span_B_t0(data)
Leading_Span_A_after25(data)
Leading_Span_B_after25(data)


#########################

#update dataset
try:
    data.to_excel('BTC_ichimoku_Dataset.xlsx', encoding='utf-8', index=False)
    print("updated successfully")
except:
    print("An exception occurred")
