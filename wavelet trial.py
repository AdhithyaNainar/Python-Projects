import os
import numpy as np
import pandas as pd
import pywt
import pywt.data
import matplotlib.pyplot as plt
a=0
os.chdir(r"D:\teststuff")
df = pd.read_csv(r"D:\teststuff\noisered.csv")
df2 = pd.read_csv(r"D:\teststuff\wowfile.csv")
totsum = df['intensity2626'].sum()
df['normalize'] = df['intensity2626']/30000
print(df['normalize'])
print(totsum)
dwtcoeff = pywt.wavedec(df['normalize'],'db4',mode='symmetric')
filtdat = pywt.waverec(dwtcoeff,'db4',mode='symmetric',axis=-1)
dwtcoeff[-1] = np.zeros_like(dwtcoeff[-1])
dwtcoeff[-2] = np.zeros_like(dwtcoeff[-2])
dwtcoeff[-3] = np.zeros_like(dwtcoeff[-3])
dwtcoeff[-4] = np.zeros_like(dwtcoeff[-4])
dwtcoeff[-5] = np.zeros_like(dwtcoeff[-5])
dwtcoeff[-6] = np.zeros_like(dwtcoeff[-6])
dwtcoeff[-7] = np.zeros_like(dwtcoeff[-7])
dwtcoeff[-8] = np.zeros_like(dwtcoeff[-8])


#for i in range(0,100):
    #df.plot(x)
#df.plot(x='wl',y='intensity3390')
df.plot(x='wl',y='normalize',color='red')
plt.plot(filtdat,color='black')
#df2=df2.drop(columns=['wl'])
#print(df.idxmax(axis=1))
plt.show()