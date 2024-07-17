import pandas as pd
import numpy as np
import yfinance as yf
from ta import trend
import matplotlib.pyplot as plt
import mplcursors
data = yf.download("AAPL", start="2023-01-01", end="2023-05-01")
df = data.reset_index()
#%K = [(Current Closing Price - Lowest Low) / (Highest High - Lowest Low)] * 100
list=[]

for i in range(81):
    close=df['Close'][i]
    low=df['Low'][i]
    high=df['High'][i]
    k=(close-low)/(high-low)
    list.append(k)
    
df['%K']=list
df['SMA'] = trend.sma_indicator(df['%K'], window=3)
df.plot(x='Date',y=['%K','SMA'])
x=df['Date'].tolist()
y=df['Open'].tolist()
fig, ax = plt.subplots()
ax.plot(x, y, 'o-')


cursor = mplcursors.cursor(ax, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[0]:.2f}, {sel.target[1]:.2f}"))

ax.set_xlabel('Date')
ax.set_ylabel('Stock price')
ax.set_title('Stock prices with time')
ax.set_xlim(x[0], x[-1])
ax.set_ylim(min(y), max(y))
ax.set_autoscale_on(False)
ax.format_coord = lambda x, y: f'({x:.2f}, {y:.2f})'
ax.set(xmargin=0.01, ymargin=0.1)
plt.gca().set_aspect('auto', adjustable='box')
plt.grid(True)

plt.show()
