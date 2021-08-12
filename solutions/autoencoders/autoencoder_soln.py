import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
from plot_reconstruction import plot_reconstruction


def load_and_condition_MNIST_data():
    '''
    loads and shapes MNIST image data
    input:  None
    output: X_train (2D np array), X_test (2D np array)
    '''
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # scale pixel values to between 0 and 1
    X_train = (X_train/255).astype('float32') #before conversion were uint8
    X_test = (X_test/255).astype('float32')
    # flatten images
    X_train = X_train.reshape(-1, 784) # 28 pix x 28 pix = 784 pixels
    X_test = X_test.reshape(-1, 784)
    # note: we don't need the ys for autoencoders.
    return X_train, X_test

def autoencoder_model(X_train):
    '''
    defines autoencoder model
    input: X_train (2D np array)
    output: autoencoder (compiled autoencoder model)
    '''
    # this is our input placeholder
    input_img = Input(shape=(X_train.shape[1],))

    # first encoding layer
    encoded1 = Dense(units = 256, activation = 'relu')(input_img)

    # second encoding layer
    # note that each layer is multiplied by the layer before
    encoded2 = Dense(units = 64, activation='relu')(encoded1)

    # first decoding layer
    decoded1 = Dense(units = 256, activation='relu')(encoded2)

    # second decoding layer - this produces the output
    decoded2 = Dense(units = 784, activation='sigmoid')(decoded1)

    # this model maps an input to its reconstruction
    autoencoder = Model(input_img, decoded2)

    # compile model
    autoencoder.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics=['mse'])

    return autoencoder


if __name__ == '__main__':
    X_train, X_test = load_and_condition_MNIST_data()
    np.random.seed(42)
    model = autoencoder_model(X_train)

    batch_size = 100

    # instantiate callbacks
    tensorboard = TensorBoard(log_dir='./autoencoder_logs', histogram_freq=2, batch_size=batch_size, write_graph=True, write_grads=True, write_images=True)
    earlystopping = EarlyStopping(monitor='val_loss', patience=2)

    # try different number of epochs - 10 gives good performanace 
    model.fit(X_train, X_train, epochs=10, batch_size=batch_size, verbose=1,
              validation_split=0.1, callbacks = [earlystopping, tensorboard]) # cross val to estimate test error

    scores = model.evaluate(X_test, X_test)
    print('Test mse = {}'.format(scores[0]))

    X_test_decoded = model.predict(X_test)

    plot_reconstruction(X_test, X_test_decoded)
