# LSTM example for sine wave and stocks adapted from blog:
# http://www.jakob-aungiers.com/articles/a/LSTM-Neural-Network-for-Time-Series-Prediction
# base code from:
# https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction

from lstm import LSTM_Model
import time
import matplotlib.pyplot as plt
import numpy as np
import sys


def plot_results(predicted_data, true_data, figtitle):
    ''' use when predicting just one analysis window '''
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.title(figtitle)
    plt.savefig(figtitle + '.png')
    plt.show()
    plt.close()
    print('Plot saved.')


def plot_results_multiple(predicted_data, true_data, prediction_len, figtitle):
    ''' use when predicting multiple analyses windows in data '''
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    # Pad the list of predictions to shift it in the graph to its correct start
    for i, data in enumerate(predicted_data):
        if i != 0:
            padding = [None for p in range(i * prediction_len)]
            plt.plot(padding + data, label='Prediction')
            plt.legend()
    plt.title(figtitle)
    plt.savefig(figtitle + '.png')
    plt.show()
    plt.close()
    print('Plot saved.')


if __name__ == '__main__':

    sine = 'sine' in sys.argv

    if sine:
        print("\n>> Analyzing sine wave")
        filename = 'data/sinwave.csv'
        normalize = False
        lstm_structure = {'first_layer_units': 10,
                          'second_layer_units': 50,
                          'dense_layer_units': 1}

        fit_parameters = {'batch_size': 512,
                          'epochs': 10,
                          'validation_split': 0.05}
    else:
        print("\n>> Analyzing stock price")
        filename = 'data/sp500.csv'
        normalize = True
        lstm_structure = {'first_layer_units': 30,
                          'second_layer_units': 50,
                          'dense_layer_units': 1}

        fit_parameters = {'batch_size': 512,
                          'epochs': 10,
                          'validation_split': 0.05}

    lstm_model = LSTM_Model()
    X_train, y_train, X_test, y_test = lstm_model.load_data(filename,
                                                            lstm_structure['first_layer_units'],
                                                            normalize)
    lstm_model.build_model(**lstm_structure)
    lstm_model.fit(X_train, y_train, **fit_parameters)

    # plot results
    if sine:
        predicted = lstm_model.predict_point_by_point(X_test)
        plot_results(predicted, y_test, 'Sine_wave-predict_one_point_ahead')

        predicted_full = lstm_model.predict_sequence_full(X_test,
                                                          lstm_structure['first_layer_units'])
        plot_results(predicted_full,
                     y_test,
                     'Sine_wave-predict_full_sequence_from_start_seed')
    else:
        predictions = lstm_model.predict_sequences_multiple(X_test,
                                                            lstm_structure['first_layer_units'],
                                                            lstm_structure['first_layer_units'])
        plot_results_multiple(predictions,
                              y_test,
                              lstm_structure['first_layer_units'],
                              'Stock_prediction')
