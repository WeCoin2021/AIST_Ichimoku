import pandas as pd

data = pd.read_excel("coinbase_Dataset.xlsx")


Lagging_Span = data['ichimoku cloud-Lagging Span']
Span_A = data['ichimoku cloud-Leading Span A']
Span_B = data['ichimoku cloud-Leading Span B']


# ichimoku cloud-Lagging Span or(chikou_span) of 25 days befor:
data['Lagging Span of 25 day before'] = Lagging_Span.shift(25) 

# ichimoku cloud-Leading Span A or(Senkou Span A)of 25 day after:
data['Span A of 25 day after'] = Span_A.shift(-25)

# ichimoku cloud-Leading Span B or(Senkou Span B) of 25 day after:
data['Span B of 25 day after'] = Span_B.shift(-25)

#update dataset
try:
   data.to_excel('updated_coinbase_Dataset.xlsx', encoding='utf-8', index=False)
   print("updated successfully")
except:
   print("An exception occurred")
   
   
