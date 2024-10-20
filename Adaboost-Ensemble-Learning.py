import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier

# Load the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=names)
array = dataframe.values

# Split the dataset into features and target
X = array[:, 0:8]
y = array[:, 8]

# Set up the AdaBoost model
num_trees = 30
seed = 7
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed, algorithm='SAMME')  # Specify 'SAMME'

# Evaluate the model using cross-validation
result = model_selection.cross_val_score(model, X, y)
print(result.mean())
