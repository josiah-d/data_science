## Warmup: Appreciating Numpy

**Include your code and answers in** `numpy_quiz.py`.

1. Write a python function to find the value in a list that's closest to a given value.

    e.g. `closest([10, 17, 2, 29, 16], 14)` should return 16.

2. Instead let's start with a numpy array. How can we do the same thing in one line using numpy magic?

    Hint: Use `np.abs` and `np.argmin`.

3. My favorite numpy trick is [masking](http://docs.scipy.org/doc/numpy/user/basics.indexing.html#boolean-or-mask-index-arrays). Say you have a feature matrix `X` (2d numpy array) and with labels `y` (1d numpy array). I would like to get a feature matrix of only the positive cases, i.e. get the rows from `X` where `y` is positive.

    How can you do this in one line?
    
4. Using the above example, the next step is to apply this to a real life problem.  I have provided the code to load the **iris** dataset, and you should be able to scatter 2 of the columns against each other color each one according to their target.  

```python 
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target
```


**Challenge:**  Imagine that you have a bunch of x,y points.  You have grouped some of the points together, but in general, when you get a new datapoint (from a sensor)
you would like a list of the tope 5 closest points to the new data.  Write a function (using numpy magic) to return the 5 closest points.

```python
data = [(1,1),
        (3,1)
        (2,4)
        (5,7)
        (1,5)
        (2,9)
        (3,1)
        (2,7)
        (3,2)]

closest_2d(data,(3,1)) #should give you the 5 slosest points
```
