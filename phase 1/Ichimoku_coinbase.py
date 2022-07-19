import pandas as pd

data = pd.read_excel("coinbase_Dataset.xlsx")


high_prices = data['High']
close_prices = data['Close']
low_prices = data['Low']
dates = data['timestamp']

# ichimoku cloud-Conversion line or(Tenkan-sen): (max of 9-period 'High' + min of 9-period 'Low') / 2 .
    
nine_period_high = data['High'].rolling(window = 9).max()
nine_period_low = data['Low'].rolling(window = 9).min()
data['ichimoku cloud-Conversion line'] = (nine_period_high + nine_period_low) /2

# ichimoku cloud-Base line or(Kijun-sen): ( max of 26-period 'High' + min of 26-period 'Low') / 2 .

period26_high = data['High'].rolling(window=26).max()
period26_low = data['Low'].rolling(window=26).min()
data['ichimoku cloud-Base line'] = (period26_high + period26_low) / 2


# ichimoku cloud-Lagging Span or(chikou_span): The most current closing price plotted 26 time periods behind ,
#this day is so in the period .

data["ichimoku cloud-Lagging Span"] = close_prices.shift(-( 26 - 1 )) 

# ichimoku cloud-Leading Span A or(Senkou Span A): (Conversion Line + Base Line)/2 ,plotted 26 time periods after .
#this day is so in the period .

data['ichimoku cloud-Leading Span A'] = ((data['ichimoku cloud-Conversion line'] + data['ichimoku cloud-Base line']) / 2).shift(26 - 1)

# ichimoku cloud-Leading Span B or(Senkou Span B): (max of 52-period 'High' + min of 52-period 'Low')/2 ,plotted 26 time periods after .
#this day is so in the period .

period52_high = data['High'].rolling(window = 52).max()
period52_low = data['Low'].rolling(window = 52).min()
data['ichimoku cloud-Leading Span B'] = ((period52_high + period52_low) / 2).shift(26 - 1)

#update dataset
try:
   data.to_excel('final_coinbase_Dataset.xlsx', encoding='utf-8', index=False)
   print("updated successfully")
except:
   print("An exception occurred")
   
   
