# Recursion

In order to implement and understand Decision Trees (our next classification algorithm), we'll need a little bit of an intro into recursion.

Recursion is a very powerful computer science idea. Recursion is when a function calls itself. The idea is to reduce the problem into a simpler version of the same problem until you reduce it to what we call the *base case*.

Several math functions are naturally recursive. For example, *factorial*. Here's an example of factorial: `6! = 6*5*4*3*2*1 = 120`. You can also write it like this: `6! = 6 * 5!`. In this way, we've reduced it to a simpler version of the same problem.

Here's the code:

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
```

Fibonacci is another commonly seen example. The Fibonacci sequence is constructed by summing the two previous numbers to get the next number. Here's the sequence: 0, 1, 1, 2, 3, 5, 8, 11, 21, 33, ...

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

We can also write a sum function, which sums a list, recursively:

```python
def sum(lst):
    if not lst:
        return 0
    return lst[0] + sum(lst[1:])
```

Note that every recursive problem has two cases (can be more too):

* The *Base Case*: This is the stopping point or minimal example. It's an empty list or when an integer is 0. It's the simplest problem that can't be reduced any more.
* The *Recursive Step*: This is where all the work is done. We reduce the problem into a smaller version of the same problem (in solving factorial of n we reduced the problem to solving factorial of n - 1).


### Trees
The examples above can also be easily written *iteratively* (using loops instead of recursion), but there are instances where recursion is really key.

A *tree* in computer science is a *data structure* (way of storing data) which looks like this:

```
         8
       /   \
      5     7
       \   / \
        3 1   2
             /
            6
```

We'll be using them for *decision trees* (discussed below). You can think of those as a flow chart:

![decision tree](images/decisiontree.jpg)

Right now, we'll be dealing with abstract trees so we can get comfortable with how to code with them.

We call each "box" a *node*. Here's the definition of a *binary tree node* (binary means that each node has at most two *children*).

A *binary tree node* is either:
* NULL, or
* Has a *left child* which is a binary tree node and a *right child* which is a binary tree node

A *binary tree* is a structure with a *root* which is a *binary tree node*.

Note that even our definition is recursive!

Here's the code for a `TreeNode`:

```python
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This code would create the binary tree drawn above:

```python
root = TreeNode(8)
root.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(2)
root.right.right.left = TreeNode(6)
```

In general, when you're working with a binary tree, you need to look at the root value and then call your function on both the left and the right subtrees.

For example, to find the minimum, you need to compare the minimum of the left subtree with the minimum of the right subtree and with the root value. The minimum of those three values will be the minimum.

Here's the code:

```python
def find_minimum(root):
    if not root:
        return None
    else:
        values = root.value, find_minimum(root.left), find_minimum(root.right)
        return min(filter(lambda x: x is not None, values))
```

## Examples and exercises

* Examples in [examples.py](examples.py)
* Exercises in [exercise.md](exercise.md)

