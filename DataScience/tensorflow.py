# TensorFlow is an open-source deep learning library developed by Google. It provides a flexible platform for building and training machine learning models.
import tensorflow as tf

#creating a simple neural network model
model = tf.keras.Sequential([tf.keras.layers.Dense(10,activation='relu',input_shape=(4,)),tf.keras.layers.Dense(3,activation='softmax')])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics = ['accuracy'])
#Sample data Iris dataset
from sklearn.datasets import load_iris
from sklearn.modek_selection import train_test_split
import numpy as np

iris = load_iris()
X_train,X_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)

#Training model
model.fit(X_train,y_train, epochs =10)
#Evaluating the model
loss,accuracy = model.evaluate(X_test,y_test)
print("Test Accuracy: ",accuracy)