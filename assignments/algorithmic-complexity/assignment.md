# Algorithmic Complexity

## Introduction

#### Implement a general sorter class
We are going to practice OOP by leveraging a class structure for our methods.  We will start by implementing 
an abstract base class.  Abstract base classes can be considered a blueprint for other classes, in which a 
set of methods are created that must be implemented by subclasses.  Read more about Abstract Base Classes in Python
[here.](https://www.geeksforgeeks.org/abstract-classes-in-python/)

The code `sorters.py` contains skeleton code for implementing the various
sorting classes we will create.  Start by building the base class.  The `__init__` and `this_sort`
functions for the base call can simply be pass statements.

## Basic

### Part 1: Examine SortTester
Sort Tester will be our base class.   All sorters will have 3 methods:
<ol>
<li>An initialization method</li>
<li>A method for implementing that specific version of a sorter; we'll call it this_sort.</li>
<li>A method for timing the sort.  A timeit decorator has been provided for this purpose.
</ol>

Rerun the test cases provided in `test_sorters.py` using `pytest`. You haven't written anything so they should all fail.

### Part 2: Implement BubbleSort and InsertSort
We discussed how these two sorting functions work in class. Put these algorithms into their own class functions.

After implementing each, rerun the test cases to verify they work.

### Part 3: Introduction to HeapSort
Take a moment to read how heap sort works:
<a href="https://en.wikipedia.org/wiki/Heapsort">Wikipedia Heap Sort</a>
<br>
Here is another [helpful visualization.](https://www.cs.usfca.edu/~galles/visualization/HeapSort.html)
<br>
<br>
Questions:
<ol>
<li>What are the steps of heapsort?</li>
<li>What are the time complexities of these steps (try to figure it out before you look at the answer!)?</li>
<li>How many times are the steps called?</li>
<li>What is the overall time complexity of heap sort?</li>
</ol>

## Advanced
### Part 4: Implement Heapsort as a class
We have shell programs, but feel free to rename or make it your own.

Rerun the test cases provided in `test_sorters.py`.

### Part 5: Plot time complexity
Create a function that will plot the time complexity of the implementations of our sorting functions. Use a decorator.
