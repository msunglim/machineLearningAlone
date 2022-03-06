# -*- coding: utf-8 -*-
"""machineLearning9.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dIXuLYEFb-BctL2JeSU8eBq-2ArkmWla
"""

import matplotlib.pyplot as plt #draw graph
import numpy as np #make array
from sklearn.model_selection import train_test_split #split array for train/test set
import pandas as pd #use file from url
from sklearn.preprocessing import StandardScaler #make scaled array for multi variables
from sklearn.linear_model import LogisticRegression #predict a value from linear equation with given input..
from sklearn.linear_model import SGDClassifier #stochastic gradient descent. epoch epoch epoch. train train train.
from sklearn.tree import DecisionTreeClassifier #calculate decision tree probability
from sklearn.tree import plot_tree #used when drawing a graph of Decision Tree

wine = pd.read_csv('https://bit.ly/wine_csv_data')
# print(wine.head()) return fisrt n rows where default of n is 5.
# wine.info() show csv column information: non null count, dtype
# wine.describe() show column information: count, mean, std, min, max, 25%,50%,75% value

wine_data = wine[['alcohol','sugar','pH']].to_numpy()
wine_target = wine[['class']].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(
  wine_data, wine_target, test_size=0.2, random_state = 42    
)

ss= StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

lr = LogisticRegression()
lr.fit(train_scaled, train_target.ravel())

print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))

print("coefs and intercept: ",lr.coef_, lr.intercept_)

train_score =[]
test_score =[]

#show increasing score as increasing max_dpeth!
range = np.arange(1,250)
for _ in range :
  dt = DecisionTreeClassifier(max_depth = _)
  dt.fit(train_input, train_target)
  train_score.append(dt.score(train_input, train_target))
  test_score.append(dt.score(test_input, test_target))

plt.scatter(range,train_score)
plt.scatter(range,test_score)
plt.show()


# dt = DecisionTreeClassifier(random_state =42)
dt = DecisionTreeClassifier(max_depth= 3, random_state= 42)
# dt.fit(train_scaled, train_target)
dt.fit(train_input, train_target)

# print(dt.score(train_scaled, train_target))
# print(dt.score(test_scaled, test_target))
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))


plt.figure(figsize=(20,17)) #set visual width and height = 10 and 7
# plot_tree(dt, max_depth = 1, filled=True, feature_names=['alcohol', 'sugar','pH'])
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()

print(dt.feature_importances_)