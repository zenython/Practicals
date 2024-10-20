import numpy as np
import pandas as pd
#Loading the PlayTennis data
Play_Tennis = pd.read_csv("/content/PlayTennis.csv")
Play_Tennis

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# Replacing 'Outlook' with 'outlook'
# Correcting the column assignments for Label Encoding:
Play_Tennis['outlook'] = le.fit_transform(Play_Tennis['outlook']) # Encoding 'outlook' and storing it back in 'outlook'
Play_Tennis['temp'] = le.fit_transform(Play_Tennis['temp'])       # Encoding 'temp' and storing it back in 'temp'
Play_Tennis['humidity'] = le.fit_transform(Play_Tennis['humidity']) # Encoding 'humidity' and storing it back in 'humidity'
Play_Tennis['windy'] = le.fit_transform(Play_Tennis['windy'])       # Encoding 'windy' and storing it back in 'windy'
Play_Tennis['play'] = le.fit_transform(Play_Tennis['play'])       # Encoding 'play' and storing it back in 'play'

Play_Tennis


x=Play_Tennis['play']  # Using the encoded 'play' column
y=Play_Tennis.drop('play',axis=1)  # Dropping the original 'play' column
from sklearn import tree
clf=tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(y,x)
tree.plot_tree(clf)

import graphviz
dot_data=tree.export_graphviz(clf,out_file=None)
graph=graphviz.Source(dot_data)
graph