import scipy
import os
from scipy.stats import median_abs_deviation
from scipy.stats import iqr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r"D:\teststuff")
df = pd.read_csv(r"D:\teststuff\lcdata.csv")
newcols={'Amp':[],'Mean':[],'Median':[],'Variance':[],'Standard Deviation':[],'Skewness':[],'Kurtosis':[],'Interquartile Range':[]}
df2 = pd.DataFrame(data=newcols)
for i in range(1,5):
    maxvalsd = df.iloc[:,[i]].max()
    minvalsd = df.iloc[:,[i]].min()
    truminvalsd = -minvalsd
    sumthing = maxvalsd+truminvalsd
    ampsd = sumthing/2
    meansd = df.iloc[:,[i]].mean()
    mediansd = df.iloc[:,[i]].median()
    varsd = df.iloc[:,[i]].var()
    stdsd = df.iloc[:,[i]].std()
#madsd=1
#madsd = df[i].apply(median_abs_deviation)
    skewsd = df.iloc[:,[i]].skew()
    kurtsd = df.iloc[:,[i]].kurtosis()
    #iqrsd = iqr(df[i])
    df2 = pd.concat([df2, pd.DataFrame({'Amp':[ampsd],'Mean':[meansd],'Median':[mediansd],'Variance':[varsd],'Standard Deviation':[stdsd],'Skewness':[skewsd],'Kurtosis':[kurtsd]})],ignore_index=True)

df2.to_csv('testfile2.csv',index=False)


