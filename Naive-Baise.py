import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load dataset
db = pd.read_csv("/content/Disease.csv")
db.info()

# Label encoding for categorical features
le = LabelEncoder()
db['Sore Throad'] = le.fit_transform(db['Sore Throad'])
db['Fever'] = le.fit_transform(db['Fever'])
db['Swollen Glands'] = le.fit_transform(db['Swollen Glands'])
db['Congestion'] = le.fit_transform(db['Congestion'])
db['Headache'] = le.fit_transform(db['Headache'])
db['Diagnosis'] = le.fit_transform(db['Diagnosis'])

# Visualize counts of various symptoms
fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x=db['Sore Throad'], data=db)
plt.title("Category wise count of Sore Throad")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x=db['Congestion'], data=db)
plt.title("Category wise count of Congestion")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x=db['Headache'], data=db)
plt.title("Category wise count of Headache")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x=db['Fever'], data=db)
plt.title("Category wise count of Fever")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

fig, ax = plt.subplots(figsize=(6,6))
sns.countplot(x=db['Swollen Glands'], data=db)
plt.title("Category wise count of Swollen Glands")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Prepare data for training
x = db.drop(['Diagnosis'], axis=1)
y = db['Diagnosis']

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the Naive Bayes classifier (MultinomialNB in this case)
classifier = MultinomialNB()
classifier.fit(x_train, y_train)

# Make predictions
y_pred = classifier.predict(x_test)

# Model evaluation
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Adding zero_division=1 to avoid undefined metric warnings
print("Precision:", precision_score(y_test, y_pred, average='macro', zero_division=1))
print("Recall:", recall_score(y_test, y_pred, average='macro', zero_division=1))
print("F1 Score:", f1_score(y_test, y_pred, average='macro', zero_division=1))

# Detailed classification report
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))
