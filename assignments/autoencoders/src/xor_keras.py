import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import os
from tensorflow.keras.callbacks import TensorBoard

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # disable Tensorflow warnings


def define_hl_mlp_model(X, nn_hl, activ='sigmoid'):
    """ Defines hidden layer mlp model
        X is the training array
        nn_hl is the desired number of neurons in the hidden layer
        activ is the activation function (could be 'tanh', 'relu', etc.)
    """
    num_coef = X.shape[1]
    model = Sequential()  # sequential model is a linear stack of layers
    model.add(Dense(units=nn_hl,
                    input_shape=(num_coef,),
                    activation=activ,
                    use_bias=True,
                    kernel_initializer='glorot_uniform',
                    bias_initializer='zeros',
                    kernel_regularizer=None,
                    bias_regularizer=None,
                    activity_regularizer=None,
                    kernel_constraint=None,
                    bias_constraint=None))
    model.add(Dense(units=1,
                    activation=activ,
                    use_bias=True,
                    kernel_initializer='glorot_uniform'))
    sgd = SGD(lr=1.0,
              decay=1e-7,
              momentum=.9)  # using stochastic gradient descent
    model.compile(loss="mean_squared_error", optimizer=sgd, metrics=["mse"])
    return model


if __name__ == '__main__':
    np.random.seed(1)

    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1],
                  [0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])

    y = np.array([[0],
                  [1],
                  [1],
                  [0],
                  [0],
                  [1],
                  [1],
                  [0]])

    nn_hl = 2  # number of neurons in the hidden layer
    num_epochs = 1000  # number of times to train on the entire training set
    batch_size = X.shape[0]  # i.e. batch gradient descent
    model = define_hl_mlp_model(X, nn_hl)

    # Added for Tensorboard
    tensorboard = TensorBoard(log_dir='./logs',
                              histogram_freq=2,
                              batch_size=batch_size,
                              write_graph=True,
                              write_grads=True,
                              write_images=True)
    # modified for Tensorboard
    model.fit(X, y,
              batch_size=batch_size,
              epochs=num_epochs,
              verbose=1,
              shuffle=True,
              validation_split=0.25,
              callbacks=[tensorboard])

    y_pred = model.predict(X)

    print("\nTraining results")
    print("yp\ty")
    for yp, yt in zip(y_pred, y):
        print("{0:0.3f}\t{1}".format(yp[0], yt[0]))
