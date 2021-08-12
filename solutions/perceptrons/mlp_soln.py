
'''
Code implements multi-perceptron neural network to classify MNIST images of 
handwritten digits using Keras and Theano.  Based on code from
https://www.packtpub.com/books/content/training-neural-networks-efficiently-using-keras 
'''

import numpy as np
from tensorflow import keras

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
    X_train = X_train.astype('float32') #before conversion were uint8
    X_test = X_test.astype('float32')
    X_train.resize(len(y_train), 784) # 28 pix x 28 pix = 784 pixels
    X_test.resize(len(y_test), 784)
    print('\nFirst 5 labels of MNIST y_train: ', y_train[:5])
    y_train_ohe = to_categorical(y_train) 
    print('\nFirst 5 labels of MNIST y_train (one-hot):\n', y_train_ohe[:5])
    print('')
    return X_train, y_train, X_test, y_test, y_train_ohe

def define_nn_mlp_model(X_train, y_train_ohe):
    ''' defines multi-layer-perceptron neural network '''
    # available activation functions at:
    # https://keras.io/activations/
    # https://en.wikipedia.org/wiki/Activation_function
    # options: 'linear', 'sigmoid', 'tanh', 'relu', 'softplus', 'softsign'
    # there are other ways to initialize the weights besides 'uniform', too 
    
    model = Sequential() # sequence of layers
    num_neurons_in_layer = 100 # number of neurons in a layer
    num_inputs = X_train.shape[1] # number of features (784)
    num_classes = y_train_ohe.shape[1]  # number of classes, 0-9
    model.add(Dense(units=num_neurons_in_layer, 
                    input_shape=(num_inputs, ),
                    kernel_initializer='uniform', 
                    bias_initializer='zeros',
                    activation='relu')) 
    model.add(Dense(units=num_neurons_in_layer, 
                    kernel_initializer='uniform', 
                    bias_initializer='zeros',
                    activation='relu')) 
    model.add(Dense(units=num_classes,
                    kernel_initializer='uniform', 
                    bias_initializer='zeros',
                    activation='softmax')) 
    sgd = SGD(lr=0.001, decay=1e-7, momentum=.9) # using stochastic gradient descent 
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=["accuracy"] ) 
    return model 

def print_output(model, y_train, y_test, rng_seed):
    '''prints model accuracy results'''
    y_train_pred = model.predict_classes(X_train, verbose=0)
    y_test_pred = model.predict_classes(X_test, verbose=0)
    print('\nRandom number generator seed: ', rng_seed)
    print('\nFirst 30 labels:      ', y_train[:30])
    print('First 30 predictions: ', y_train_pred[:30])
    train_acc = np.sum(y_train == y_train_pred, axis=0) / X_train.shape[0]
    print('\nTraining accuracy: {0:0.2f}%'.format(train_acc * 100))
    test_acc = np.sum(y_test == y_test_pred, axis=0) / X_test.shape[0]
    print('Test accuracy: {0:0.2f}%'.format(test_acc * 100))


if __name__ == '__main__':
    rng_seed = 2 # set random number generator seed
    X_train, y_train, X_test, y_test, y_train_ohe = load_and_condition_MNIST_data() 
    np.random.seed(rng_seed)
    model = define_nn_mlp_model(X_train, y_train_ohe)
    model.fit(X_train, y_train_ohe, epochs=15, batch_size=100, verbose=1,
              validation_split=0.1) # cross val to estimate test error
    print_output(model, y_train, y_test, rng_seed)
        
