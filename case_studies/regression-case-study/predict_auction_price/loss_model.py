import sys
import numpy as np
import pandas as pd

def rmsle(actual, predictions):
    log_diff = np.log(predictions+1) - np.log(actual+1)
    return np.sqrt(np.mean(log_diff**2))
        
if __name__=='__main__':
    '''
    Takes the location of the file of predictions that should have columns 'SaleID' and 'SalePrice' and gives a loss.
    '''
    infile = sys.argv[1]
    predictions = pd.read_csv(infile)
    predictions.set_index('SalesID', inplace=True)
    test_solution = pd.read_csv('data/end_of_day/test_actual.csv')
    test_solution.set_index('SalesID', inplace=True)

    error = rmsle(test_solution['SalePrice'], predictions['SalePrice'])
    print(error)
