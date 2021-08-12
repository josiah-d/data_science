from time import time

def timeit(fn):
    def timed(*args, **kw):
        ts = time()
        ret = fn(*args, **kw)
        te = time()

        return ret, te - ts

    return timed

class Node(object):
    pass

class Tree:
    def __init__(self, l_in = []):
        pass

    def getRoot(self):
        pass

    @timeit
    def timed_add(self, val):
        pass

    def add(self, val):
        pass

    @timeit
    def timed_search(self, val, return_depth=False):
        pass

    def search(self, val, return_depth=False):
        pass

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None
