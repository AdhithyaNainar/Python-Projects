import pandas as pd
import numpy as np
import os
os.chdir(r"D:\teststuff")
print(os.getcwd())
heatmap = pd.read_csv(r"D:\teststuff\lcdata.csv",header=None).T
heatmap.to_csv('translcdata.csv',header=False,index=False)
