# -*- coding: utf-8 -*-
"""MarketAndMachineLearning4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZU4bsSiSyOfN6Maz5NJSNMjCmagb5wq
"""



import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error



# # nong o , overfitting
# perch_length = [25.4,26.3,26.5,29.0,29.0,29.7,29.7,30.0,30.7,30.9,31.0,31.0,31.5,32.0,32.0,33.0,33.5,33.5,34.0,34.0]
# perch_weight= [430.3,450.0,460.0,490.0,450.0,500.0,475.0,500.0,500.0,540.0,600.0,600.0,610.0,615.0,610.0,650.0,675.0,685.0,620.0,680.0]

# underfitting
perch_length = [25.4,26.3,26.5,29.0,29.0,29.7,29.7,30.0,30.7,30.9,31.0,31.0,31.5,32.0,32.0,33.0,33.5,33.5,34.0,34.0]
perch_weight= [430.3,450.0,460.0,490.0,490.0,495.0,500.0,501.0,502.0,540.0,600.0,600.0,610.0,615.0,610.0,650.0,675.0,675.5,680.0,680.0]
# print(len(perch_length))= 20

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

#we don't need stratify for regression.
#train, test input = perch_length, and train,test target = perch_weight
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state= len(perch_length)
)

#make the arrays look like [
#  [],
#  [], 
# ]
train_input = np.array(train_input).reshape(-1,1)
test_input = np.array(test_input).reshape(-1,1)

knr = KNeighborsRegressor()
knr.fit(train_input, train_target)


test_prediction = knr.predict(test_input)
mae = mean_absolute_error(test_target, test_prediction)

# knr.n_neighbors = 9 
print("train score:",knr.score(train_input, train_target) , "\ntest score",knr.score(test_input, test_target))

# from sklearn.neighbors import KNeighborsClassifier
# ar0 = [11,22,33,44,55]
# ar1 = [1,2,3,4,5]

# a1 = np.column_stack((ar0, ar1))
# a2 = np.concatenate((np.ones(3), np.zeros(2)))


# a3, a4,a5,a6 = train_test_split(
#     a1, a2, stratify= a2, random_state=3)

# kn = KNeighborsClassifier()
# kn.fit(a3,a5)

# print(a3)