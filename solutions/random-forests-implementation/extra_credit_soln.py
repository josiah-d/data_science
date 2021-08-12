import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score



def format_data():
    # Load in the data
    df = pd.read_csv('./data/titanic.csv')

    # Remove the Nan vals from the dataframe
    df = df.dropna()

    # 'y' is the target value we are trying to predict
    y = df['survived'].values

    # 'X' are our features, only categorical
    X = df[['pclass', 'age', 'fare']].values

    return X, y


def do_grid_search():
    # Get the data from our function above
    X, y = format_data()

    # Split it up into our training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X,y)

    # Initalize our model here
    est = GradientBoostingClassifier()

    # Here are the params we are tuning, ie, 
    # if you look in the docs, all of these are 'nobs' within the GradientBoostingClassifier algo. 
    param_grid = {'learning_rate': [0.1, 0.05, 0.02],
                  'max_depth': [2, 3],
                  'min_samples_leaf': [3, 5],
                  }

    # Plug in our model, params dict, and the number of jobs, then .fit()
    gs_cv = GridSearchCV(est, param_grid, n_jobs=2).fit(X_train, y_train)

    # return the best score and the best params
    return gs_cv.best_score_, gs_cv.best_params_



def do_regular_decision_tree(best_max_depth):
    # Get the data from our function above
    X, y = format_data()

    # Split it up into our training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X,y)

    # Initalize our decision tree algo, set the max_depth to our maximum_max_depth
    clf = DecisionTreeClassifier(max_depth=best_max_depth)
    
    # Fit our tree
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Find the precision, recall, and score
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    score = clf.score(X_test, y_test)
    return precision, recall, score


if __name__ == '__main__':
    best_score, best_grid_params =  do_grid_search()
    
    best_max_depth = best_grid_params['max_depth']
    
    print(do_regular_decision_tree(best_max_depth))
