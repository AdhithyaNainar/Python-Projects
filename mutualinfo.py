import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
#from sklearn import feature_selection
from sklearn import svm
os.chdir(r"D:\teststuff")
dfx = pd.read_csv(r"D:\teststuff\translcdata3.csv",header=None)
npx = dfx.values
#print(npx.shape)
#print(npx)
dfy = pd.read_csv(r"D:\teststuff\mutualinfotableY2.csv",header=None)
npy = np.array(dfx['Type'])
print(npy.shape)
#clf = svm.SVC()
#print(clf.fit(npx[0:12],npy))
#print(clf.score(npx,npy))
X_train, X_test, y_train, y_test = train_test_split(npx,npy,test_size=0.3)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train,y_train)
y_pred = svclassifier.predict(X_test)
print(y_pred)
print(classification_report(y_test,y_pred))
#clf.predict([1.39063830e+01 -2.68608908e-01 -2.93000000e-01  6.46109841e+01 8.03809580e+00  5.73869008e-02 -1.11406766e+00 -7.61191489e+00 7.02638298e+00  1.46382979e+01  2.03503669e-01  1.21831548e-01 5.98670031e-01  2.37184884e-01])
#print(classdf)