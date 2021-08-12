import numpy as np
from keras.datasets import mnist


def load_and_condition_MNIST_data():
    '''
    loads and shapes MNIST image data
    input:  None
    output: X_train (2D np array), X_test (2D np array)
    '''
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # scale pixel values to between 0 and 1
    X_train = (X_train/255).astype('float32')  # before conversion were uint8
    X_test = (X_test/255).astype('float32')
    # flatten images
    X_train = X_train.reshape(-1, 784)  # 28 pix x 28 pix = 784 pixels
    X_test = X_test.reshape(-1, 784)
    # note: we don't need the ys for autoencoders.
    return X_train, X_test


def autoencoder_model(X_train):
    '''
    defines autoencoder model
    input: X_train (2D np array)
    output: autoencoder (compiled autoencoder model)
    '''
    # your code here
    pass


if __name__ == '__main__':
    X_train, X_test = load_and_condition_MNIST_data()

    np.random.seed(42)

    model = autoencoder_model(X_train)

    model.fit(X_train, X_train,
              epochs=100,
              batch_size=100,
              verbose=1,
              validation_split=0.1)  # cross val to estimate test error

    # your code here
