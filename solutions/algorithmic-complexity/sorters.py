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
        return self.this_sort(input_list)


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
        for i in range(len(input_list)):
            # Create a 2nd index to itterate down as needed
            j = i
            while j > 0:
                #Check if the element to it's left is less than the current element
                if input_list[j-1] > input_list[j]:
                    #Do an in place swap
                    input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
                    #Itterate your 2nd index down
                    j -= 1
                #Exit while loop
                else:
                    break


class BubbleSort(SortTester):
    @classmethod
    def this_sort(cls, input_list):
        n = len(input_list)
        while n > 0:
            newn = 0
            for i in range(1, n):
                if input_list[i - 1] > input_list[i]:
                    input_list[i], input_list[i - 1] = input_list[i - 1], input_list[i]
                    newn = i
            n = newn

class HeapSort(SortTester):
    @classmethod
    def this_sort(cls, input_list):
        # convert input_list to heap
        length = len(input_list) - 1
        least_parent = int(length / 2)
        for i in range(least_parent, -1, -1):
            cls.move_down(input_list, i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if input_list[0] > input_list[i]:
                cls.swap(input_list, 0, i)
                cls.move_down(input_list, 0, i - 1)

    @classmethod
    def move_down(cls, input_list, first, last):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if (largest < last) and (input_list[largest] < input_list[largest + 1]):
                largest += 1

            # right child is larger than parent
            if input_list[largest] > input_list[first]:
                cls.swap(input_list, largest, first)
                # move down to largest child
                first = largest;
                largest = 2 * first + 1
            else:
                return  # force exit

    @staticmethod
    def swap(input_list, x, y):
        tmp = input_list[x]
        input_list[x] = input_list[y]
        input_list[y] = tmp

