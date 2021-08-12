"""Contains a node class for a decision tree."""

from collections import Counter
import numpy as np


class TreeNode(object):
    """A node class for a decision tree."""

    def __init__(self):
        """Initialize an empty TreeNode."""
        self.column = None  # (int)    index of feature to split on
        self.value = None  # value of the feature to split on
        self.categorical = True  # (bool) whether or not node is split on
                                 # categorial feature
        self.name = None    # (string) name of feature (or name of class in the
                            #          case of a list)
        self.left = None    # (TreeNode) left child
        self.right = None   # (TreeNode) right child
        self.leaf = False   # (bool)   true if node is a leaf, false otherwise
        self.classes = Counter()  # (Counter) only necessary for leaf node:
                                  #           key is class name and value is
                                  #           count of the count of data points
                                  #           that terminate at this leaf

    def predict_one(self, x):
        """Return the predicted label for a single data point.

        Parameters
        ----------
        x: 1d numpy array
            A single data point.

        Returns
        -------
        y: predicted label
        """
        if self.leaf:
            return self.name
        col_value = x[self.column]

        if self.categorical:
            if col_value == self.value:
                return self.left.predict_one(x)
            else:
                return self.right.predict_one(x)
        else:
            if col_value < self.value:
                return self.left.predict_one(x)
            else:
                return self.right.predict_one(x)

    # This is for visualizing your tree. You don't need to look into this code.
    def as_string(self, level=0, prefix=""):
        """Return a string representation of the tree rooted at this node.

        Parameters
        ----------
        level: int
            Amount to indent.

        Returns
        -------
        prefix: str
            Prefix to start the line with.
        """
        result = ""
        if prefix:
            indent = "  |   " * (level - 1) + "  |-> "
            result += indent + prefix + "\n"
        indent = "  |   " * level
        result += indent + "  " + str(self.name) + "\n"
        if not self.leaf:
            if self.categorical:
                left_key = str(self.value)
                right_key = "no " + str(self.value)
            else:
                left_key = ">= " + str(self.value)
                right_key = "< " + str(self.value)
            result += self.left.as_string(level + 1, left_key + ":")
            result += self.right.as_string(level + 1, right_key + ":")
        return result

    def __repr__(self):
        """Represent TreeNode as string."""
        return self.as_string().strip()
