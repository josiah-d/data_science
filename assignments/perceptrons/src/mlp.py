'''
Code implements multi-perceptron neural network to classify MNIST images of
handwritten digits using Keras and Tensorflow.  Based on code from
https://www.packtpub.com/books/content/training-neural-networks-efficiently-using-keras

'''

import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def load_and_condition_MNIST_data():
    ''' loads and shapes MNIST image data '''
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    print("\nLoaded MNIST images")
    X_train = X_train.astype(np.float32) #before conversion were uint8
    X_test = X_test.astype(np.float32)
    X_train.resize(len(y_train), 784) # 28 pix x 28 pix = 784 pixels
    X_test.resize(len(y_test), 784)
    print('\nFirst 5 labels of MNIST y_train: {}'.format(y_train[:5]))
    y_train_ohe = to_categorical(y_train) # one hot encode the target
    print('\nFirst 5 labels of MNIST y_train (one-hot):\n{}'.format(y_train_ohe[:5]))
    print()
    return X_train, y_train, X_test, y_test, y_train_ohe


if __name__ == '__main__':
    X_train, y_train, X_test, y_test, y_train_onehot = load_and_condition_MNIST_data()    
