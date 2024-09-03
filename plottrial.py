import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=0
sum=0
#os.chdir()
df = pd.read_csv(r"D:\teststuff\noisered.csv")
df2 = pd.read_csv(r"D:\Check_OES2\mergedcsv.csv")
for files in os.listdir(r'D:\Check_OES'):
    a=a+1
    if(a>3400):
        a=3400
    
print(sum)
#df.to_csv('noisered.csv',index='False')
#for a in range(1,100):

#plt.show()