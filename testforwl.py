import scipy
import os
from scipy.stats import median_abs_deviation
from scipy.stats import iqr
from scipy.integrate import simpson
from numpy import trapz
from scipy import fftpack
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"D:\teststuff")
df = pd.read_csv(r"D:\teststuff\lcdata.csv")
maxvalsd = df['SD_I'].max()
minvalsd = df['SD_I'].min()
truminvalsd = -minvalsd
sumthing = maxvalsd+truminvalsd
ampsd = sumthing/2
meansd = df['SD_I'].mean()
mediansd = df['SD_I'].median()
varsd = df['SD_I'].var()
stdsd = df['SD_I'].std()
#madsd=1
#madsd = df['SD_I'].apply(median_abs_deviation)
skewsd = df['SD_I'].skew()
kurtsd = df['SD_I'].kurtosis()
iqrsd = iqr(df['SD_I'])
#newcols={'Amp':ampsd,'Mean':meansd,'Median':mediansd,'Variance':varsd,'Standard Deviation':stdsd, 'MAD':madsd,'Skewness':skewsd,'Kurtosis':kurtsd,'Interquartile Range':iqrsd}
newcols={'Amp':[ampsd],'Mean':[meansd],'Median':[mediansd],'Variance':[varsd],'Standard Deviation':[stdsd],'Skewness':[skewsd],'Kurtosis':[kurtsd],'Interquartile Range':[iqrsd]}
df2 = pd.DataFrame(data=newcols)
df['Charge'] = trapz(abs(df['SD_I']),dx=0.00016)
sd1 = df['Charge'].values
df2 = pd.concat([df2, pd.DataFrame({'Amp':[25]})],ignore_index=True)
ffttrial = fftpack.fft(sd1)
v = 3*299792458
freq = 1/0.33
ampl = np.abs(ffttrial)
wl = v/freq
print(wl)
#df2.to_csv('testfile.csv',index=False)
plt.plot(df['Time'],df['SD_I'])
#plt.plot(df['Time'],df['Charge'])

plt.show()

