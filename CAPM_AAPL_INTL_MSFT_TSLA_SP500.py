# -*- coding: utf-8 -*-

"""
Created on Wed Jan 24 09:35:30 2018

@author: Brandon O'Briant

CAPM, Markowitz Efficient Frontier with Sharpe Ratio
    
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
    plt.rcParams['axes.facecolor']='gainsboro'
plt.rcParams['savefig.facecolor']='gainsboro'
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
tickers = ['AAPL', 'MSFT', 'INTL', 'TSLA']

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
plt.savefig('Line-Chart_Compare_Behvior.png', 
    bbox_inches = 'tight', dpi=None, facecolor='w', edgecolor='b', 
    orientation='portrait', papertype=None, format=None, 
    transparent=False, pad_inches=0.25, frameon=None)
plt.show()
plt.close()


# daily stock prices converted into daily returns
returns = securities_data.pct_change()

# calculate mean daily returns
mean_daily_returns = returns.mean()

# covariance of daily returns
cov_matrix = returns.cov()

# set the number of the random portfolio weights runs to try
number_of_portfolios = 30000

# results, array to hold results
# increase array size to hold weight values for each of the assets
results = np.zeros((4+len(tickers)-1,number_of_portfolios))


for i in range(number_of_portfolios):
    # random weights selected
    weights = np.array(np.random.random(len(tickers)))
    # weight sum to 1
    weights /= np.sum(weights)
    
    # portfolio return
    portfolio_return = np.sum(mean_daily_returns * weights) * 252
    
    # calcualte portfolio volatility
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    
    # results, array to store results
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev
    
    # store sharpe ratio, (return/volatility)
    results[2, i] = results[0,i]/ results[1,i]
    
    # add results to array by iterating through weight vector
    for x in range(len(weights)):
        results[x+3, i]  = weights[x]
    
# results_df
results_df = pd.DataFrame(results.T,columns=['ret','stdev','sharpe',tickers[0],tickers[1],tickers[2],tickers[3]])
 
# locate position of portfolio with highest Sharpe Ratio
max_sharpe_port = results_df.iloc[results_df['sharpe'].idxmax()]

# locate positon of portfolio with minimum standard deviation
min_vol_port = results_df.iloc[results_df['stdev'].idxmin()]
 
#create scatter plot coloured by Sharpe Ratio
plt.scatter(results_df.stdev,results_df.ret,c=results_df.sharpe,cmap='RdYlBu')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.title('Markowitz Efficient Frontier with Sharpe Ratio')
plt.colorbar()
#plot red star to highlight position of portfolio with highest Sharpe Ratio
plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
#plot green star to highlight position of minimum variance portfolio
plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=1000)    
plt.savefig('Markowitz-Efficient-Frontier-with-Sharpe-Ratio.png', 
    bbox_inches = 'tight', dpi=None, facecolor='w', edgecolor='b', 
    orientation='portrait', papertype=None, format=None, 
    transparent=False, pad_inches=0.25, frameon=None)
plt.show()
plt.close()
