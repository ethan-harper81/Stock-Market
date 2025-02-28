import yfinance as yf
import pandas as pd
import csv
import numpy as np
from utils import *

CONTEXT = 30

#add context next token pair split
def ticker_to_data(tick):

  data = yf.Ticker(tick).history(period = "5y")
  data = data[["Open", "High", "Low", "Close"]]
  return data.to_numpy()

def create_data():
  Xdata = []
  Ydata = []

  with open('Data/nasdaq_tickers.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
      cur_stock = row[0]

      print("Current Stock: ", cur_stock)

      data = ticker_to_data(cur_stock)

      print("Current stock history", data.shape[0])

      '''
      Will skip any stock that doesnt have enough context
      Will also skip stocks that could not be found
      Only issue is missing data from {ticker}^{class} stocks
      '''
      if data.shape[0] > CONTEXT + 1:
        data_points = split_array(data, CONTEXT + 1)

        print(data_points.shape)

        data_x = data_points[:CONTEXT]
        data_y = data_points[CONTEXT:]

        data_x = data_x.reshape(-1, data_x.shape[-1])
        data_y = data_y.reshape(-1, data_y.shape[-1])

        '''
        Need to think of better way to store data
        '''
        np.savetxt('./Data/datax.csv', data_x, delimiter=',')
        np.savetxt('./Data/datay.csv', data_y, delimiter=',')
        
      break

create_data()
    
