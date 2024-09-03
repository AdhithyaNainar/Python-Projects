import os
import numpy as np
from numpy.fft import rfft, rfftfreq
import pandas as pd
import matplotlib.pyplot as plt
a=0
os.chdir(r"D:\teststuff")
df = pd.read_csv(r"D:\teststuff\noisered.csv")
df2 = pd.read_csv(r"D:\teststuff\wowfile.csv")
a = df['intensity2626']
n = len(df['intensity2626'])
print(n)
dt=0.02
Fs = 6250
tstep = 0.00016
f0 = 50

N = 1044
t = df['wl'].values

fstep = Fs/N
f = np.linspace(0, (N-1)*fstep, N)
y = df['intensity2626'].values

x = np.fft.fft(y)
x_mag = np.abs(x)/N
xmagdf = pd.DataFrame(data=x_mag)


fdf = pd.DataFrame(data=f)
xmagdf = pd.concat([xmagdf, fdf], axis=1, join='inner')



plt.plot(df['wl'],df['intensity2626'])
plt.xlim(0,1000)









#fft=fft(df2['intensity2626'])
#freq=rfftfreq(n,)
#n1=len(freq)
#FFT=abs(fft)
#print(len(FFT))
#print(len(freq))
#plt.plot(freq,FFT)
#for i in range(0,100):
    #df.plot(x)
#df.plot(x='wl',y='intensity3390')
#df2.plot(x='wl',y='intensity2626',color='red')
#df2=df2.drop(columns=['wl'])
#print(df.idxmax(axis=1))
plt.show()