# ichimoku cloud-Conversion line t0
##########################################
def Conversion_line(data):
    nine_period_high = data['High'].rolling(window = 9).max()
    nine_period_low = data['Low'].rolling(window = 9).min()
    data['ichimoku cloud-Conversion line t0'] = (nine_period_high + nine_period_low) /2
   



# ichimoku cloud-Base line t0
##########################################
def Base_line(data):
    period26_high = data['High'].rolling(window=26).max()
    period26_low = data['Low'].rolling(window=26).min()
    data['ichimoku cloud-Base line t0'] = (period26_high + period26_low) / 2



# ichimoku cloud-Lagging Span t0-25
##########################################
def Lagging_Span_befor25(data):
    data['ichimoku cloud-Lagging Span t0-25'] = data['Close'].shift(-25).shift(25)


# ichimoku cloud-Leading Span A t0
##########################################
def Leading_Span_A_t0(data):
    data['ichimoku cloud-Leading Span A t0'] = ((data['ichimoku cloud-Conversion line t0'] + data['ichimoku cloud-Base line t0']) / 2).shift(25)


#  ichimoku cloud-Leading Span B t0
##########################################
def Leading_Span_B_t0(data):
    period52_high = data['High'].rolling(window = 52).max()
    period52_low = data['Low'].rolling(window = 52).min()
    data['ichimoku cloud-Leading Span B t0'] = ((period52_high + period52_low) / 2).shift(25)


# ichimoku cloud-Leading Span A t0+25
##########################################
def Leading_Span_A_after25(data):
    data['ichimoku cloud-Leading Span A t0+25'] = data['ichimoku cloud-Leading Span A t0'].shift(-25)


# ichimoku cloud-Leading Span B t0+25
##########################################
def Leading_Span_B_after25(data):
    data['ichimoku cloud-Leading Span B t0+25'] = data['ichimoku cloud-Leading Span B t0'].shift(-25)









    
