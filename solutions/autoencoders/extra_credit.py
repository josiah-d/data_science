import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
from plot_reconstruction import plot_reconstruction
from tensorflow.keras.optimizers import Adam


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
    # one hot encode ys
    y_train_ohe = one_hot_encode(y_train)
    y_test_ohe = one_hot_encode(y_test)

    return X_train, X_test, y_train_ohe, y_test_ohe

def one_hot_encode(y):
    '''
    one-hot encodes y values
    input: y (1D np array)
    output : y_ohe (2D np.array)
    '''
    return (np.arange(10).reshape(1, -1) == y.reshape(-1, 1)).astype(int)


def encoder_model(input_dim):
    '''
    helper function for autoencoder
    input: input_dim (int)
    output: encoder (keras Model object)
    '''
    # this is our input placeholder
    input_img = Input(shape=(input_dim,))

    # first encoding layer
    encoded1 = Dense(units = 256, activation = 'relu')(input_img)

    # second encoding layer
    # note that each layer is multiplied by the layer before
    encoded2 = Dense(units = 64, activation='relu')(encoded1)

    encoder = Model(input_img, encoded2)
    return encoder


def decoder_model(input_dim):
    '''
    helper function for autoencoder
    input: input_dim (int)
    output: decoder (keras Model object)
    '''
    input_img = Input(shape=(input_dim,))
    # first decoding layer
    decoded1 = Dense(units = 256, activation='relu')(input_img)

    # second decoding layer
    decoded2 = Dense(units = 784, activation='relu')(decoded1)

    decoder = Model(input_img, decoded2)
    return decoder

def autoencoder_model(X_train):
    '''
    defines autoencoder model
    input: X_train (2D np array)
    output: autoencoder (compiled autoencoder model)
    '''
    # this is our input placeholder
    input_img = Input(shape=(X_train.shape[1],))

    encoder = encoder_model(X_train.shape[1])

    decoder = decoder_model(64)

    encoded = encoder(input_img)
    decoded = decoder(encoded)

    # this model maps an input to its reconstruction
    autoencoder = Model(input_img, decoded)

    # compile model
    autoencoder.compile(optimizer = 'adam', loss = 'mean_squared_error')

    return autoencoder, encoder, decoder


def predictive_model(X_train, y_train_ohe, encoder):
    '''
    returns compiled predictive model
    input: X_train (2D)
    '''
    # turn training off for autoencoder layers
    for layer in encoder.layers[1:]:
        layer.trainable = False

    # create input placeholder
    input_img = Input(shape=(X_train.shape[1],))

    # first step - pass data through autoencoder
    decoded = encoder(input_img)

    # add one more dense layer
    dense = Dense(units = 35, activation = 'sigmoid')(decoded)
    dense = Dropout(0.25)(dense)
    # pass through predictive layer at the end
    preds = Dense(units = y_train_ohe.shape[1], kernel_initializer = 'uniform', activation = 'softmax')(dense)

    # compile model
    classifier = Model(input_img, preds)

    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy'])
    return classifier


if __name__ == '__main__':
    X_train, X_test, y_train_ohe, y_test_ohe = load_and_condition_MNIST_data()
    np.random.seed(42)

    batch_size = 100

    # instantiate callbacks
    earlystopping = EarlyStopping(monitor='val_loss', patience=2)

    autoencoder, encoder, decoder  = autoencoder_model(X_train)
    autoencoder.fit(X_train, X_train, epochs=100, batch_size=batch_size, verbose=1,
              validation_split=0.1, callbacks = [earlystopping])
    print('Done fitting autoencoder\n')
    print('Fitting classifier layers\n')

    classifier = predictive_model(X_train, y_train_ohe, encoder)
    classifier.fit(X_train, y_train_ohe, epochs=100, batch_size=batch_size, verbose=1,
              validation_split=0.1, callbacks = [earlystopping])

    # flip classifier layers to trainable and train one more time
    for layer in classifier.layers[1:]:
        layer.trainable = True

    classifier.fit(X_train, y_train_ohe, epochs=10, batch_size=batch_size, verbose=1,
              validation_split=0.1, callbacks = [earlystopping])
