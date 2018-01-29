# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:11:56 2018

@author: obria
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:35:30 2018

@author: Brandon O'Briant

The problem definition: 
   

Research:
    
    
Solution:
   
    
"""
# import packages to be used in the namespace
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# overrides the default rcParams for plotting
def init_plotting():
    plt.style.use(style='ggplot')
    plt.rcParams['figure.figsize'] = (10.0, 8.0)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['text.color'] = 'black'
    plt.rcParams['axes.labelcolor'] = 'black'
    plt.rcParams['xtick.color']= 'black'
    plt.rcParams['ytick.color']= 'black'
init_plotting()
# avoid empty plot, always good to close plot
plt.close() 


# note about numpy, we can vectorize (organize several knids of data processing
# tasks as array expression) data to simplify calucations
# using one or multi demensional arrays

# The adjusted closing price will be used for calucaltions in this program
# since the adjusted closing price (Adj Close) accounts for dividen payouts
# and stock splits

# ticker_df, desired name for pandas DataFrame
# tickername, type string, is the name of the ticker for source to look up
# data_source is yahoo
# start_date, the desired start date of the stock information
def import_stock_data(ticker_df, tickers, start_date):
    ticker_df = pd.DataFrame()
    for t in tickers:
        ticker_df[t] = wb.DataReader(t, data_source = 'yahoo',
                               start = start_date)['Adj Close']
    return ticker_df


# prints first and last few rows of DataFrame
# prints information about DataFrame (number of columns, rows, data type)
def print_head_tail_info_df(dataframe):
    print('\n{} first ten rows:\n {}'.format(dataframe.name, dataframe.head()))
    print('\n{} last ten rows:\n {}'.format(dataframe.name, dataframe.tail()))
    print('\n{} dataframe information:\n {}'.format(dataframe.name, dataframe.info()))

# start date for the stocks data
# the dataset starts June 29, 2010 and goes to present
start_date = '2010-6-29'

# tickers for stocks to be ustilized in this program
# Apple Inc (AAPL), Microsoft (MSFT), Intel (INTL), Tesla Inc. (TSLA), 
# SP500 market (^GSPC)
tickers = ['AAPL', 'MSFT', 'INTL', 'TSLA', '^GSPC']

# securites_data, pandas DataFrame to store stock data
# initialized to enmtpy DataFrame
securities_data = pd.DataFrame()

# add name to DataFrame
securities_data.name = 'securities'

# import the stock data from yahoo for the tickers, and store it in port_data
# ------NOTE: check this agains yahoo to make sure information is correct-----#
securities_data = import_stock_data(securities_data, tickers, start_date) 

# add name to DataFrame
securities_data.name = 'portfolio'


# check the first and last few rows and infor for port_data
print_head_tail_info_df(securities_data)


# Normalizatoin to 100: helps normalize data to 100
#  (P_t/P_0) * 100
# create subset of data using .iloc[0] to exract the data from the first column
# of the table to be used in normailization procedure to use for campring 
# all stocks as if they all started at 100
# create line chart of data to compare behavior of stocks
(securities_data/securities_data.iloc[0]*100).plot(figsize = (15,6))
plt.savefig('Line-Chart_Compare_Behvior.pdf', 
    bbox_inches = 'tight', dpi=None, facecolor='w', edgecolor='b', 
    orientation='portrait', papertype=None, format=None, 
    transparent=True, pad_inches=0.25, frameon=None)
plt.show()
plt.close()

##############################################################################
#            Calcualting The Log Return of Portfolio Securities              #
##############################################################################
## log Rate of Return
# To calcualte the log rate of return  we use todays
# closing price divided by the previous
# log(P_1/P_0)

# calcualtes the log rate of return
# creates a new column to store the simple_return
# security_returns dataframe with the new column associated with the log rate of return
# we shift the day using pandas.DataFrame.shit(# of lags), in our case
# # of lags is 1, thus we are shifting the index by 1
# Note there will be a nan value for the first value, since there is no lag for the
# first day recorded
# prints out the calcualted results
def log_rate_of_return(dataframe):
    returns = np.log((dataframe/dataframe.shift(1)))
    print('\n{} simple_rate_of_return results:\n {}'
          .format(dataframe.name, returns))
    return returns

# calculate the securities log rate of return
securities_returns = log_rate_of_return(securities_data)

# Roll Function, returns groupby object
def rolling_func(dataframe, stacking_amount):
    rolling_array = np.dstack([dataframe.values[i:i+stacking_amount, :] for i in range(len(dataframe.index) - stacking_amount + 1]).T
        


