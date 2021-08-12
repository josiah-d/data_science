## Runtime Analysis

Runtime analysis is a way of measuring how long an algorithm or bit of code takes to run. It may at first appear to be theoretical, but having an understanding of runtime analysis can really help you write good code. It can be the difference between your code running in a few minutes and it taking days.

Let's start with a simple example.

## Simple Example

The following code searches for an element in a python list.

```python
def find_element(lst, element):
    for elem in lst:
        if elem == element:
            return True
    return False
```

#### What's the Runtime?
We start by assuming that the list `lst` has *n* elements in it. The standard is to use the letter *n*.

So how many steps does it take? Well, it depends if the element is in the list. If it is, you only have to go till you find it. If it isn't you have to go all the way till the end (n steps). When we talk about runtime, we talk about the *worst case* scenario. So, here, the worst case is that you have to look at every element, so the runtime is O(n).

## Big-Oh Notation
This is the notation we use. Written like this: O(n) and said like this: "big oh of n."

There is a [formal mathematical definition](http://en.wikipedia.org/wiki/Big_O_notation#Formal_definition) of big-oh, but you don't actually need to know it.

#### Ignore Constant Factors
The thing to keep in mind, is that it is a rough measure of runtime, not an exact measure of the amount of time the code will take. This means that we don't care about constant factors. You don't need to figure out if it takes one or two steps for each element in the list. We never say O(n/2). This is the same as O(n). This also means that if you only loop over half of an array, the runtime is still O(n).

Also, if you have two parts to your function, one which takes O(n) and one which takes O(n^2), we say the total runtime is O(n^2) since this is the larger factor. 


#### Big-oh Example
So does this value really matter? Is n really that much faster than n^2? YES! Let's look at some examples. We have a O(n) algorithm and a O(n^2) algorithm. When n is 100, they both take 1 second. So what's the big deal? Let's see what happens when we scale this up.

|       n |    O(n) algorithm |        O(n^2) algorithm |
| ------- | ----------------- | ----------------------- |
| 100     |             1 sec |                   1 sec |
| 1000    |            10 sec |                 100 sec |
| 10,000  |           100 sec |    10,000 sec = 167 min |
| 100,000 | 1000 sec = 17 min | 1,000,000 sec = 11 days |

17 minutes versus 11 days? I certainly care about that difference.

Note that each time the O(n) algorithm increases by a factor of 10 and the O(n^2) algorithm increases by a factor of 100 (10^2).


## Anagrams Example

Let's look at the anagrams problem that many of you did in your interview for Zipfian.

First, two words are anagrams if they have the same letters in them but in a different order. For example, rats and arts are anagrams since they have the same letters. You would like to write a function `find_anagrams` which takes a list of strings and returns the strings that are anagrams with another word in the list. For example:

```python
In [8]: find_anagrams(['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star'])
Out[8]: ['god', 'dog', 'rats', 'arts', 'star']
```

All of the solutions work correctly, but they vary greatly in their efficiency.

For our analysis, we'll say that *n* is the length of the list. We also have a second variable, the length of the word! Let *k* be the maximum length of a word.

We'll start with some inefficient solutions and end with an efficient one.

I go over the runtimes in excessive detail. As you get more comfortable, you can handwave over a lot of this analysis and just give the result.

#### Solution 1

```python
 1  def find_anagrams(lst):
 2      result = []
 3      for word1 in lst:
 4          for word2 in lst:
 5              if word1 != word2:
 6                  for perm in permutations(word1):
 7                      if perm == list(word2):
 8                          result.append(word1)
 9      return result
```

What's the runtime? I like to work inwards out, so I'll start with line 8.

* **Line 8:** Appending to an array is constant time: O(1)

* **Line 7:** Checking equality of two lists means you have to check every element of the list. The length of the list here is the length of the word, which we said was k. So this takes O(k).

* **Lines 7-8:** Two operations that happen one after another we can add. This gives us 1 + k. Since k is much bigger than 1, we just care about that term, so we get O(k).

* **Lines 6-8:** How many times do we go over this for loop? Well, we go through the loop for every permutation of the word, which is k!. So we do the contents of the for loop k! times. So we multiple k! times the previous result to get: O(k * k!)

* **Line 5:** To check if two strings are equal, you have to check every character, so this is O(k)

* **Lines 5-8:** We sum the above two results. Note that even though only sometimes will lines 6-8 run, we just pretend like they always do. We round up in runtime analysis! We get k + k * k!. Since the second term is much bigger, we just say O(k * k!)

* **Lines 4-8:** We go over this loop once for every word in the list. There are n words in the list. So to get the total runtime of this for loop, we multiply n by the runtime of the contents of the loop (from above): O(n * k * k!)

* **Lines 3-8:** This for loop also is going over every word in the list, so n times. We multiply n by the result from above to get our final result: O(n^2 * k * k!)

This is OK, but the k factorial is pretty huge! Do we really need to check every single permutation?

#### Solution 2

```python
 1  def find_anagrams(lst):
 2      result = []
 3      for word1 in lst:
 4          for word2 in lst:
 5              if word1 != word2 and sorted(word1) == sorted(word2):
 6                  if word1 not in result:
 7                      result.append(word1)
 8                  if word2 not in result:
 9                      result.append(word2)
10       return result
```

* **Lines 6-7:** Working inwards out, we start with this lines 6-7:

    ```python
    if word1 not in result:
        result.append(word1)
    ```

    How long does it take to check if the word is already in the result? Well, it depends on the length of ``result`, which is upperbounded by the length of `lst` (n). So we just say that the runtime of this operation is O(n).

* **Lines 8-9:** The next bit has the same analysis and will also be O(n).

* **Lines 6-9:** So together, what is it? 6-7 is O(n) and 8-9 is O(n), so that's O(2n) for lines 6-9, but we don't care about constants so that's O(n).

* **Line 5:** What about the if statement on line 5? Sorting is O(n log n) (something you should try to remember). Since we're sorting the characters, the variable is acutally *k* here, so the runtime of the if statement is O(k log k). Convince yourself that the sorting is the most time consuming part of this line.

* **Lines 5-9:** All together, lines 5-9 have runtime O(n + k log k). Note that we keep both terms because we don't actually know which one of these will be bigger.

* **Lines 4-9:** The for loop on line 4 is looping over every word in the list. So this will go through *n* times. We know the runtime of the content of the for loop above, so we multiple that by n to get: O(n^2 + nk log k)

* **Lines 3-9:** The for loop on line 3 also goes over every word in the list, which is *n*. So we multiply the previous result by n to get our final runtime: O(n^3 + n^2 k log k)

This is not super great. The check for membership on lines 6 and 8 really hurts the runtime! This is basically three nested for loops!


#### Solution 3
We can get a better solution by removing that membership check. The following is O(n^2 + n k log k).

```python
 1  def find_anagrams(lst):
 2      result = []
 3      for word1 in lst:
 4          for word2 in lst:
 5              if word1 != word2 and sorted(word1) == sorted(word2):
 6                  result.append(word1)
 7                  break
 8       return result
```


#### Solution 4
But we can do better! Dictionaries to the rescue! In a coding interview if the interviewer asks: *Can you optimize this?*, 99% of the time the answer is: *Yes! Use a dictionary!*

```python
 1  def find_anagrams(lst):
 2      result = []
 3      d = defaultdict(list)
 4      for word in lst:
 5          d[tuple(sorted(word))].append(word)
 6      for key, value in d.iteritems():
 7          if len(value) > 1:
 8              result.extend(value)
 9      return result
```

Before worrying about the analysis, make sure you understand how this code workds.

This has two parts to it: building the dictionary and checking for anagram lists that have at least 2 elements. So we need to figure out the runtime of each of these parts and then sum the two results.

* **Line 5:** Sorting the word takes k log k. Finding the element in the dictionary and appending are both constant operations. So the runtime is O(k log k)

* **Lines 4-5:** We go over this loop n times, so we multiply n by the above result to get O(n k log k)

* **Lines 6-8:** It's easiest to analyze this all at once. The only work here is adding elements to the result. Since we are adding at most n elements, the runtime is O(n)

We sum those two results to get the total runtime. Since lines 4-5 have a larger runtime, that's all we care about, so our final runtime is O(n k log k). This is much better than the previous solutions!


## Key Runtimes to Remember

#### Common Runtimes

Python method [time complexities](https://wiki.python.org/moin/TimeComplexity).

Here are the runtimes you will commonly see, in order from slow to fast:

* O(1) (*constant*)
* O(log n) (*logarithmic*)
* O(n) (*linear*)
* O(n log n)
* O(n^2) (*quadratic*)
* O(n^3) (*cubic*)
* O(2^n) (*exponential*) (there are different levels of exponential depending on the base)

Here are some standard operations and their operations:

1. List operations:
    * Appending: O(1)
    * Adding to the beginning or middle: O(n) (have to slide everything over!)
    * Popping from the end: O(1)
    * Popping from the beginning or middle: O(n)
    * Looking up by index: O(1)
    * Checking membership (*seaching*): O(n) (have to look at every item)
    * Searching if the list is in sorted order: O(log n) ([binary search](http://en.wikipedia.org/wiki/Binary_search_algorithm))

2. Dictionary operations (*Dictionaries are fast!!*):
    * Inserting an item: O(1)
    * Removing an item: O(1)
    * Looking up by key: O(1)
    * Looking up by value: O(n) (have to look at every item)

3. Sorting:
    * O(n log n)
