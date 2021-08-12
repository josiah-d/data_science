from DecisionTree import DecisionTree
import numpy as np
from collections import Counter


class RandomForest(object):
    '''A Random Forest class'''

    def __init__(self, num_trees, num_features):
        '''
           num_trees:  number of trees to create in the forest:
        num_features:  the number of features to consider when choosing the
                           best split for each node of the decision trees
        '''
        self.num_trees = num_trees
        self.num_features = num_features
        self.forest = None

    def fit(self, X, y):
        '''
        X:  two dimensional numpy array representing feature matrix
                for test data
        y:  numpy array representing labels for test data
        '''
        self.forest = self.build_forest(X, y)

    def build_forest(self, X, y):
        '''
        Return a list of self.num_trees DecisionTrees built using bootstrap samples
        and only considering self.num_features features at each branch.
        '''
        forest = []
        for i in range(self.num_trees):
            sample_indices = np.random.choice(X.shape[0], X.shape[0],
                                              replace=True)
            sample_X = np.array(X[sample_indices])
            sample_y = np.array(y[sample_indices])
            dt = DecisionTree(num_features=self.num_features)
            dt.fit(sample_X, sample_y)
            forest.append(dt)
        return forest

    def predict(self, X):
        '''
        Return a numpy array of the labels predicted for the given test data.
        '''
        answers = np.array([tree.predict(X) for tree in self.forest]).T
        return np.array([Counter(row).most_common(1)[0][0] for row in answers])

    def score(self, X, y):
        '''
        Return the accuracy of the Random Forest for the given test data and
        labels.
        '''
        return (self.predict(X) == y).mean()

if __name__ == '__main__':
    from sklearn.model_selection import train_test_split
    import pandas as pd

    df = pd.read_csv('./data/congressional_voting.csv', names=['Party']+list(range(1, 17)))
    y = df.pop('Party').values
    X = df.values
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    rf = RandomForest(num_trees=10, num_features=(X.shape[1]//3))
    rf.fit(X_train, y_train)
    print("Random Forest score:", rf.score(X_test, y_test))
