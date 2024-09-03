import pandas as pd
import numpy as np
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

t=pd.read_csv('C:\\Users\\trial\\Desktop\\EW.csv',usecols=[0])
a=pd.read_csv('C:\\Users\\trial\\Desktop\\EW.csv',usecols=[1])
n=len(a)
dt=0.02 #time increment in each data

acc=a.values.flatten() #to convert DataFrame to 1D array
#acc value must be in numpy array format for half way mirror calculation

fft=rfft(acc)*dt
freq=rfftfreq(n,d=dt)

FFT=abs(fft)

plt.plot(freq,FFT)