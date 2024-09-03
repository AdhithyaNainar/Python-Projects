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
import math
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
Fs = 6250
tstep = 0.00016
f0 = 50

N = 2000
t = df['Time'].values

fstep = Fs/N
f = np.linspace(0, (N-1)*fstep, N)
y = df['DB_I'].values

x = np.fft.fft(y)
x_mag = np.abs(x)/N
xmagdf = pd.DataFrame(data=x_mag)


fdf = pd.DataFrame(data=f)
xmagdf = pd.concat([xmagdf, fdf], axis=1, join='inner')
harm1sd = 5.47187126174719
harm3sd = 1.11354587602548
sqharm3sd = harm3sd**2
harm5sd = 0.66664654357869
sqharm5sd = harm5sd**2
sumharmsqsd = sqharm3sd+sqharm5sd
rootsumsd = math.sqrt(sumharmsqsd)
sdthd = rootsumsd/harm1sd
#print(sdthd)
k3k1sd = harm3sd/harm1sd
#print(k3k1sd)
k5k1sd = harm5sd/harm1sd
#print(k5k1sd)
k5k3sd = harm5sd/harm3sd
#print(k5k3sd)


harm1db=0.687558158160758
sqharm1db = harm1db**2
harm3db=0.283852192002219
sqharm3db = harm3db**2
harm5db=0.050251326430939
sqharm5db = harm5db**2
sumharmsqdb = sqharm3db+sqharm5db
rootsumqb = math.sqrt(sumharmsqdb)
dbthd = rootsumqb/harm1db
#print(dbthd)
k3k1db = harm3db/harm1db
#print(k3k1db)
k5k1db = harm5db/harm1db
#print(k5k1db)
k5k3db = harm5db/harm3db
#print(k5k3db)




harm1bl = 13.8215698311455
harm3bl = 2.1069476473014
sqharm3bl = harm3bl**2
harm5bl = 1.41154101017304
sqharm5bl = harm5bl**2
sumharmsqbl = sqharm3bl+sqharm5bl
rootsumsqbl = math.sqrt(sumharmsqbl)
blthd = rootsumsqbl/harm1bl
#print(blthd)
k3k1bl = harm3bl/harm1bl
#print(k3k1bl)
k5k1bl = harm5bl/harm1bl
#print(k5k1bl)
k5k3bl = harm5bl/harm3bl
#print(k5k3bl)



harm1tr = 24.2248884829731
harm3tr = 0.472501823858657
sqharm3tr = harm3tr**2
harm5tr = 0.258182679362657
sqharm5tr = harm5tr**2
sumharmsqtr = sqharm3tr+sqharm5tr
rootsumsqtr = math.sqrt(sumharmsqtr)
trthd = rootsumsqtr/harm1tr
print(trthd)
k3k1tr = harm3tr/harm1tr
#print(k3k1tr)
k5k1tr = harm5tr/harm1tr
#print(k5k1tr)
k5k3tr = harm5tr/harm3tr
#print(k5k3tr)












xmagdf.to_csv('xmagdb.csv',index=False) 



#df2.to_csv('testfile.csv',index=False)

#plt.plot(df['Time'],df['SD_I'])
#plt.plot(f,x_mag)
#plt.xlim(0,500)
#plt.plot(df['Time'],df['Charge'])

plt.show()

