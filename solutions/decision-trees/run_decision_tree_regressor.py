import pandas as pd
from DecisionTreeRegressor import DecisionTreeRegressor


def test_tree(filename):
    df = pd.read_csv(filename)
    y = df.pop('Humidity').values
    X = df.values
    print(X)

    tree = DecisionTreeRegressor()
    tree.fit(X, y, df.columns)
    tree.prune(X, y)
    print(tree)

    y_predict = tree.predict(X)
    print('%35s   %10s   %10s' % ("FEATURES", "ACTUAL", "PREDICTED"))
    print('%35s   %10s   %10s' % ("----------", "----------", "----------"))
    for features, true, predicted in zip(X, y, y_predict):
        print('%35s   %10d   %10d' % (str(features), true, predicted))


if __name__ == '__main__':
    test_tree('data/playgolf.csv')
