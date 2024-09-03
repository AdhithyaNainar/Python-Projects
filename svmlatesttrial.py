import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.feature_selection import mutual_info_classif
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import os
os.chdir(r"D:\teststuff")

df = pd.read_csv(r"D:\teststuff\attemptnoidk3csv.csv")

npx = np.array(df.iloc[:,0])
npy = np.array(df.iloc[:,1])
x = npx.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(x, npy, test_size=0.2,random_state=0)
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(x, npy)
new_data_point = np.array([[0.002]])
prediction = svm_classifier.predict(new_data_point)
disp = ConfusionMatrixDisplay.from_estimator(svm_classifier,X_test,y_test,cmap=plt.cm.Blues)
print(f"Prediction for {new_data_point[0][0]} is {prediction[0]}")
print(disp.confusion_matrix)
#print(f"Mutual information for classification: {mi}")
plt.show()