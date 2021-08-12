import pandas as pd

from DecisionTree import DecisionTree


def test_tree(filename):
    df = pd.read_csv(filename)
    y = df.pop('Result').values
    X = df.values
    print(X)
    
    tree = DecisionTree()
    tree.fit(X, y, df.columns)
    print(tree)
    print()

    y_predict = tree.predict(X)
    print('{:>26} {:>10} {:>10}'.format("FEATURES", "ACTUAL", "PREDICTED"))
    print('{:>26} {:>10} {:>10}'.format("----------", "----------", "----------"))
    for features, true, predicted in zip(X, y, y_predict):
        print('{!s:>26} {:>10} {:>10}'.format(features, true, predicted))


if __name__ == '__main__':
    test_tree('data/playgolf.csv')
