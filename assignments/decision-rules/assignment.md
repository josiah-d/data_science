# Decision Rules

Frequently we will encounter imbalanced datasets, in which each class is not equally represented. If the imbalance is not addressed, classifiers treat the costs of misclassifying to the positive class and to the negative class as equal (traditional classifiers optimize for accuracy.) Because the majority instances outnumber the minority instances, this leads to models that tend to classify instances to the majority class and perform poorly at classifying the minority class, which is often the class of interest. 

Imbalanced datasets highlight that the misclassification costs implicit in model algorithms don't always align with our judgement of real-world misclassification costs. Sometimes it is equally important to get every instance right. Sometimes it is more important to identify some classes than others. A data scientist should always consider the costs and frequencies of different misclassifications.

There are many strategies for dealing with imbalanced classes, which are more generally strategies for developing models that are optimized for different misclassification cost scenarios.
- Optimizing for metrics other than accuracy (Parts 2-4.) 
- Specifying misclassification costs for the model training (explore the `class_weight` parameter in scikit-learn classifiers.)
- Ensembling diverse classifiers (# 13.) 
- Sampling from the data to produce a more balanced dataset (Part 5.)

## Basic

### Part 1: Confusion Matrices

Say we ran a model and got the following true labels and predicted probabilities of the positive class:

| Observation | True Label | Predicted Probability |
|:-----------:|:----------:|:---------------------:|
|       0     |      0     |          0.2          |
|       1     |      0     |          0.6          |
|       2     |      1     |          0.4          |

1. Write down the predicted labels using a default 0.5 probability threshold.

| Observation | True Label | Predicted Probability | >=0.5  |
|:-----------:|:----------:|:---------------------:|:------:|
|       0     |      0     |          0.2          |        |
|       1     |      0     |          0.6          |        |
|       2     |      1     |          0.4          |        |

2. Write down the confusion matrix using a 0.5 threshold.

|    *Threshold : 0.5*   | Actual Positive | Actual Negative |
|:----------------------:|:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

3. Find a another probability threshold that produces a different confusion matrix. Write down the threshold and the confusion matrix.

| Observation | True Label | Predicted Probability | >=0.5 | >= ?  |
|:-----------:|:----------:|:---------------------:|:-----:|:-----:|
|       0     |      0     |          0.2          |       |       |
|       1     |      0     |          0.6          |       |       |
|       2     |      1     |          0.4          |       |       |

|    *Threshold : (?)*   | Actual Positive | Actual Negative |
|:----------------------:|:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

4. Record thresholds that produce all 4 different confusion matrices for this data and write out the matrices. You have already found 2 thresholds.

| Observation | True Label | Predicted Probability | >= ?  | >= ?  | >= ?  | >= ?  |
|:-----------:|:----------:|:---------------------:|:-----:|:-----:|:-----:|:-----:|
|       0     |      0     |          0.2          |       |       |       |       |
|       1     |      0     |          0.6          |       |       |       |       |
|       2     |      1     |          0.4          |       |       |       |       |

|    *Threshold : (?)*   | Actual Positive | Actual Negative |
|:----------------------:|:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

|    *Threshold : (?)*   | Actual Positive | Actual Negative |
|:----------------------:|:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

|    *Threshold : (?)*   | Actual Positive | Actual Negative |
|:----------------------:|:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

|    *Threshold : (?)*   | Actual Positive | Actual Negative |
|:----------------------:|:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

### Part 2: Profit Matrices

We'll be working with customer data from a BU&U, a fictional telecom company. 

Let's create profit matrices considering different scenarios.

BU&U is concerned about customer churn (a customer canceling their service.) On average, each customer generates a `$`4 profit per month for the company, so when they churn the company loses that `$`4. A customer can be prevented from churning by sending them a promotion. BU&U wants to send promotions to customers it thinks will churn, but it will cost the company `$`1 whether or not the customer was actually going to churn. BU&U wants to evaluate the impact of using churn prediction models to target promotions to customers most likely to churn.

We need to establish a baseline before creating a profit matrix. We can do this in many different ways. You can think of the baseline as the planned budget for the company. Any non-zero values in the profit matrix are deviations from that budget.

For example, suppose the baseline budget **assumes no customers will ever churn**. In the tables below, "Actual Negative" means the customer is happy and won't churn and "Actual Positive" means a customer is going to churn, so they will leave if they don't receive the promotion (False Negative.) If a customer wasn't going to churn and we predict that correctly (so we don't send them a promotion) then we're on budget.


|                        | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |        0        |

If the customer is going to churn and we don't send them a promotion, we'll be at -`$`4 relative to the budget. If we predict they will churn we'll send them a promotion that will definitely make them stay, so we'll lose `$`1 whether or not they would have churned. Our final profit matrix is


|                        | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |       -1        |        -1       |
| **Predicted Negative** |       -4        |         0       |

Note that none of the cases are positive because our baseline budget was highly optimistic.

5. Create another profit matrix for the same scenario, but assuming that churning is the status quo and that sending a promotion to someone costs money but does prevent someone from churning. 

|                        | Actual Positive | Actual Negative |
| ---------------------- |:---------------:|:---------------:|
| **Predicted Positive** |                 |                 |
| **Predicted Negative** |                 |                 |

6. Consider a different scenario. BU&U wants you to evaluate the **additional** profit that churn prediction models can generate relative to the status quo of not trying to prevent customer churn. Specify the profit matrix for this scenario as a 2x2 numpy array. Start by considering the costs of the company doing nothing, and then the costs and profits after they send promotions to customers. The matrix should contain the benefit of true positives, false positives, true negatives and false negatives in the following form:

```python
[[tp, fp]
 [fn, tn]]
```

Use this profit matrix for the rest of the assignment.

7. Using the model at the beginning of the assignment and your confusion matrices and profit matrix, calculate the expected profit per customer at different thresholds. Your answers should match this plot. **Do not spend time recreating the plot!**

<div align='center'>
    <img src='./images/toy_profit_curve.png', width='600'>
</div>

### Part 3: Profit Curve Implementation

8. Using the code stub provided in `src/decision_rules.py`, write a function called `profit_curve()` that takes these arguments:  
    `y_true`: True labels for each datapoint (either 0 or 1.)  
    `y_probs`: Predicted probability for being the positive class for each datapoint (between 0 and 1.)  
    `profit_mat`: Your profit matrix.  
    `per_instance`: Boolean value for whether to calculate total or per instance profit. Default is False.

    Here's the pseudocode for `profit_curve()`. Note the similarity to building an ROC plot!

    ```
    profit_curve(y_true, y_probs, profit_mat, per_instance)
    1    thresholds = sort y_probs in decreasing order and append 1 to 
             the beginning so you consider all classification 
             thresholds
    2    for threshold in thresholds
    3        label all observations with 
                 predicted probabilities >= threshold as the 
                 positive class
    4        compute the confusion matrix using true labels and 
                 predicted labels (call the standard_confusion_matrix 
                     function in src/decision_rules.py)
    5        calculate expected profit
                 - multiply each of the 4 counts in the confusion matrix 
                       with its corresponding value in the profit matrix
                 - sum the products
    6    if per_instance
    7        divide expected profits by the number of 
                 sample observations
    8    return an array of expected profits and an array of 
             corresponding thresholds
    ```

9. Test your `profit_curve()` function on the same toy example from above:

    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    from src.decision_rules import profit_curve

    y_labels = [0, 0, 1]
    y_probs = [0.2, 0.6, 0.4]
    profit_mat = [[3, -1], [0, 0]]
    # You will get the same profit values as Part 2 if you pass 
    # `per_instance=True` to `profit_curve`.
    exp_profits, thresholds = profit_curve(y_labels, y_probs, profit_mat)
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(8, 4.5), tight_layout=True)
    pcts = np.linspace(0, 100, len(thresholds))
    ax.step(pcts, exp_profits, 'k', where='post', label='Toy Classifier')
    ax.set(title="Profits",
           xlabel="Percentage of Test Instances (decreasing by score)",
           ylabel="Profit")
    ax.legend()
    plt.show()
    ```
    
<div align='center'>
    <img src='./images/toy_profit_curve_v2.png', width=600>
</div>

## Advanced

### Part 4: Profit Curve Investigation

10. Now you're ready to plot profit curves using BU&U data!

    Use `pandas` to load the dataset from `data/churn.csv`. Drop the "State", "Area Code" and "Phone" columns. If there are any columns with only two values, convert those values to 1's and 0's. The "Churn?" column will be our target.

11. Fit a logistic regression to the churn data using these settings:
```python
LogisticRegression(penalty='none', max_iter=1e4)
```
...and build off the plotting code above to create the corresponding profit curve. Don't forget to split the data into a training set and a validation/test set. Which set should you use to plot the profit curve?

Use this profit matrix if you are not already:
```python
profit_mat = np.array([[3, -1], [0, 0]])
```
Note: If you have a scikit-learn model stored as a variable, say `model`, you can use `model.__class__.__name__` to return the name of the model class. This will be helpful for labeling plots.

12. Implement a `plot_profit_curve()` function with the following parameters:
    ```
    model, profit_mat, X, y
    ```
    You should be able to use it like this:

    ```python
    lr = LogisticRegression(penalty='none', max_iter=1e4)
    lr.fit(X_train, y_train)
    profit_mat = [[3, -1], [0, 0]]
    plot_profit_curve(lr, profit_mat, X_test, y_test)
    plt.show()
    ```
    The shape of your profit curve should look similar to this:
    <div align='center'>
        <img src='./images/profit_curve_lr.png', width=600>
    </div>

13. Now use the following code snippet to compare several models.

    Note: This uses the provided function `plot_profit_curve_v2()` and not the plotting function you wrote.

    ```python
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import GradientBoostingClassifier as GBC
    from sklearn.ensemble import RandomForestClassifier as RF
    from sklearn.svm import SVC
    from sklearn.linear_model import LogisticRegression
    from src.decision_rules import plot_profit_curve_v2

    # Support Vector Machine separating hyperplanes are influenced by 
    # feature sizes.
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)
    models = [GBC(), RF(n_jobs=-1), SVC(probability=True), 
              LogisticRegression(penalty='none')]
    random_state = 1310
    for i, model in enumerate(models):
        model.set_params(**{'random_state': random_state})
        model.fit(X_train_std, y_train)

    fig, ax = plt.subplots(figsize=(16, 9))
    profit_mat = [[3, -1], [0, 0]]
    for model in models:
        plot_profit_curve_v2(model, profit_mat, X_test_std, y_test, ax=ax)
    # Add profit matrix.
    tp_profit, fp_profit, fn_profit, tn_profit = profit_mat.ravel()
    table = [['Profit', 'Actual +', 'Actual -'], 
             ['Predicted +', tp_profit, fp_profit],
             ['Predicted -', fn_profit, tn_profit]]
    ax.table(cellText=table, cellLoc='center', colWidths=[0.1] * 3, 
             loc='lower left')
    plt.show()
    ```

14. What's the maximum profit that we can achieve, at what threshold and which model should we use to get it? What proportion of the customer base does this target?

## Extra Credit

### Part 5: Sampling Methods

Because traditional classifiers optimize for accuracy, they tend to perform poorly at identifying the minority class in imbalanced datasets where the classes are not well-separated. Sampling methods alter the training set to create a more balanced class distribution.

<div align='center'>
    <img src='./images/sampling_methods.png' width=600>
</div>

There are many different sampling methods to address imbalanced classes. We will explore 3.
- (Random) Undersampling, which randomly samples a subset from the majority class.
- (Random) Oversampling, which randomly duplicates observations from the minority class.
- SMOTE, a method of oversampling which augments the minority class by generating similar observations.

**(Random) Undersampling**  
    Discard majority class observations at random to reach a desired 
    ratio of minority class observations to majority class 
    observations.

**(Random) Oversampling**  
    Duplicate sets of minority class observations to reach a desired 
    ratio of minority class observations to majority class 
    observations. For example, if there are 10 minority class 
    instances and 103 majority class instances, oversampling would 
    copy the 10 minority instances 9 times each and sample an 
    additional 3 minority instances without replacement.

15. **SMOTE - Synthetic Minority Over-sampling TEchnique**  
SMOTE is a method of oversampling the minority class that involves creating synthetic minority class examples.

    SMOTE first selects a minority class instance (call it *a*) at random and finds its *k* nearest minority class neighbors. The synthetic instance is then created by choosing one of the *k* nearest neighbors (call it *b*) at random and connecting *a* and *b* to form a line segment in the feature space, and then picking a point randomly along that line (ie. a convex combination of the two chosen instances *a* and *b*.)

    Depending upon the amount of over-sampling required, neighbors from the k nearest neighbors are randomly chosen. For instance, if the amount of over-sampling needed is 200%, only two neighbors from the five nearest neighbors are chosen and one sample is generated in the direction of each.

Implement the [original algorithm][1] in python as the class `SMOTE`. Use the `src.decision_rules.NearestNeighbors` class for finding nearest neighbors. It works exactly like [`sklearn.neighbors.NearestNeighbors`][2]. Also, take a look at the [`numpy.random`][3] module. It will be useful for the randomization tasks needed in this class.
    
<!-- References -->
[1]: https://arxiv.org/pdf/1106.1813.pdf
[2]: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors
[3]: https://numpy.org/doc/stable/reference/random/index.html#quick-start
```
Algorithm SMOTE(T, N, k)  
Input: Number of minority class samples T; Amount of SMOTE N%; Number of nearest
neighbors k  
Output: (N/100)  T synthetic minority class samples  
1  (∗ If N is less than 100%, randomize the minority class samples as only a random
       percent of them will be SMOTEd. ∗)  
2  if N < 100  
3      then Randomize the T minority class samples  
4      T = (N/100) ∗ T  
5      N = 100
6  endif
7  N = (int)(N/100) (∗ The amount of SMOTE is assumed to be in integral multiples of
       100. ∗)
8  k = Number of nearest neighbors
9  numattrs = Number of attributes
10 Sample[ ][ ]: array for original minority class samples
11 newindex: keeps a count of number of synthetic samples generated, initialized to 0
12 Synthetic[ ][ ]: array for synthetic samples
   (∗ Compute k nearest neighbors for each minority class sample only. ∗)
13 for i ← 1 to T
14     Compute k nearest neighbors for i, and save the indices in the nnarray
15     Populate(N, i, nnarray)
16 endfor

   Populate(N, i, nnarray) (∗ Function to generate the synthetic samples. ∗)
17 while N =/= 0
18     Choose a random number between 1 and k, call it nn. This step chooses one of
           the k nearest neighbors of i.
19     Compute: gap = random number between 0 and 1
20     for attr ← 1 to numattrs
21         Compute: dif = Sample[nnarray[nn]][attr] − Sample[i][attr]
22         Synthetic[newindex][attr] = Sample[i][attr] + gap ∗ dif
23     endfor
24     newindex++
25     N = N − 1
26 endwhile
27 return (∗ End of Populate. ∗)
End of Pseudo-Code.
```

Test that your class works by running the code below. Your plot should look similar to the SMOTE plot above. Pay attention to the `# SMOTE the dataset.` section of code for how your class should be instantiated and used.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from src.decision_rules import SMOTE
# Define dataset.
random_state = 1
X, y = make_classification(
    n_samples=10000, n_features=2, n_redundant=0, 
    n_clusters_per_class=1, weights=[0.99], flip_y=0, 
    random_state=random_state)
# SMOTE the dataset.
T, N = 100, 9800
smote = SMOTE(T, N, random_state=256)
y_sm = np.append(y, np.ones(N))
X_sm = smote.fit_resample(X[y == 1])
X_sm = np.vstack((X, X_sm))
# Scatter plot.
fig, ax = plt.subplots(figsize=(8.5, 4), tight_layout=True)
labels = [0, 1]
for label in labels:
    ax.scatter(X_sm[y_sm == label, 0], X_sm[y_sm == label, 1], 
               label=label)
    ax.set(title='SMOTE', xlabel='Feature 0', ylabel='Feature 1')
    ax.legend()
plt.show()
```

#### Comparing Methods

16. Try running the documentation examples for the `Undersample`, `Oversample` and `SMOTE_v2` classes to get familiar with the API.
17. Using the churn dataset and a logistic regression model, calculate the expected profit for the different sampling methods and a range of different minority class *percentages* (how can you convert minority to majority ratios into minority class proportions? What is the minority to majority ratio for the starting data, and what is the maximum ending minority to majority ratio? Hint: What is the fewest number of majority class observations possible after sampling for each method?)
18. Which method is best? What minority class percentages maximize expected profit?
19. Try this investigation several times, with a different random train/test split each time. Does the expected profit and optimal sampling proportion vary substantially? How might you deal with this variance?
