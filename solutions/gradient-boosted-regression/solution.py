# Note that this is the completed final solution. Please refer to the notebook
# for step-by-step solution.
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import textwrap

def load_and_split_data():
    ''' Loads sklearn's boston dataset and splits it into train:test datasets
        in a ratio of 80:20. Also sets the random_state for reproducible 
        results each time model is run.
    
        Parameters: None

        Returns:  (X_train, X_test, y_train, y_test):  tuple of numpy arrays
                  column_names: numpy array containing the feature names
    '''
    boston = load_boston() #load sklearn's dataset 
    X, y = boston.data, boston.target
    column_names = boston.feature_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                       test_size = 0.2, 
                                       random_state = 1)
    return (X_train, X_test, y_train, y_test), column_names


def cross_val(estimator, X_train, y_train, nfolds):
    ''' Takes an instantiated model (estimator) and returns the average
        mean square error (mse) and coefficient of determination (r2) from
        kfold cross-validation.

        Parameters: estimator: model object
                    X_train: 2d numpy array
                    y_train: 1d numpy array
                    nfolds: the number of folds in the kfold cross-validation

        Returns:  mse: average mean_square_error of model over number of folds
                  r2: average coefficient of determination over number of folds
    
        There are many possible values for scoring parameter in cross_val_score.
        http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

        kfold is easily parallelizable, so set n_jobs = -1 in cross_val_score
    '''
    mse = cross_val_score(estimator, X_train, y_train, 
                          scoring='neg_mean_squared_error',
                          cv=nfolds, n_jobs=-1) * -1
    # mse multiplied by -1 to make positive
    r2 = cross_val_score(estimator, X_train, y_train, 
                         scoring='r2', cv=nfolds, n_jobs=-1)
    mean_mse = mse.mean()
    mean_r2 = r2.mean()
    name = estimator.__class__.__name__
    print("{0:<25s} Train CV | MSE: {1:0.3f} | R2: {2:0.3f}".format(name,
                                                        mean_mse, mean_r2))
    return mean_mse, mean_r2
    
def plot_stage_score(ax, estimator, X_train, y_train, X_test, y_test):
    '''
        Parameters: ax: a Matplotlib axis object, on which the graph will be plotted
                    estimator: GradientBoostingRegressor
                    X_train: 2d numpy array
                    y_train: 1d numpy array
                    X_test: 2d numpy array
                    y_test: 1d numpy array

        Returns: A plot of the number of iterations vs the MSE for the model for
        both the training set and test set.
    '''
    estimator.fit(X_train, y_train)
    name = estimator.__class__.__name__.replace('Regressor', '')
    learn_rate = estimator.learning_rate
    # initialize 
    train_scores = np.zeros((estimator.n_estimators,), dtype=np.float64)
    test_scores = np.zeros((estimator.n_estimators,), dtype=np.float64)
    # Get train score from each boost
    for i, y_train_pred in enumerate(estimator.staged_predict(X_train)):
        train_scores[i] = mean_squared_error(y_train, y_train_pred)
    # Get test score from each boost
    for i, y_test_pred in enumerate(estimator.staged_predict(X_test)):
        test_scores[i] = mean_squared_error(y_test, y_test_pred)
    ax.plot(train_scores, alpha=.5, label="{0} Train - learning rate {1}".format(
                                                                name, learn_rate))
    ax.plot(test_scores, alpha=.5, label="{0} Test  - learning rate {1}".format(
                                                      name, learn_rate), ls='--')
    ax.set_title(name, fontsize=16, fontweight='bold')
    ax.set_ylabel('MSE', fontsize=14)
    ax.set_xlabel('Iterations', fontsize=14)
    ax.legend()

def plot_rf_score(ax, randforest, X_train, y_train, X_test, y_test):
    '''
        Parameters: ax: a Matplotlib axis object, on which the graph will be plotted
                    randforest: RandomForestRegressor
                    X_train: 2d numpy array
                    y_train: 1d numpy array
                    X_test: 2d numpy array
                    y_test: 1d numpy array

        Returns: The prediction of a random forest regressor on the test set
    '''
    randforest.fit(X_train, y_train)
    y_test_pred = randforest.predict(X_test)
    test_score = mean_squared_error(y_test, y_test_pred)
    ax.axhline(test_score, 
               alpha = 0.7, 
               c = 'y', 
               lw=3, 
               ls='-.', 
               label ='Random Forest Test')
    ax.legend()

def gridsearch_with_output(estimator, parameter_grid, X_train, y_train):
    '''
        Parameters: estimator: the type of model (e.g. RandomForestRegressor())
                    paramter_grid: dictionary defining the gridsearch parameters
                    X_train: 2d numpy array
                    y_train: 1d numpy array

        Returns:  best parameters and model fit with those parameters
    '''
    model_gridsearch = GridSearchCV(estimator,
                                    parameter_grid,
                                    n_jobs=-1,
                                    verbose=True,
                                    scoring='neg_mean_squared_error')
    model_gridsearch.fit(X_train, y_train)
    best_params = model_gridsearch.best_params_ 
    model_best = model_gridsearch.best_estimator_
    print("\nResult of gridsearch:")
    print("{0:<20s} | {1:<8s} | {2}".format("Parameter", "Optimal", "Gridsearch values"))
    print("-" * 55)
    for param, vals in parameter_grid.items():
        print("{0:<20s} | {1:<8s} | {2}".format(str(param), 
                                                str(best_params[param]),
                                                str(vals)))
    return best_params, model_best



def display_default_and_gsearch_model_results(model_default, model_gridsearch, 
                                              X_test, y_test):
    '''
        Parameters: model_default: fit model using initial parameters
                    model_gridsearch: fit model using parameters from gridsearch
                    X_test: 2d numpy array
                    y_test: 1d numpy array
        Return: None, but prints out mse and r2 for the default and model with
                gridsearched parameters
    '''
    name = model_default.__class__.__name__.replace('Regressor', '') # for printing
    y_test_pred = model_gridsearch.predict(X_test)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)
    print("Results for {0}".format(name))
    print("Gridsearched model mse: {0:0.3f} | r2: {1:0.3f}".format(mse, r2))
    y_test_pred = model_default.predict(X_test)
    mse = mean_squared_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)
    print("     Default model mse: {0:0.3f} | r2: {1:0.3f}".format(mse, r2))


def answer_description(question_num = 4, start_with_nl = False):
    '''
        Parameters: question_num: integer that returns text describing the 
                        answer to that question
        Return: None, but prints answer description
    '''
    if question_num == 4:
        txt =  ''' 
            4) There isn't a 'best' model at this point because the best hyperparameters
            for each model haven't been determined.
        '''
    elif question_num == 5:
        txt = "5) The MSE has more than doubled with learning rate = 1."
    elif question_num == 8:
        txt = '''
            8) For both learning rates the train error drops to near zero with
            progressive boosting stages (iterations).  However, the larger learning
            rate test error doesn't decrease as more iterations are added.  The larger
            learning rate makes large changes per iteration and so likely overfits
            the data.  For the lower learning rate model to get low test error, many
            boosting stages are required.
        '''
    elif question_num == 9:
        txt = "9) Gradient Boost outperforms Random Forest at about 60 iterations."
    elif question_num >= 10:
        txt = '''
            10 & 11) For both RandomForest and GradientBoosting regressors, the model
            with gridsearched parameters outperformed (had a lower mse) than the 
            default model.
        '''
    nl = '\n' if start_with_nl else ''
    print(nl + textwrap.dedent(txt).strip() )

if __name__ == '__main__':
    # 2) load and train-test-split data 
    (X_train, X_test, y_train, y_test), column_names = load_and_split_data()
    
    # 3) define models then compare the mse and r2 
    # instantiate models, note random forest can be parallelized (n_jobs = -1)
    rf = RandomForestRegressor(n_estimators=100, n_jobs=-1, random_state=1)

    gdbr = GradientBoostingRegressor(learning_rate=0.1, loss='ls',
                                     n_estimators=100, random_state=1)

    dtr = DecisionTreeRegressor(random_state=1)
   
    # 4) perform the cross-validation and print results
    k = 10 # number of folds in the cross-validation 
    print("\nScript output.")
    print("Using {0} folds in cross validation.".format(k))
    print("\n4) Train MSE and R2 for the 3 models")
    cross_val(rf, X_train, y_train, k) 
    cross_val(gdbr, X_train, y_train, k) 
    cross_val(dtr, X_train, y_train, k) 
    #4) results should be something like this:
    # RandomForestRegressor     Train CV | MSE: 9.943 | R2: 0.866
    # GradientBoostingRegressor Train CV | MSE: 8.720 | R2: 0.882
    # DecisionTreeRegressor     Train CV | MSE: 16.958 | R2: 0.778
    answer_description(4, start_with_nl = True) 
    
    # 5) New gradient boosting regressor with learning rate = 1
    gdbr_lr1 = GradientBoostingRegressor(learning_rate=1.0, loss='ls',
                                     n_estimators=100, random_state=1)
    print("\n5) Quick learning rate investigation with Gradient Boosting Regressor" )
    print("Cross validation score of Gradient Boosting Regressor with lr = 0.1:")
    cross_val(gdbr, X_train, y_train, k) 
    print("Cross validation score of Gradient Boosting Regressor with lr = 1.0:")
    cross_val(gdbr_lr1, X_train, y_train, k)
    answer_description(5, start_with_nl = True) 

    # 6) Investigate effect of number of iterations
    print("\n6) Plotting effect of boosting and lr = 0.1 on GradientBoostingRegressor.")
    plot_name = "6_GBR_Effect_iterations.png"
    fig, ax = plt.subplots()
    plot_stage_score(ax, gdbr, X_train, y_train, X_test, y_test)
    plt.savefig(plot_name)
    plt.close()
    print("Plot {0} saved.".format(plot_name))

    # 7) Investigate effect of learning rate
    print("\n7) Plotting effect of boosting and learning rate on GBR.")
    plot_name = "7_GBR_Effect_iterations_and_lr.png"
    fig, ax = plt.subplots()
    plot_stage_score(ax, gdbr, X_train, y_train, X_test, y_test)
    plot_stage_score(ax, gdbr_lr1, X_train, y_train, X_test, y_test)
    plt.savefig(plot_name)
    plt.close()
    print("Plot {0} saved.".format(plot_name))

    # 8) Explain plot behavior
    answer_description(8, start_with_nl = True) 

    # 9) Compare GBR with lr = 0.1 to RandomForestRegressor
    print("\n9) Plot comparing Gradient Boosting to Random Forest Regressor.")
    plot_name = "9_Compare_GBR_to_RFR.png"
    fig, ax = plt.subplots()
    plot_stage_score(ax, gdbr, X_train, y_train, X_test, y_test)
    plot_rf_score(ax, rf, X_train, y_train, X_test, y_test)
    plt.savefig(plot_name)
    plt.close()
    print("Plot {0} saved.".format(plot_name))
    answer_description(9, start_with_nl = True) 
    
    # 10) Gridsearch best hyperparameters for RandomForest
    print("\n11) RandomForest GridSearch" )
    random_forest_grid = {'max_depth': [3, None],
                      'max_features': ['sqrt', 'log2', None],
                      'min_samples_split': [2, 4],
                      'min_samples_leaf': [1, 2, 4],
                      'bootstrap': [True, False],
                      'n_estimators': [10, 20, 40, 80],
                      'random_state': [1]}
    rf_best_params, rf_best_model = gridsearch_with_output(RandomForestRegressor(), 
                                                           random_forest_grid, 
                                                           X_train, y_train)
    print("\nb & c) Comparing model with gridsearch params to initial model on Test set.")
    rf.fit(X_train, y_train)
    display_default_and_gsearch_model_results(rf, rf_best_model, X_test, y_test)

    # 11) Gridsearch best hyperparameters for GradientBoosting
    print("\n12) GradientBoosting GridSearch")
    # note that learning rate has multiple values while n_estimators is set
    gradient_boosting_grid = {'learning_rate': [0.1, 0.05, 0.02, 0.01],
                              'max_depth': [2, 4, 6],
                              'min_samples_leaf': [1, 2, 5, 10],
                              'max_features': [1.0, 0.3, 0.1],
                              'n_estimators': [500],
                              'random_state': [1]}
    gdbr_best_params, gdbr_best_model = gridsearch_with_output(GradientBoostingRegressor(), 
                                                               gradient_boosting_grid, 
                                                               X_train, y_train)
    print("\nb & c) Comparing model with gridsearch params to initial model on Test set.")
    gdbr.fit(X_train, y_train)
    display_default_and_gsearch_model_results(gdbr, gdbr_best_model, X_test, y_test)
    answer_description(12, start_with_nl = True)
    
