import pandas as pd
import numpy as np

def get_tickers():
  data = pd.read_csv("Data/nasdaq_screener_1740024491187.csv")
  data = data["Symbol"]
  data.to_csv('Data/nasdaq_tickers.csv', index = False)

'''
Splits 'arr' into 'n' sub arrays
If the split is not even, 
  the necessary ammount of items will be skipped at the begining of array
'''
def split_array(arr, n):
  window = arr.shape[0] // n
  excess = arr.shape[0] % n
  
  chunks = []
  i = excess
  while i < arr.shape[0]:
    chunks.append(np.array(arr[ i : i + window ]))
    i = i + window

  return np.array(chunks)

x = np.array([])


