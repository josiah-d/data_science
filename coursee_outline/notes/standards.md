Data Science Immersive Standards
====


### What is a Standard?
---

Standards are the core-competencies of data scientists - the knowledge, skills, and habits every Galvanize graduate should possess.  These were carefully crafted in a joint effort by your  lead instructors, and represent those knowledge, skills, and habits we believe students need to get your foot in the door and be successful in industry.

### Standards by Topic
---

#### **1. Unix**
1. Perform basic file operations from the command line, while consulting man/help/Google if necessary.
1. Get help using `man` (ex man grep)
1. Perform “survival” edits using vi, emacs, nano, or pico
1. Configure environment & aliases in .bashrc/.bash_profile/.profile
1. Install data science stack
1. Manage a process with job control
1. Examine system performance and kill processes
1. Work on a remote machine with ssh/scp
1. State what an RE (regular expression) is and write a simple one
1. State the features and use cases of grep/sed/awk/cut/paste to process/clean a text file

#### **2. Version Control / Git**
1. Explain the basic function and purpose of version control.
1. Use a basic Git workflow to track project changes over time, share code, and write useful commit messages.

#### **3. Python**
1. Explain the difference between mutable and immutable types and their relationship to dictionaries.
1. Compare the strengths and weaknesses of lists vs. dictionaries vs. sets.
1. Choose the appropriate collection (dict, Counter, defaultdict) to simplify a problem.
1. Compare the strengths and weaknesses of lists vs. generators.
1. Write pythonic code.

#### **4. Pandas**
1. Explain/use the relationship between DataFrame and Series
1. Know how to set, reset indexes
1. Use iloc, loc, ix, and iat appropriately
1. Use index alignment and know when it applies
1. Use Split-Apply-Combine Methods
1. Be able to read and write data to pandas
1. Recognize problems that can probably be solved with Pandas (as opposed to writing vanilla Python functions).
1. Use basic DateTimeIndex functionality

#### **5. Plotting**
1. Describe the architecture of a matplotlib figure
1. Plot in and outside of notebooks with matplotlib and seaborn
1. Combine multiple datasets/categories in same plot
1. Use subplots effectively
1. Plot with Pandas
1. Use and explain scatter_matrix output
1. Use and explain a correlation heatmap
1. Visualize pairwise relationships with seaborn
1. Compare within-class distributions
1. Use matplotlib techniques with seaborn

#### **6. Visualization**
1. Explain the difference between exploratory and explanatory visualizations.
1. Explain what a visualization is
1. Don’t lie with data
1. Visualize multidimensional relationships with data using position, size, color, alpha, facets.
1. Create an explanatory visualization that makes a relationship in data explicit.

#### **7. Linear Algebra in Python**
1. Perform basic Linear Algebra operations by hand: Multiply matrices,
subtract matrices, Transpose matrices, verify inverses.
1. Perform linear algebra operations (multiply matrices, transpose matrices, and invert matrices) in numpy.

#### **8. OOP**
1. Given the code for a python class, instantiate a python object and call the methods and list the attributes.
1. Write the python code for a simple class.
1. Match key “magic” methods to their functionality.
1. Design a program or algorithm in object oriented fashion.
1. Compare and contrast functional and object oriented programming.

#### **9. Docker**
1. Pull a docker image from dockerhub
1. Start a docker container from a docker image
1. List running containers
1. Stop/remove a running container
1. Create a docker image based on a working directory.
1. Upload your docker images to dockerhub.

#### **10. AWS**
1. Scope & Configure a data science environment on AWS.
1. Protect AWS resources against unauthorized access.
1. Manage AWS resources using awscli, ssh, scp, or boto3.
1. Monitor and control costs incurred on AWS

#### **11. Algorithmic Complexity and Data Structures**
1. Explain the meaning of Big-Oh.
1. Analyze the runtime of code.
1. Explain what recursion is.
1. Contrast an in place method with it's counterpart.  Know a sorting algorithm for each type.
1. Understand a binary tree, a binary search tree, and a heap.  Know what the application of the various tree structures is.
1. Explain block memory arrays and contrast how `numpy` arrays vs python lists do indexed look up.

#### **12. Webscraping**
1. Compare and contrast SQL and noSQL.  
1. Complete basic operations with mongo.
1. Explain the basic concepts of HTML.  
1. Write python code to pull out an element from a web page.  
1. Fetch data from an existing API

#### **13. SQL**
1. Connect to a SQL database via command line (i.e. Postgres).
1. Connect to a database from within a python program.
1. State function of basic SQL commands.
1. Write simple queries on a single table including SELECT, FROM, WHERE, CASE clauses and aggregates.
1. Write complex queries including JOINS and subqueries.
1. Explain how indexing works in Postgres.
1. Create and dump tables.
1. Format a query to follow a standard style.
1. Move data from SQL database to text file.

#### **14. Spark**
1. Describe differences and similarities between MapReduce and Spark  
1. Get data into spark for processing.
1. Describe lazy evaluation in the context of Spark.
1. Cache RDDs effectively to improve performance.
1. Use Spark to do compute basic statistics
1. Know the difference between Spark data types: RDD, DataFrame, DAG

#### **15. SQL in Spark**
1. Identify what distinguishes a Spark DataFrame from an RDD
1. Explain how to create a Spark DataFrame
1. Query a DF with SQL
1. Transform a DF with dataframe methods
1. Use user-defined functions
1. Set up a pipeline to use spark's MLLib

#### **16. Probability Distributions**
1. Give noncircular definitions for probability, statistics, and likelihood
1. Define what a random variable is.
1. Contrast discrete and continuous probability distributions
1. Describe phenomena that are modeled using the following distributions: Bernoulli, binomial (bonus: multinomial), Poisson, geometric, uniform, normal, exponential.
1. Use models to assess the likelihood of and event having happened.
1. Know what the following methods give you for a scipy distribution: pdf, ppf, sf, cdf.

#### **17. Binomial Tests**
1. Describe a null and alternative hypothesis
1. Explain the connection between significance level and type 1 error.
1. Describe a p-value.
1. Calculate a p-value for a binomial test.
1. Describe how a Chi^2 test works, and the scenarios in which it is appropriate.

#### **17. Sampling**
1. Compute MLE estimate for simple example (such as coin-flipping)
1. Pseudocode Bootstrapping for a given sample of size N.
1. Construct confidence interval for case where parametric construction does not work
1. Discuss examples of times when you need bootstrapping.
1. Define the Central Limit Theorem
1. Compute standard error
1. Compare and contrast the use cases of parametric and nonparametric estimation


#### **18. Central Limit Theorem Tests**
1. Describe a situation in which a one-tailed test would be appropriate (vs. a two-tailed test).
1. Given a particular situation, correctly choose among the following options:
  - z-test
  - t-test
  - 2 sample t-test (one-sided and two-sided)
  - 2 sample z-test (one-sided and two-sided)
1. Define p-value, Type I error, Type II error, significance level and discuss their significance in an example problem.
1. Account for the multiple comparisons problem via Bonferroni correction.
1. Discuss when to use an A/B test to evaluate the efficacy of a treatment

#### **19. Power**
1. Define Power and relate it to the Type II error.
1. Compute power given a dataset and a problem.
1. Explain how the following factors contribute to power:
    - sample size
    - effect size (difference between sample statistics and statistic formulated under the null)
    - significance level
1. Identify what can be done to increase power.
1. Estimate sample size required of a test (power analysis) for one sample mean or proportion case
1. Solve by hand for the posterior distribution for a uniform prior based on coin flips.
1. Solve Discrete Bayes problem with some data
1. What is the difference between Bayesian and Frequentist inference, with respect to fixed parameters and prior beliefs?
1. Define power - Be able to draw the picture with two normal curves with different means and highlight the section that represents Power.
1. Explain trade off between significance and power

#### **20. Data Products**
1. Explain REST architecture/API
1. Write a basic Flask API
1. Describe web architecture at a high level
1. Know the role of javascript in a web application
1. Know how to use developer tools to inspect an application
1. Write a basic Flask web application
1. Be able to describe the difference between online and offline computation

#### **21. k-th nearest neighbor (kNN)**
1. Write pseudocode for the kNN algorithm from scratch
1. State differences between kNN regression and classification
1. Discuss Pros and Cons of kNN

#### **22. Cross Validation & Regularized Linear Regression**
1. Perform (one-fold) cross-validation on dataset (train test splitting)
1. Algorithmically, explain k-fold cross-validation
1. Give the reasoning for using k-fold cross-validation
1. Given one full model and one regularized model, name 2 appropriate ways to compare the two models. Name 1 inappropriate way.
1. Generally, when we increase flexibility or complexity of model, what happens to bias? variance? training error? test error?
1. Compare and contrast Lasso and Ridge regression.
1. What happens to Bias and Variance as we change the following factors: sample size, number of parameters, etc.
1. What is the cost function for Ridge? for Lasso?
1. Build test error curve for Ridge regression, while varying the alpha parameter, to determine optimal level or regularization
1. Build and interpret Learning curves for two learning algorithms, one that is overfit (high variance, low bias) and one that is underfit (low variance, high bias)

#### **23. Exploratory Data Analysis (EDA)**
1. Define EDA in your own words.
1. Identify the key questions of EDA.
1. Perform EDA on a dataset.

#### **24. Linear Regression**
1. State and troubleshoot the assumptions of linear regression model.
1. Describe, interpret, and visualize the model form of linear regression: Y = B0+B1X1+B2X2+....
1. Relate Beta vector solution of Ordinary Least Squares to the cost function (residual sum of squares)
1. Perform ordinary least squares (OLS) with statsmodels and interpret the output: Beta coefficients, p-values, R^2, adjusted-R^2
1. Explain how to incorporate interactions and categorical variables into linear regression
1. Explain how one can detect outliers

#### **25. Logistic Regression**
1. Place logistic regression in the taxonomy of ML algorithms
1. Describe conditions under which logistic regression should work well.
1. Fit and interpret a logistic regression model in scikit-learn
1. Interpret the coefficients of logistic regression, using odds ratio
1. Explain the key differences and similarities between logistic and linear regression.  

#### **26. Classification Measures of Effectiveness**
1. Generate ROC curves, and calculate AUC scores
1. Describe the issues with imbalanced classes.
1. Define the classification metrics: accuracy, precision/recall, f1, sensitiviey/specificity
1. Contrast when you would use the aboves MOEs.
1. Explain the profit curve method for thresholding.
1. Explain how they deal with imbalanced classes.
1. Explain cost sensitive learning and how it deals with imbalanced classes.

#### **27. Decision Trees**
1. Thoroughly explain the construction of a decision tree (classification or regression), including selecting an impurity measure (gini, entropy, variance)
1. Understand the nature of the decision boundaries generated by decision trees, contrast with logistic regression
1. Recognize overfitting and explain pre/post pruning and why it helps.
1. Pick the ‘best’ tree via cross-validation, for a given data set.
1. Discuss pros and cons

#### **28. Random Forest**
1. Thoroughly explain the construction of a random forest (classification or regression) algorithm
1. Explain the relationship and difference between random forest and bagging.
1. Explain why random forests are more accurate than a single decision tree.
1. Explain how to get feature importances from a random forest using an algorithm
1. How is OOB error calculated and what is it an estimate of?  

#### **29. Boosted Trees**
1. Define boosting in your own words.
1. Be able to interpret boosting output
1. List advantages and disadvantages of boosting.
1. Compare and contrast boosting with other ensemble methods
1. Explain each of the tuning parameters and specifically how they affect the model
1. Learn, tune, and score a model using scikit-learn’s boosting class

#### **30. Perceptrons**
1. Explain the basic architecture of neural networks
1. Describe an activation function, and it's role in NNs
1. Explain how neural networks use back propagation during training.

#### **31. Gradient Descent**
1. Identify and justify use cases for and failure modes of gradient descent.
1. Write pseudocode of the gradient descent and stochastic gradient descent algorithms.
1. Compare and contrast batch and stochastic gradient descent - the algorithms, costs, and benefits.

#### **32. NLP**
1. Explain the syntactic similarity hypothesis, and how it informs basic text featurization.
1. Identify and explain ways of featurizing text.
1. Discuss basic dimensionality reduction techniques (i.e. stemming, lemmatization).
1. Featurize a text corpus in Python using `NLTK` and `scikit-learn`.
1. Explain part of speech tagging, named entity extraction.

#### **33. Naive Bayes**
1. Derive the naive bayes algorithm and discuss its assumptions.
1. Explain the role of Laplace smoothing.
1. Contrast generative and discriminative models.
1. Discuss the pros and cons of Naive Bayes.

#### **34. Clustering**
1. List the characteristics of a dataset necessary to perform K-means
1. Detail the k-means algorithm in steps, commenting on convergence or lack thereof.  
1. Use the elbow method to determine K and evaluate the choice
1. Interpret Silhouette plot
1. Interpret clusters by examining cluster centers, and exploring the data within each cluster (dataframe inspection, plotting, decision trees for cluster membership)
1. Build and interpret a dendrogram using hierarchical clustering.
1. Compare and contrast k-means and hierarchical clustering.

#### **35. Dimensionality Reduction**
1. List reasons for reducing the dimensions.
1. Describe how the principal components are constructed in PCA.
1. Interpret the principal components of PCA.
1. Determine how many principal components to keep.
1. Describe the relationship between PCA and SVD.
1. Compute and interpret PCA using sklearn.

#### **36. NMF**
1. Write down and explain the NMF equation.  
1. Compare and contrast NMF, SVD, and PCA, and k-means
1. Implement Alternating-Least-Squares algorithm for NMF
1. Find and interpret latent topics in a corpus of documents with NMF
1. Explain how to interpret H matrix?  W matrix?  
1. Explain regularization in the context of NMF.

#### **37. Graphs**
1. Define a graph and discuss the implementation.
1. List common applications of graph models.
1. Discuss the searching algorithms and applications of them.
1. Explain the various ways of measuring the importance of a node.
1. Explain methods and applications of clustering on a graph.
1. Use appropriate package to build graph data structure in Python and execute common algorithms (shortest path, connected components, …)
1. Explain the various ways of measuring the importance of a node.
1. Explain methods and applications of clustering on a graph.

#### **38. Bayesian Inference**
1. Contrast MAP with MLE
1. Identify the prior, posterior, and nominal likelihood in a Bayesian update formula
1. Explain a conjugate prior and how it encodes the strength of belief of a prior.

#### **39. Multi Armed Bandit**
1. Explain the difference between a frequentist A/B test and a Bayesian A/B test.
1. Define and explain prior, likelihood, and posterior.
1. Explain what a conjugate prior is and how it applies to A/B testing.
1. Analyze an A/B test with the Bayesian approach.
1. Explain how multi-armed bandit addresses the tradeoff between exploitation and exploration, and the relationship to regret.
1. Write pseudocode for the Multi-Armed Bandit algorithm.

#### **40. Recommender Systems**
1. Survey approaches to recommenders, their pros & cons, and when each is likely to be best.
1. Describe the cold start problem and know how it affects different recommendation strategies
1. Explain either the collaborative filtering algorithm or the matrix factorization recommender algorithm.  
1. Discuss recommender evaluation.  
1. Discuss performance concerns for recommenders.

#### **41. Image Analytics**
1. Describe how to convert images to data
1. Describe a haar cascade and HOG variables
1. Describe convolutional architectures for neural networks

#### **42. Transfer Learning**
1. Explain what transfer learning is
1. Use transfer learning to build a large, accurate convolutional neural network with limited training data

#### **43. Time Series**
1. Explain why time series data needs special treatment
1. Recognize when time series analysis could be applied
1. Define key times series concepts
1. Determine structure of a time-series using graphical tools  
1. Compute a forecast using Box-Jenkins Methodology
1. Evaluate models/forecasts using cross validation and statistical tests
1. Engineer features to handle seasonal, calendar, and periodic components
1. Explain taxonomy of exponential smoothing using ETS framework