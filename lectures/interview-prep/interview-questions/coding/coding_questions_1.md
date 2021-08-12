## Whiteboarding Practice

#### You can find notes on whiteboarding and runtime analysis [here](../../runtime_notes/runtime_analysis.md).

Write up solutions to each of these problems *on paper* or a *whiteboard*. Do not use your computer to look anything up or test out a command. If you don't remember exactly how a function works, make a reasonable assumption.

It's important to practice writing code by hand without having any resources since many interviewers will ask you to do this.

### 1. Stock trading
1.1 You have an array that contains the stock prices for each day over the past year. You would like to know the maximum money you could have made with one purchase and one sale. We are assuming that the price of stock is constant over each day.

1.2 What is the runtime of your algorithm?

1.3 Now assume you have these rules: Each day you can buy at most 1 share of stock. You can sell any number of shares of your stock at any time. What is the maximum amount of money you could have made over the year?


### 2. Even-Odd Split
2.1 Given a list of integers, move all the odd numbers to the left and the even numbers to the right.

2.2 What is the runtime of your algorithm?

2.3 How much space does it use?

2.4 If you didn't already, can you modify your algorithm to work in place (using constant extra space)?


### 3. Word Break
3.1 Given an input string and a dictionary of words, segment the input string into two dictionary words if possible. For example, if the input string is "applepie" and dictionary contains a standard set of English words, then we would return the string "apple pie" as output.

    * You can choose how the dictionary of words is stored.
    * If there are multiple possibilities, you only need to return one.
   <br></br>
3.2 What is the runtime of your algorithm?

3.3 Can you make an algorithm that would work for any number words (rather than just 2)? What's the runtime of this algorithm?

### 4. Most Frequent Words
Given a file that contains the text of a document and an integer `n`, return a list of the top n most frequent words.


### 5. Pig Latin Translator

Write a pig latin translator. Given a phrase in english, return the pig latin. Rules:

- If the word starts with a consonant, move consonant to the end and add ay.
  - `cat->atcay`
- If the word starts with a vowel, add hay.
  - `orange->orangehay`
- If the word starts with more than one consonant, move all of them to the end and add ay.
  - `string->ingstray`
Start by assuming the phrase is all lowercase with no punctuation.



### 6. Phone Numberpad

Given a dictionary that shows the mapping of digits to numbers on a phone numberpad (e.g. `'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']`, etc.) and a string of digits, return all the possible letter combinations that correspond to the string of digits.

Start by assuming that there are two digits in the string.

example: `32 => da, db, dc, ea, eb, ec, fa, fb, fc`

Extension: Have your function also take a corpus of words and only return strings which are in your corpus.


### 7. Matrix Diagonals

Given a matrix, print out the diagonals. 

```
example input:
[[1, 2, 8],
 [-4, 5, 2],
 [0, -4, -6],
 [-3, 3, 9]]

example output:
8
2 2
1 5 -6
-4 -4 9
0 3
-3
```


### 8. Change Machine

Write a function that computes what coins needed to give an amount of change. Given a value and a list containing the coin values, return the numbers of each coin required (use the minimum number of coins possible).

```
example input: 85, [5, 10, 25]
example output: [0, 1, 3]  => corresponds to 0 nickels, 1 dime, 3 quarters
```


### 9. Rotate an Image

Given a square image encoded as a matrix, rotate the image clockwise with using only constant extra space.

```
input:
[[2, 3],
 [1, 4]]

output:
[[1, 2],
 [4, 3]]
```


### 10. Intersection of Two Lists

Given two lists of integers, return the intersection.

example: `[2, 5, 3, 8, 1], [1, 9, 5, 6] => [1, 5]`

Extension: get a linear time algorithm.

Extension 2: preserve duplicates (if both lists have two 6’s, the result should have two 6’s).


### 11. Triple Sum to 0

Given a list of integers, find three which sum to zero.

example: `[3, 4, -10, 10, 1, -2, -7] => (3, 4, -7)`

Extension: Don't allow reuse of elements.


### 12. Largest Subsequence

Given a list of integers, find the consecutive subsequence with the largest sum.

example: `[4, -6, 10, 5, -11, 12, -5] => (10, 5, -11, 12) = 16`


### 13. Foreign Alphabet

*Very challenging*

There’s another language with our same letters but a different ordering of the letters. You are giving a list of words in alphabetical order and you must determine the order of the alphabet. You can assume that the input is not contradictory and if there are multiple possible alphabet orderings, you may return any of them.

```
example input: 
dbga
dgg
aa
bbgd
example output: d, a, b, g
```

### 14. Dutch National Flag

Given a list of integers, sort them based on modulo 3. So first it's all the values that are 0 mod 3, then 1 mod 3, then 2 mod 3. You don't have to preserve order within each class.

```
[4, 6, 1, 3, 9, 2, 8, 10, 12] -> [6, 3, 9, 12, 4, 1, 10, 2, 8]
```

Extension: Do it in-place.

# Searches & Sorts

1. Implement [selection sort](https://en.wikipedia.org/wiki/Selection_sort) in place.

2. Write pseudocode for, and analyze the runtime of the [mergesort](https://en.wikipedia.org/wiki/Merge_sort) algorithm.

3. Implement the merge function that's used in the mergesort algorithm.

4. Implement breadth first search (BFS) for the following challenge: Say you have a function `get_all_links` which takes a URL and finds all links that URL points to. Write a function `find_shortest_path` which takes two URLs and finds the links you need to click to get from the first to the second in the smallest number of clicks.
