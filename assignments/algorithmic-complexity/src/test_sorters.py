import unittest
import numpy as np
from copy import copy
from sorters import *

def equal_lists(size=1000):
    lst1 = np.random.randint(10000, size=size)
    return [lst1, copy(lst1)]


class TestSortMethods(unittest.TestCase):

    def test_bubble(self):
        lst1, lst2 = equal_lists()
        bubble_sorter = BubbleSort()
        a = bubble_sorter.this_sort(lst1)
        b = bubble_sorter.timed_sort(lst2)
        self.assertEqual(lst1.all(), lst2.all())
        for i in range(1,len(lst1)):
            self.assertGreaterEqual(lst1[i], lst1[i-1])

    def test_insert(self):
        lst1, lst2 = equal_lists()
        insert_sorter = InsertSort()
        a = insert_sorter.this_sort(lst1)
        b = insert_sorter.timed_sort(lst2)
        self.assertEqual(lst1.all(), lst2.all())
        for i in range(1,len(lst1)):
            self.assertGreaterEqual(lst1[i], lst1[i-1])

    def test_heap(self):
        lst1, lst2 = equal_lists()
        heap_sorter = HeapSort()
        a = heap_sorter.this_sort(lst1)
        b = heap_sorter.timed_sort(lst2)
        self.assertEqual(lst1.all(), lst2.all())
        for i in range(1,len(lst1)):
            self.assertGreaterEqual(lst1[i], lst1[i-1])


if __name__ == '__main__':
    unittest.main()