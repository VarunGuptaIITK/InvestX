import pandas as pd
import numpy as np
import yfinance as yf
from ta import trend
import matplotlib.pyplot as plt
import mplcursors
data = yf.download("^NSEBANK", start="2023-01-01", end="2023-05-01")
df = data.reset_index()
#MF = [(Close - Low) - (High - Close)] / (High - Low)
#MFV = MF * Volume
ls=[]
Mfv=[]
Adl=0
adl=[]
for i in range(79):
    close=df['Close'][i]
    low=df['Low'][i]
    high=df['High'][i]
    k=((close-low)-(high-close))/(high-low)
    p=k*df['Volume'][i]
    adl.append(Adl)
    Adl+=p
    
    Mfv.append(p)
    ls.append(k)

df['MF']=ls
df['MFV']=Mfv
df['ADL']=adl
df.plot(x='Date',y='ADL')
plt.show()
