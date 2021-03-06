# -*- coding: utf-8 -*-
"""machineLearning14.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z2C5ZKFHLO0k54-462jiFIMM4lsDvq8u
"""

import matplotlib.pyplot as plt #draw graph
import numpy as np #make array
from sklearn.decomposition import PCA #find principal component from attributes(axis)

from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import cross_validate

from sklearn.cluster import KMeans #set n number of cluster. First, randomly group elements and get mean of them. Then group again with the mean and then get mean value of them again. Repeat this process until all clusters form propery.

#require 2 dimensional array
def draw_fruits(arr, ratio=1):
  n = len(arr)
  rows = int(np.ceil(n/10))


  cols = n if rows <2 else 10

  fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)

  for i in range(rows):
    for j in range(cols):
      if i*10 + j < n:
        axs[i,j].imshow(arr[i*10+j], cmap='gray_r')
      axs[i,j].axis('off')

  plt.show()

!wget https://bit.ly/fruits_300_data -O fruits_300.npy
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100) #make the 3 dimensional array two dimensional array

pca = PCA(n_components= 50)
pca.fit(fruits_2d)

print(pca.components_.shape)

# draw_fruits(pca.components_.reshape(-1, 100, 100))

print(fruits_2d.shape)

fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

fruits_inverse = pca.inverse_transform(fruits_pca)
print(fruits_inverse.shape)

fruits_reconstruct = fruits_inverse.reshape(-1, 100,100)

# draw_fruits(fruits)
# draw_fruits(fruits_reconstruct)

print(np.sum(pca.explained_variance_ratio_))

plt.plot(pca.explained_variance_ratio_)
plt.show()

lr = LogisticRegression(max_iter = 1000)
target = np.array([0]*100+[1]*100+[2]*100) #answer sheet

scores = cross_validate(lr, fruits_2d, target)
print('test score original',np.mean(scores['test_score']))

print('fit time original',np.mean(scores['fit_time']))

scores = cross_validate(lr, fruits_pca, target)
print('test score pca 50',np.mean(scores['test_score']))

print('fit time pca 50',np.mean(scores['fit_time']))


pca = PCA(n_components = 0.5)
pca.fit(fruits_2d)
print(pca.n_components_)

fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

scores = cross_validate(lr, fruits_pca, target)
print('test score pca 0.5',np.mean(scores['test_score']))

print('fit time pca 0.5',np.mean(scores['fit_time']))


km = KMeans(n_clusters =3, random_state = 42)
km.fit(fruits_pca)

print(np.unique(km.labels_, return_counts= True))

# draw_fruits(fruits[km.labels_ ==0])
# draw_fruits(fruits[km.labels_ ==1])
# draw_fruits(fruits[km.labels_ ==2])

for label in range(0, 3):
  data = fruits_pca[km.labels_ == label]
  plt.scatter(data[:,0], data[:,1])
plt.legend(['apple', 'banana', 'pineapple'])
plt.show()