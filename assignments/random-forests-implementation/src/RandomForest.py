from DecisionTree import DecisionTree


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
        pass

    def predict(self, X):
        '''
        Return a numpy array of the labels predicted for the given test data.
        '''
        pass

    def score(self, X, y):
        '''
        Return the accuracy of the Random Forest for the given test data and
        labels.
        '''
        pass
