import time
import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow import keras

# import matplotlib.pyplot as plt

start = time.time()

df = pd.read_csv('mnist-train.csv')
y_train = keras.utils.to_categorical(df['label'], 10)
x_train = df.values[:,1:]
x_train = x_train.reshape(60000, 28, 28, 1)
x_train = x_train / 255

end = time.time()

print(end - start, 'secs to load training data')

start = time.time()

df = pd.read_csv('mnist-test.csv')
y_test = keras.utils.to_categorical(df['label'], 10)
x_test = df.values[:,1:]
x_test = x_test.reshape(10000, 28, 28, 1)
x_test = x_test / 255

end = time.time()

print(end - start, 'secs to load test data')

print(x_test)

model = keras.Sequential([
    keras.layers.Conv2D(12, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.Conv2D(20, kernel_size=(3,3), activation='relu'),
    keras.layers.Conv2D(20, kernel_size=(3,3), activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=2, validation_split=0.2)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test Accuracy:', test_acc)

model.save('digits.h5')

predictions = model.predict(test_img)
print(predictions[0], test_lbl[0])
