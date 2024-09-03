import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os
os.chdir(r"D:\teststuff")

df = pd.read_csv(r"D:\teststuff\heatmap3.csv",header=None)
#print(df)
#df.to_csv('labelledcoeff2.csv',index=False)
df2 = df.corr().abs()
df.columns = ['SD','DB','BL','TR']
df.index = ['Type','Amp','Mean','Median','Variance','Standard Deviation','Skewness','Kurtosis','Interquartile Range','Quartile1','Quartile3','K3/K1','K5/K1','K5/K3','THD']

print(df.columns)
print(df.index)
labels = ['Type','Amp','Mean','Median','Variance','Standard Deviation','Skewness','Kurtosis','Interquartile Range','Quartile1','Quartile3','K3/K1','K5/K1','K5/K3','THD']
nparr = df.to_numpy()
r = np.corrcoef(nparr)
coeffdf = pd.DataFrame(data=r)
#print(r)
plt.subplots(figsize=(20,10))
#print(df2)
#plt.figure(figsize=(14,8))
sns.heatmap(r, xticklabels=labels,yticklabels=labels, annot=True, cmap='coolwarm')
plt.show()