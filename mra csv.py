import scipy
from scipy.stats import median_abs_deviation
from scipy.stats import iqr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"D:\teststuff\lcdata.csv")
maxvalsd = df['SD_I'].max()
minvalsd = df['SD_I'].min()
sumthing = maxvalsd+minvalsd
ampsd = sumthing/2
meansd = df['SD_I'].mean()
mediansd = df['SD_I'].median()
varsd = df['SD_I'].var()
stdsd = df['SD_I'].std()
madsd = df['SD_I'].apply(median_abs_deviation)
skewsd = df['SD_I'].skew()
kurtsd = df['SD_I'].kurtosis()
iqrsd = iqr(df['SD_I'])
newcols={'Amp':ampsd,'Mean':meansd,'Median':mediansd,'Variance':varsd,'Standard Deviation':stdsd, 'MAD':madsd,'Skewness':skewsd
         ,'Kurtosis':kurtsd,'Interquartile Range':iqrsd}
df2 = pd.DataFrame(newcols)
df2.to_csv('testfile.csv',index=False)

