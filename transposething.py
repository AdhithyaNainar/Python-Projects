import pandas as pd
import numpy as np
import os
os.chdir(r"D:\teststuff")
print(os.getcwd())
heatmap = pd.read_csv(r"D:\teststuff\labelledcoeff.csv",header=None).T
heatmap.to_csv('heatmap2.csv',header=False,index=False)
