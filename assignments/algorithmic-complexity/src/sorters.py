from abc import ABC
from time import time


def timeit(fn):
    def timed(*args, **kw):
        ts = time()
        fn(*args, **kw)
        te = time()

        return te - ts

    return timed


class SortTester(ABC):
    """
    Abstract base class for our sorting classes

    Allows for the calling of a sort, a stack count sort, and a timed sort
    """
    def __init__(self):
        pass

    @classmethod
    def this_sort(cls, input_list):
        pass

    @timeit
    def timed_sort(self, input_list):
        pass


class InsertSort(SortTester):
    """
    InsertSort - Class implementation of insert sort

    Usage:
    >>> lst = [4, 1, 2, 3]
    >>> my_sorter = InsertSort()
    >>> my_sorter.this_sort(lst)
    >>> print(lst)
    [1, 2, 3, 4]
    >>> my_sorter.timed_sort(lst)

    """

    @classmethod
    def this_sort(cls, input_list):
        '''
        YOUR CODE
        '''
        pass


class BubbleSort(SortTester):
    @classmethod
    def this_sort(cls, input_list):
        '''
        YOUR CODE
        '''
        pass

class HeapSort(SortTester):
    @classmethod
    def this_sort(cls, input_list):
        '''
        YOUR CODE
        '''
        pass


