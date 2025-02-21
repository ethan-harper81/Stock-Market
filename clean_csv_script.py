import pandas as pd

data = pd.read_csv("Data/nasdaq_screener_1740024491187.csv")
data = data["Symbol"]
data.to_csv('Data/nasdaq_tickers.csv', index = False)