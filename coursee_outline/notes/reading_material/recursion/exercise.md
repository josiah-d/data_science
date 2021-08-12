## Recursion Practice
We're going to be implementing an algorithm that relies on recursion. We're going to practice with some problems. Write the functions in `recursion_practice.py`.

We'll be using this implementation of a `TreeNode` (in `node.py`) for all the questions concerning trees (2-4):

```python
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

1. Write a recursive function which takes an integer and computes and sum of the digits:

    ```python
    sum_digits(4502)    # returns 11
    ```

    Here's how to think about it recursively:
    ```
    4502 % 10 gives you 2
    4502 / 10 gives you 450
    So sum_digits(4502) = 4502 % 10 + sum_digits(4502 / 10)
    ```

2. Write a function `sum_tree` which sums all the values in a binary tree. Here's how to think about it recursively:

    ```
    sum_tree(root) = sum_tree(root.left) + sum_tree(root.right) + root.value
    ```

3. Write a function `print_all` which prints all the values in a binary tree. In your recursive call you'll need to print `root.left`, `root.right` and `root.value`. You can do these three things in any order and it will affect the order of the outcome.

    As a sidenote these are called *traversals* and each possible order has a name. **Preorder** is `value, left, right`. **Postorder** is `left, right, value`. **Inorder** is `left, value, right`.

4. Write a function `build_coinflip_tree` which takes an integer *k* and builds the tree containing all the possible results of flipping a coin *k* times. The value at each node should be a string of the flips to get there. For example, if *k* is 3, your tree should look like something similar to this:

    ```
                       ''
                     /    \
                   /        \
                 /            \
               /                \
             H                    T
           /   \                /   \
         /       \            /       \
       HH         HT        TH         TT
      /  \       /  \      /  \       /  \
    HHH  HHT   HTH  HTT  THH  THT   TTH  TTT
    ```

    To verify your result, you'll have to just do things like:
    ```python
    root = build_coinflip_tree(3)
    assert root.value == ""
    assert root.left.value == "H"
    assert root.left.left.value == "HH"
    ```
    or build the tree manually and use the `equals` function written in `recusion_examples.py`.
    
    **Hint:** The `value` parameter you'll see in the docstring is so that you can pass to the tree what path you took to get there. It might make the problem a little easier to build a tree like this instead:
    
    ```
         ''
        /  \
       /    \
      H      T
     / \    / \
    H   T  H   T
    ```



## Extra Credit
1. Go back to the traversal problem from above. If you are given the *output* of that function, can you rebuild the tree? Let's say you have the preorder and inorder. Write a function which builds the tree. You can assume values are unique.

    **Hint:** The first item in the preorder traversal is the root. In the inorder traversal, everything to the left of the root is in the left subtree and everything to the right is in the right subtree.

2. Write a function `print_tree` which takes a tree and prints the output in a human readable format.

3. Write a function `make_word_breaks` which takes a string `phrase` and a set `word_list`. The idea is to determine if you can make word breaks in the string. For example: `"thedogruns"` would become `"the dog runs"`. Of course for many strings of letters, this is not possible. Don't worry about being efficient, just try every possibility.
