import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif
from sklearn.svm import SVC
import os
os.chdir(r"D:\teststuff")

df = pd.read_csv(r"D:\teststuff\attemptnoidk3csv.csv")

npx = np.array(df.iloc[:,0])
npy = np.array(df.iloc[:,1])
x = npx.reshape(-1, 1)
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(x, npy)
new_data_point = np.array([[40]])
prediction = svm_classifier.predict(new_data_point)
print(f"Prediction for {new_data_point[0][0]} is {prediction[0]}")
#print(f"Mutual information for classification: {mi}")