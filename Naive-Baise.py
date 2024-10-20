import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, CategoricalNB,GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
db=pd.read_csv("/content/Disease.csv")
db.head(11)
db.info()
le=LabelEncoder()
db['Sore Throad']=le.fit_transform(db['Sore Throad'])
db['Fever']=le.fit_transform(db['Fever'])
db['Swollen Glands']=le.fit_transform(db['Swollen Glands'])
db['Congestion']=le.fit_transform(db['Congestion'])
db['Headache']=le.fit_transform(db['Headache'])
db['Diagnosis']=le.fit_transform(db['Diagnosis'])

fig,ax=plt.subplots(figsize=(6,6))
sns.countplot(x=db['Sore Throad'],data=db)
plt.title("Catgory wise count of Sore Throad")
plt.xlabel("Catgory")
plt.ylabel("Count")
plt.show()
fig,ax=plt.subplots(figsize=(6,6))
sns.countplot(x=db['Congestion'],data=db)
plt.title("Catgory wise count of Congestion")
plt.xlabel("Catgory")
plt.ylabel("Count")
plt.show()
fig,ax=plt.subplots(figsize=(6,6))
sns.countplot(x=db['Headache'],data=db)
plt.title("Catgory wise count of Headache")
plt.xlabel("Catgory")
plt.ylabel("Count")
plt.show()
fig,ax=plt.subplots(figsize=(6,6))
sns.countplot(x=db['Fever'],data=db)
plt.title("Catgory wise count of Fever")
plt.xlabel("Catgory")
plt.ylabel("Count")
plt.show()
fig,ax=plt.subplots(figsize=(6,6))
sns.countplot(x=db['Swollen Glands'],data=db)
plt.title("Catgory wise count of Sore Throad")
plt.xlabel("Catgory")
plt.ylabel("Count")
plt.show()
x=db.drop(['Diagnosis'],axis=1)
y=db['Diagnosis']
Classifire=MultinomialNB()
classifire=CategoricalNB()
classifire.fit(x,y)
Classifire=GaussianNB()
Classifire.fit(x,y)

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
classifire = MultinomialNB()
classifire.fit(x_train, y_train)
y_pred = classifire.predict(x_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
