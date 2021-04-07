import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# add file

#Store the data
AAPL = pd.read_csv('AAPL.csv')

#Show the data
AAPL

# Visulize
plt.figure(figsize=(12.5, 4.5))
plt.plot(AAPL['Adj Close Price'], label = 'AAPL')