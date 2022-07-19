from sqlite3 import Timestamp
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from  mplfinance.original_flavor import candlestick_ohlc
import matplotlib.pyplot as plt
import numpy as np
import decimal
import matplotlib.dates as dates

class PLOT():

    

    def __init__(self, data):
        self.data = data

    def plot(self):
        fig, ax = plt.subplots()    
        self.plot_candlesticks(fig, ax)
        self.plot_ichimoku(fig, ax)
        self.pretty_plot(fig, ax)
        plt.show()

    def pretty_plot(self, fig, ax):
        ax.legend()
        fig.autofmt_xdate()
        ax.xaxis_date()

        # Chart info
        title = 'Ichimoku  (BTC/USD)'
        bgcolor = '#131722'
        grid_color = '#363c4e'
        spines_color = '#d9d9d9'
        # Axes
        plt.title(title, color='white')
        plt.xlabel('Date', color=spines_color, fontsize=7)
        plt.ylabel('Price (BTC)', color=spines_color, fontsize=7)

        ax.set_facecolor(bgcolor)
        ax.grid(linestyle='-', linewidth='0.5', color=grid_color)
        ax.yaxis.tick_right()
        ax.set_yscale("log", nonposy='clip')
        fig.patch.set_facecolor(bgcolor)
        fig.patch.set_edgecolor(bgcolor)
        plt.rcParams['figure.facecolor'] = bgcolor
        plt.rcParams['savefig.facecolor'] = bgcolor
        ax.spines['bottom'].set_color(spines_color)
        ax.spines['top'].set_color(spines_color) 
        ax.spines['right'].set_color(spines_color)
        ax.spines['left'].set_color(spines_color)
        ax.tick_params(axis='x', colors=spines_color, size=7)
        ax.tick_params(axis='y', colors=spines_color, size=7)
        fig.tight_layout()
        ax.autoscale_view()

    def plot_ichimoku(self, fig, ax):
        d2 = self.data
        
        date_axis = self.data.timestamp
        # ichimoku
        plt.plot(date_axis, d2['ichimoku cloud-Conversion line'], label="tenkan", color='#0496ff', alpha=0.65,linewidth=0.5)
        plt.plot(date_axis, d2['ichimoku cloud-Base line'], label="kijun", color="#991515", alpha=0.65,linewidth=0.5)
        plt.plot(date_axis, d2['ichimoku cloud-Lagging Span'], label="chikou", color="#008000", alpha=0.65,linewidth=0.5)
        plt.plot(date_axis, d2['ichimoku cloud-Leading Span A'], label="span a", color="#ff0000", alpha=0.65, linewidth=0.5)
        plt.plot(date_axis, d2['ichimoku cloud-Leading Span B'], label="span b", color="#ffffff", alpha=0.65, linewidth=0.5)
        # green cloud
        ax.fill_between(date_axis, d2['ichimoku cloud-Leading Span A'], d2['ichimoku cloud-Leading Span B'], where=d2['ichimoku cloud-Leading Span A']> d2['ichimoku cloud-Leading Span B'], facecolor='#008000', interpolate=True, alpha=0.25)
        # red cloud
        ax.fill_between(date_axis, d2['ichimoku cloud-Leading Span A'], d2['ichimoku cloud-Leading Span B'], where=d2['ichimoku cloud-Leading Span B']> d2['ichimoku cloud-Leading Span A'], facecolor='#ff0000', interpolate=True, alpha=0.25)

    def plot_candlesticks(self, fig, ax):
        # plot candlesticks
        self.data.timestamp = dates.date2num(self.data.timestamp)
        candlesticks_df = self.data.loc[:, ['timestamp','Open','High','Low', 'Close']]
        
        # plot candlesticks
        candlestick_ohlc(ax, candlesticks_df.values, width=0.6, colorup='#83b987', colordown='#eb4d5c', alpha=0.5 )

    # Range generator for decimals
    def drange(self, x, y, jump): 
        while x < y:
            yield float(x)
            x += decimal.Decimal(jump)

my_data = pd.read_excel("final_coinbase_Dataset.xlsx")
my_plot = PLOT(my_data)  
my_plot.plot()          