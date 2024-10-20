import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import *

pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)

df=pd.read_csv("/content/diabetes.csv")
df.head()
df.shape
df.describe()
x=df.drop('Outcome',axis=1)
y=df['Outcome']
x_train=x.iloc[:600]
x_test=x.iloc[600:]
y_train=y.iloc[:600]
y_test=y.iloc[600:]
print("X_train shape",x_train.shape)
print("X_test shape",x_test.shape)
print("y_train shape",y_train.shape)
print("y_test shape",y_test.shape)

from skompiler import skompile
from sklearn.svm import SVC
support_vector_classifier=SVC(kernel='linear').fit(x_train,y_train)
support_vector_classifier
support_vector_classifier.C
support_vector_classifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
y_pred=support_vector_classifier.predict(x_test)
cm=confusion_matrix(y_test,y_pred)
cm
print("Our Accuracy is:",(cm[0][0]+cm[1][1])/(cm[0][0]+cm[1][1]+cm[0][1]+cm[1][0]))
accuracy_score(y_test,y_pred)
print(classification_report(y_test,y_pred))
support_vector_classifier
from sklearn.model_selection import cross_val_score
accuracies=cross_val_score(estimator=support_vector_classifier,X=x_train,y=y_train,cv=10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
