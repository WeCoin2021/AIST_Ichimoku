import pandas as pd
#from pandas_datareader import data, wb
import matplotlib as mpl
#from mpl_finance import candlestick_ohlc
import matplotlib.dates as dates
import datetime
import matplotlib.pyplot as plt
from plotly.offline import init_notebook_mode, plot, iplot
#matplotlib inline


d = pd.read_excel("final_coinbase_Dataset.xlsx")

# Set colours for up and down candles
INCREASING_COLOR = '#2D7FEB'
DECREASING_COLOR = '#FA1511'
# create list to hold dictionary with data for our first series to plot
# (which is the candlestick element itself)
data = [ dict(
    type = 'candlestick',
    open = d.Open,
    high = d.High,
    low = d.Low,
    close = d.Close,
    x = d.timestamp,
    yaxis = 'y2',
    name = 'F',
    increasing = dict( line = dict( color = INCREASING_COLOR ) ),
    decreasing = dict( line = dict( color = DECREASING_COLOR ) ),
) ]
# Create empty dictionary for later use to hold settings and layout options
layout=dict()
# create our main chart "Figure" object which consists of data to plot and layout settings
fig = dict( data=data, layout=layout )
# Assign various seeting and choices - background colour, range selector etc
fig['layout']['plot_bgcolor'] = 'rgb(250, 250, 250)'
fig['layout']['xaxis'] = dict( rangeselector = dict( visible = True ) )
fig['layout']['yaxis'] = dict( domain = [0, 0.2], showticklabels = False )
fig['layout']['yaxis2'] = dict( domain = [0.2, 0.8] )
fig['layout']['legend'] = dict( orientation = 'h', y=0.9, x=0.3, yanchor='bottom' )
fig['layout']['margin'] = dict( t=40, b=40, r=40, l=40 )

# Populate the "rangeselector" object with necessary settings
rangeselector=dict(
    visible = True,
    x = 0, y = 0.9,
    bgcolor = 'rgba(150, 200, 250, 0.4)',
    font = dict( size = 13 ),
    buttons=list([
        dict(count=1,
             label='reset',
             step='all'),
        dict(count=1,
             label='1yr',
             step='year',
             stepmode='backward'),
        dict(count=3,
            label='3 mo',
            step='month',
            stepmode='backward'),
        dict(count=1,
            label='1 mo',
            step='month',
            stepmode='backward'),
        dict(step='all')
    ]))
    
fig['layout']['xaxis']['rangeselector'] = rangeselector

# Append the Ichimoku elements to the plot
fig['data'].append( dict( x=d.timestamp, y=d['ichimoku cloud-Conversion line'], type='scatter', mode='lines', 
                         line = dict( width = 1 ),
                         marker = dict( color = '#1E94D9' ),
                         yaxis = 'y2', name='tenkan_sen' ) )
fig['data'].append( dict( x=d.timestamp, y=d['ichimoku cloud-Base line'], type='scatter', mode='lines', 
                         line = dict( width = 1 ),
                         marker = dict( color = '#EB2323' ),
                         yaxis = 'y2', name='kijun_sen' ) )
fig['data'].append( dict( x=d.timestamp, y=d['ichimoku cloud-Leading Span A'], type='scatter', mode='lines', 
                         line = dict( width = 1 ), 
                         marker = dict( color = '#1FB81F' ),
                         yaxis = 'y2', name='senkou_span_a' ) )
fig['data'].append( dict( x=d.timestamp, y=d['ichimoku cloud-Leading Span B'], type='scatter', mode='lines', 
                         line = dict( width = 1 ),fill='tonexty',
                         marker = dict( color = '#FF3342' ),
                         yaxis = 'y2', name='senkou_span_b' ) )
fig['data'].append( dict(x=d.timestamp, y=d['ichimoku cloud-Lagging Span'], type='scatter', mode='lines', 
                         line = dict( width = 1 ),
                         marker = dict( color = '#2B7018' ),
                         yaxis = 'y2', name='chikou_span' ) )

# Set colour list for candlesticks
colors = []
for i in range(len(d.Close)):
    if i != 0:
        if d.Close[i] > d.Close[i-1]:
            colors.append(INCREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)
    else:
        colors.append(DECREASING_COLOR)
        
iplot( fig, filename = 'candlestick-ichimoku' )
