import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor

class GradientBoostedRegressor:
    """A gradient boosting class
    """
    def __init__(self,
                 n_estimators=100, 
                 learning_rate=0.1,
                 subsample=0.5,
                 model=DecisionTreeRegressor,
                 loss='mse',
                 **kwargs):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.subsample = subsample
        self.loss = loss
        self.model = model
        if loss not in ('mse', 'mae'):
            raise ValueError("Loss must be 'mse' or 'mae'")
        self.kwargs = kwargs
        self.estimators = []

    def fit(self, X, y):
        dummy = DummyRegressor()
        dummy.fit(X, y)
        self.estimators.append(dummy)
        
        # NB: it would be easier to call the predict method
        # of this model and avoid duplicated code, but that
        # adds a O(n**2) term in the number of estimators
        # because earlier estimators are called multiple
        # times during fitting
        prediction = np.zeros(len(y))
        for i in range(self.n_estimators):
            prediction = prediction + self.estimators[i].predict(X)
            
            if self.loss == 'mae':
                target = self.learning_rate * np.sign(y - prediction)
            else:
                target = self.learning_rate * (y - prediction)
            estimator = self.model(**self.kwargs)
            
            subsample_idx = np.random.choice(range(len(X)),
                                             round(self.subsample * len(X)),
                                             replace=False)
            estimator.fit(X[subsample_idx],
                          target[subsample_idx])
            self.estimators.append(estimator)

    def predict(self, X):
        predictions = np.zeros((len(self.estimators),
                                len(X)))
        for i, estimator in enumerate(self.estimators):
            predictions[i] = estimator.predict(X)

        return predictions.sum(axis=0)