import pandas as pd
import numpy as np
import yfinance as yf
from ta import trend
import matplotlib.pyplot as plt
import mplcursors
import math

data = yf.download("^NSEBANK", start="2023-01-01", end="2023-05-01")
df = data.reset_index()
lst=[0]

for i in range(79):
    if(i!=0):
        a=math.log(df['Close'][i]/df['Close'][i-1])
        lst.append(a)
df['LOG_R']=lst
iv=df['LOG_R'].tolist()
d=np.array(iv)
std=np.std(d)
print(df)
print("the Implied volatility is",std)
