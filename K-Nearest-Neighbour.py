import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
df=pd.read_csv("/content/diabetes.csv")
df.head()

df.shape
df.dtypes
x=df.drop('Outcome', axis=1).values
y=df['Outcome'].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

from sklearn.neighbors import KNeighborsClassifier
neighbors = np.arange(1,20)
train_accuracy =np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i,k in enumerate(neighbors):
   knn = KNeighborsClassifier(n_neighbors=k)
   knn.fit(x_train, y_train)
   train_accuracy[i] = knn.score(x_train, y_train)
   test_accuracy[i] = knn.score(x_test, y_test)

plt.title('k-NN Varying number of neighbors')
plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(neighbors, train_accuracy, label='Training accuracy')
plt.legend()
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.show()
