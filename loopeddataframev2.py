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
    col_data=df.iloc[:,i]
    col_datadf=pd.DataFrame(data=col_data)
    maxvalsd = col_data.max()
    minvalsd = col_data.min()
    truminvalsd = -minvalsd
    sumthing = maxvalsd+truminvalsd
    ampsd = sumthing/2
    meansd = col_data.mean()
    mediansd = col_data.median()
    varsd = col_data.var()
    stdsd = col_data.std()
#madsd=1
#madsd = df[i].apply(median_abs_deviation)
    skewsd = col_data.skew()
    kurtsd = col_data.kurtosis()
    q1sd = np.percentile(col_data,25)
    q3sd = np.percentile(col_data,75)
    iqr = q3sd-q1sd
    df2 = pd.concat([df2, pd.DataFrame({'Amp':[ampsd],'Mean':[meansd],'Median':[mediansd],'Variance':[varsd],'Standard Deviation':[stdsd],'Skewness':[skewsd],'Kurtosis':[kurtsd],'Quartile1':[q1sd],'Quartile3':[q3sd],'Interquartile Range':[iqr]})],ignore_index=True)

df2.to_csv('testfile2.csv',index=False)


