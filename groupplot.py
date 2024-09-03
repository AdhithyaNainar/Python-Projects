import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
clnames = ['wl', 'intensity']

#print(df)
a=0
os.chdir(r'D:\Check_OES2')
dftot = pd.DataFrame()
dftot = pd.read_csv(r'D:\Check_OES\QEP045501__29879__21-40-00-035.txt',names=clnames,header=None,delim_whitespace=True)

#dftot['wl'] = dftot['wl'].astype('float64')
print(dftot.dtypes)
for files in os.listdir(r'D:\Check_OES2'):
    a=a+1
    #print(files)
    df = pd.read_csv(files,names=clnames,header=None,delim_whitespace=True)
    dftot['intensity'+str(a)] = df['intensity']
print(dftot)




