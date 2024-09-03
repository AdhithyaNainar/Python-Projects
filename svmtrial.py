import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import os
os.chdir(r"D:\teststuff")

df = pd.read_csv(r"D:\teststuff\translcdata.csv")

x = df.drop('Type',axis=1)
y = df['Type']

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train,y_train)
y_pred = svclassifier.predict(X_test)
print(classification_report(y_test,y_pred))