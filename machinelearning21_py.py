# -*- coding: utf-8 -*-
"""machineLearning21.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iAfvPistsQx3qaYvhjgTHTwnfNeOVNaG
"""

from tensorflow.keras.datasets import imdb
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

(train_input, train_target), (test_input, test_target) = imdb.load_data(
    num_words =500
)

train_input, val_input, train_target, val_target = train_test_split(
    train_input, train_target, test_size = 0.2, random_state = 42
)

train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)

print(train_seq)
model = keras.Sequential()

model.add(keras.layers.Embedding(500, 16, input_length = 100))
# model.add(keras.layers.LSTM(8, dropout= 0.3, return_sequences=True))
# model.add(keras.layers.LSTM(8, dropout= 0.3))
model.add(keras.layers.GRU(8))

model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()

rmsprops = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer= rmsprops, loss='binary_crossentropy', metrics='accuracy')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-lstm-model.h5', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience= 3, restore_best_weights=True)

history = model.fit(train_seq, train_target, epochs=100, batch_size=64,
                    validation_data = (val_seq, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['train','val'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()


plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['train','val'])
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()