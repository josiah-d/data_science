import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pickle


class Model(object):
    def __init__(self):
        self.model = None
        self.X = None
        self.y = None
    
    def load_data(self):
        data = load_iris()
        self.X = data.data
        self.y = data.target

    def fit_model(self):
        self.model = RandomForestClassifier()
        self.model.fit(self.X, self.y)

    def pickle_model(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.model, f)

if __name__ == '__main__':
    m = Model()
    m.load_data()
    m.fit_model()
    m.pickle_model('model.pkl')
