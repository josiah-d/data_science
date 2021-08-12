import matplotlib.pyplot as plt
import numpy as np

def closest(value_list:list, given_value:int):
    '''
    Return the value in a list that's closest to a given value.

    Parameters
    ----------
    value_list: list
    given_value: int

    Returns
    -------
    int
        closest value
        
    Examples
    --------
    >>> closest([10, 17, 2, 29, 16], 14)
    16
    '''
    distances = [abs(value - given_value) for value in value_list]
    return value_list[distances.index(min(value_list))]


def closest_np(value_list:list, given_value:int):
    '''
    Return the value in a list that's closest to a given value.

    Parameters
    ----------
    value_list: list
    given_value: int

    Returns
    -------
    int
        closest value
        
    Examples
    --------
    >>> closest([10, 17, 2, 29, 16], 14)
    16
    '''
    closest_index = np.argmin(np.abs(np.array(value_list) - given_value))
    return value_list[closest_index]


def plt_iris(x:int, y:int, feature, target, feature_names:list, target_names:list, **kwargs):
    '''
    Make 2-way scatterplots with points colored
    according to their target.

    Parameters
    ----------
    x: int
            column index to plot on the x-axis
    y: int
            column index to plot on the y-axis
    feature: numpy array
            feature matrix
    target: numpy array
            target array
    feature_names: list
            list of feature names
    target_names: list
            list of target classes
            
    Returns
    -------
    none
    '''
    for class_ in set(target):
        plt.scatter(feature[target==class_, x], feature[target==class_, y], label=target_names[class_], **kwargs)
    plt.title(f'Iris Data')
    plt.xlabel(f'{feature_names[x].capitalize()}')
    plt.ylabel(f'{feature_names[y].capitalize()}')
    plt.legend(loc='upper left')

    
def closest_2d(data:list, point:tuple):
    '''
    Return the top 5 closest points to a new data point.

    Parameters
    ----------
    data: list
            list of data points encoded as tuples
    point: tuple
            new data point

    Returns
    -------
    NumPy array
            top 5 closest points
            
    Examples
    --------
    >>> data = [(1,1),
        (3,1)
        (2,4)
        (5,7)
        (1,5)
        (2,9)
        (3,1)
        (2,7)
        (3,2)]
    >>> closest_2d(data,(3,1))
    [(3, 1), (3, 1), (3, 2), (1, 1), (2, 4)]
    '''
    data = np.array(data)
    point = np.array(point)
    distances = np.linalg.norm(np.array(data) - np.array(point), axis=1)
    points = data[np.argsort(distances)[:5]]
    return [tuple(p) for p in points]