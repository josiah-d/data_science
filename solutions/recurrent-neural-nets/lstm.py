import warnings
import numpy as np
from time import time
from numpy import newaxis
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import LSTM

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hide messy TensorFlow warnings
warnings.filterwarnings("ignore")  # Hide messy Numpy warnings


class LSTM_Model:
    def __init__(self):
        self.model = None

    def load_data(self, filename, seq_len, normalize_window):
        print('>> Loading data...')
        f = open(filename, 'rb').read()
        data = f.decode().split('\n')
        data = [float(num) for num in data]

        sequence_length = seq_len + 1
        result = []
        for index in range(len(data) - sequence_length):
            result.append(data[index: index + sequence_length])

        if normalize_window:
            result = self._normalize_windows(result)

        result = np.array(result)
        row = round(0.9 * result.shape[0])
        train = result[:int(row), :]
        np.random.shuffle(train)
        X_train = train[:, :-1].reshape(-1, seq_len, 1)
        y_train = train[:, -1]
        X_test = result[int(row):, :-1].reshape(-1, seq_len, 1)
        y_test = result[int(row):, -1]

        return X_train, y_train, X_test, y_test

    def _normalize_windows(self, window_data):
        normalized_data = []
        for window in window_data:
            normalized_window = [((float(p) / float(window[0])) - 1)
                                 for p in window]
            normalized_data.append(normalized_window)
        return normalized_data

    def build_model(self,
                    first_layer_units,
                    second_layer_units,
                    dense_layer_units):
        print('>> Building model...')
        model = Sequential()

        model.add(LSTM(
            units=first_layer_units,
            return_sequences=True))
        model.add(Activation("tanh"))
        model.add(Dropout(0.2))

        model.add(LSTM(
            units=second_layer_units,
            return_sequences=False))
        model.add(Activation("tanh"))
        model.add(Dropout(0.2))

        model.add(Dense(
            units=dense_layer_units))
        model.add(Activation("linear"))

        model.compile(loss="mse", optimizer="rmsprop")
        print('>> Compiled...')
        self.model = model
        return model

    def fit(self, X, y, batch_size=256, epochs=10, validation_split=0.05):
        start_time = time()
        print('>> Fitting model...')
        self.model.fit(X, y,
                       batch_size=batch_size,
                       epochs=epochs,
                       validation_split=validation_split)
        elapsed_time = time() - start_time
        print('>> Completed')
        print('>> Training duration (s): {0}'.format(elapsed_time))
        return self.model

    def predict_point_by_point(self, data):
        # Predict each timestep given the last sequence of true data,
        # in effect only predicting 1 step ahead each time
        return self.model.predict(data).reshape(-1, )

    def predict_sequence_full(self, data, window_size):
        # Shift the window by 1 new prediction each time,
        # re-run predictions on new window
        curr_frame = data[0]
        predicted = []
        for i in range(len(data)):
            predicted.append(self.model.predict(curr_frame[newaxis, :, :])[0, 0])
            curr_frame = curr_frame[1:]
            curr_frame = np.insert(curr_frame,
                                   [window_size-1],
                                   predicted[-1],
                                   axis=0)
        return predicted

    def predict_sequences_multiple(self, data, window_size, prediction_len):
        # Predict sequence of 50 steps before
        # shifting prediction run forward by 50 steps
        prediction_seqs = []
        for i in range(int(len(data)/prediction_len)):
            curr_frame = data[i*prediction_len]
            predicted = []
            for j in range(prediction_len):
                predicted.append(self.model.predict(curr_frame[newaxis, :, :])[0, 0])
                curr_frame = curr_frame[1:]
                curr_frame = np.insert(curr_frame,
                                       [window_size-1],
                                       predicted[-1],
                                       axis=0)
            prediction_seqs.append(predicted)
        return prediction_seqs
