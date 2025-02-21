import yfinance as yf
import pandas as pd
import csv
import numpy as np

CONTEXT = 30

#add context next token pair split
def ticker_to_data(tick):

  data = yf.Ticker(tick).history(period = "5y")
  data = data[["Open", "High", "Low", "Close"]]
  return data.to_numpy()

with open('Data/nasdaq_tickers.csv', 'r') as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    ticker = row[0]
    