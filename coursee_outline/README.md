<h2>This is the main branch of the course outline.
               Links and dates may not match any particular campus.
               Use the branch corresponding to your cohort.</h2>
               
# Welcome main Cohort!

## Welcome to the Galvanize Data Science Immersive!

Make sure you are on the branch of the `course-outline` repository corresponding to your cohort. This README is your primary resource for class activities and contains information about the program as well as links to pre-lecture resources, assignments and lecture materials. **Bookmark this page** and refer to it daily.

#  Weekly overview
The Data Science Immersive (DSI) has a total of 8 instructional weeks, 3 capstone weeks, 1 week-long break (Solo Week) and a final showcase/career week. Instructors will have limited availability during Solo Week.

There is a readiness assessment on Day 1 of the course and six assessments on Mondays following instructional weeks. Most Fridays during instructional weeks are a group case study day.

Capstone weeks are reserved for your capstone projects (see below) and mock job interiews. You will present your capstone 1 and 2 projects to your peers and instructors at the end of the capstone weeks. You will present your capstone 3 project to the data science community at the end of the course.

Click on the link to jump to a week of interest.

| Date | Topic |
| --- | --- |
| 5/17 | [Week 1: Programming for Data Science](#week-1-programming-for-data-science)
| 5/24 | [Week 2: Statistics](#week-2-statistics)
| 5/31 | [Week 3: Big Data](#week-3-big-data)
| 6/7 | [Week 4: Unit 1 Capstone](#week-4-unit-1-capstone)
| 6/14 | [Week 5: Supervised Learning and Regression](#week-5-supervised-learning-and-regression)
| 6/21 | [Week 6: Nonlinear Supervised Learning](#week-6-nonlinear-supervised-learning)
| 6/28 | [Week 7: NLP and Unsupervised Learning](#week-7-nlp-and-unsupervised-learning)
| 7/5 | [Solo Week](#solo-week)
| 7/12 | [Week 8: Unit 2 Capstone](#week-8-unit-2-capstone)
| 7/19 | [Week 9: Advanced Topics 1](#week-9-advanced-topics-1)
| 7/26 | [Week 10: Advanced Topics 2](#week-10-advanced-topics-2)
| 8/2 | [Week 11: Unit 3 Capstone](#week-11-unit-3-capstone)
| 8/9 | [Week 12: Showcase](#week-12-showcase)


## Other important links
* [Morning Warmups](https://github.com/GalvanizeDataScience/morning-warmups)
* [Solutions](https://github.com/GalvanizeDataScience/solutions) for warmups, assignments and assessments will be added to this repository. If a solution is missing, please tell an instructor!
* [Past student capstone projects](https://github.com/GalvanizeDataScience/project-proposals/blob/master/past_student_projects.md) Take a look for capstone ideas or resources to help you with your current capstone. Exemplary projects are marked with an asterisk.
* [Lectures](https://github.com/GalvanizeDataScience/lectures/tree/main) Links to lecture materials point to this repository. **`git clone` this repository and `git checkout main` to get the materials for your campus. `git pull` regularly to keep synchronized with the latest updates instructors make.**
* [Quick reference](./quick-reference) documents for software and python libraries used in the DSI. `DSI_quick_ref.pdf` contains all the documents in one file but each of the documents is also available individually. The `Git.pdf` is likely to come in handy everyday. The `DSI_Installation_Guide.pdf` is provided if you need to re-install VSCode and Anaconda's distribution of Python.
* [Notes](./notes) Please read about [pair programming](./notes/pairing.md), [program standards](./notes/standards.md) and [development workflow](./notes/workflow.md) during your first week. Instructors may ask you to read additional materials from this directory in the coming weeks.

## Capstone Projects
You will use the knowledge and skills you are gaining in this program to create personal projects of your choosing. You can talk about these projects and the skills you developed through them during job interviews. You will submit capstone proposals to the instructors for approval before the capstone weeks begin. Often, capstone 3 builds on work done in capstone 2 and sometimes even in capstone 1.

## Daily Outline
Each row corresponds to a day in the week tables below and contains the following fields:
* __Day__ Day of the week.
* __Readings__ Nightly preparation for the next day's lectures.
* __Repos__ The day's assignment(s).
* __Lead__ The instructor who is leading the day's activities.
* __Lectures__ The day's lecture materials.

Instructional days have a general schedule of:
* Morning Announcements
* Warmup, Review or Career-Services Activities
* Morning Lecture (~1.5 Hours)
* Morning Assignment
* Lunch
* Afternoon Lecture (~1.5 Hours)
* Afternoon Paired Assignment
* End-of-Day Review of Assignments and Announcements

## Schedule:

<br/>

### Week 1: Programming for Data Science
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 5/17| [Unix Tutorial](http://www.ee.surrey.ac.uk/Teaching/Unix/) <br/> [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) <br/> [Git Remote](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) <br/> [Pair Programming](notes/pairing.md) <br/> [Git Quick Reference](quick-reference/Git.pdf) <br/> [Five Types of Git Workflows](https://buddy.works/blog/5-types-of-git-workflows) <br/>  | [Unix for Data Science](http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/) <br/> [Development Workflow](notes/workflow.md) <br/> [What is git?](https://git-scm.com/videos) <br/>  | [Readiness Assessment](https://learn-2.galvanize.com/cohorts/2286) <br/> [Unix](https://github.com/GalvanizeDataScience/unix) ([std](standards/unix.md)) <br/>[Git Intro](https://github.com/GalvanizeDataScience/git-intro) ([std](standards/git-intro.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/unix) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/git-intro) <br/> |
|Tuesday 5/18| [Python code style](https://docs.python-guide.org/writing/style/#general-concepts) <br/> [A Taxonomy of Data Science](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/) (Extra) <br/> [Classes and objects](http://www.greenteapress.com/thinkpython2/html/thinkpython2016.html) <br/>  | [A Quick Tour of IPython Notebook](https://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/master/cookbook/A%20quick%20tour%20of%20IPython%20Notebook.ipynb) (Extra) <br/>  | [Python Intro](https://github.com/GalvanizeDataScience/python-intro) ([std](standards/python-intro.md)) <br/>[Object-Oriented Programming](https://github.com/GalvanizeDataScience/oop) ([std](standards/oop.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/python-intro) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/oop) <br/> |
|Wednesday 5/19| [Numpy Reading](notes/reading_material/numpy_reading.md) <br/> [Linear Algebra Review and Reference](http://cs229.stanford.edu/section/cs229-linalg.pdf) (Reference) <br/> [Linear Algebra for Deep Learning](http://www.deeplearningbook.org/contents/linear_algebra.html) (2.1&ndash;2.7) <br/> [Linear Algebra (precourse)](https://learn-2.galvanize.com/cohorts/1984/blocks/16/content_files/units/linear-algebra1/overview.md) <br/>  |  | [Numpy](https://github.com/GalvanizeDataScience/numpy) ([std](standards/numpy.md)) <br/>[Linear Algebra](https://github.com/GalvanizeDataScience/linear-algebra) ([std](standards/linear-algebra.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/numpy) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/linear-algebra) <br/> |
|Thursday 5/20| [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) <br/> [Pandas Top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/) <br/> [EDA with Pandas](http://nbviewer.ipython.org/github/cs109/content/blob/master/labs/lab3/lab3full.ipynb) (Extra) <br/> [Data Wranging with Pandas](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_04_wrangling.ipynb) (Extra) <br/> [Matplotlib Tutorial 0](http://matplotlib.org/users/pyplot_tutorial.html) (but avoid plt interface) <br/> [Matplotlib Tutorial 2](https://matplotlib.org/users/artists.html) <br/>  |  | [Pandas](https://github.com/GalvanizeDataScience/pandas) ([std](standards/pandas.md)) <br/>[Matplotlib](https://github.com/GalvanizeDataScience/matplotlib) ([std](standards/matplotlib.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/pandas) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/matplotlib) <br/> |
|Friday 5/21| [What is EDA?](https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm) <br/>  |  | [Pandas EDA Case study](https://github.com/GalvanizeDataScience/pandas-eda-case-study)  <br/>| XXX | |
<br/>

### Week 2: Statistics
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 5/24| [Review of Probability Theory](http://cs229.stanford.edu/section/cs229-prob.pdf) <br/> [Basic Probability](https://seeing-theory.brown.edu/basic-probability/index.html) <br/> [Binomial Distribution and Test](https://www.youtube.com/watch?v=J8jNoF-K8E8) <br/>  | [Types of probability distributions](https://www.youtube.com/watch?v=b9a27XN_6tg) <br/> [Constructing a probability distribution](https://www.youtube.com/watch?v=cqK3uRoPtk0) <br/> [Binomial testing](https://www.youtube.com/watch?v=J8jNoF-K8E8) <br/> [p-value](https://www.youtube.com/watch?v=5Z9OIYA8He8) <br/>  | [Assessment 1](https://learn-2.galvanize.com/cohorts/2286) <br/> [Probability Distributions](https://github.com/GalvanizeDataScience/probability-distributions) ([std](standards/probability-distributions.md)) <br/>[Binomial Tests](https://github.com/GalvanizeDataScience/binomial-tests) ([std](standards/binomial-tests.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/probability-distributions) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/binomial-tests) <br/> |
|Tuesday 5/25| [Bootstrapping Intro](https://www.youtube.com/watch?v=_nhgHjdLE-I) <br/> [Frequentist Inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) <br/> [The Central Limit Theorem](https://www.youtube.com/watch?v=YAlJCEDH2uY) <br/> [Central Limit Theorem](https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-mean/v/central-limit-theorem) <br/>  | [Introduction to sampling distributions](https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/what-is-sampling-distribution/v/introduction-to-sampling-distributions) <br/> [Sampling Distributions](https://www.youtube.com/watch?v=XLCWeSVzHUU) <br/> [Central Limit Theorem](https://www.youtube.com/watch?v=YAlJCEDH2uY) <br/>  | [Sampling Distributions](https://github.com/GalvanizeDataScience/sampling-distributions) ([std](standards/sampling-distributions.md)) <br/>[The Central Limit Theorem](https://github.com/GalvanizeDataScience/central-limit-theorem) ([std](standards/central-limit-theorem.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/sampling-distributions) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/central-limit-theorem) <br/> |
|Wednesday 5/26| [Maximum Likelihood](https://www.youtube.com/watch?v=XepXtl9YKwc) <br/> [Maximum Likelihood for Normal Distribution](https://www.youtube.com/watch?v=Dn6b9fCIUpM) (Optional) <br/> [MLE part 0](https://www.youtube.com/watch?v=I_dhPETvll8) <br/> [MLE part 2](https://www.youtube.com/watch?v=Z582V53dfr8) <br/> [MLE part 3](https://www.youtube.com/watch?v=jpHreXjtw1Q) <br/> [z-test VS t-test](https://www.youtube.com/watch?v=5ABpqVSx33I) <br/> [Hypothesis Testing](https://www.youtube.com/watch?v=-FtlH4svqx4) <br/>  |  | [Maximum-Likelihood Estimation](https://github.com/GalvanizeDataScience/maximum-likelihood) ([std](standards/maximum-likelihood.md)) <br/>[Hypothesis Testing](https://github.com/GalvanizeDataScience/hypothesis-testing) ([std](standards/hypothesis-testing.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/maximum-likelihood) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/hypothesis-testing) <br/> |
|Thursday 5/27| [Power Analysis](https://www.youtube.com/watch?v=lHI5oEgNkrk) <br/> [Getting Started with Docker](https://docs.docker.com/get-started/) (wait to install until class) <br/>  | [Power](https://www.youtube.com/watch?v=Rsc5znwR5FA) <br/> [What is Docker?](https://www.youtube.com/watch?v=u-YWtdbpEhQ) <br/>  | [Statistical Power](https://github.com/GalvanizeDataScience/statistical-power) ([std](standards/statistical-power.md)) <br/>[Docker](https://github.com/GalvanizeDataScience/docker) ([std](standards/docker.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/statistical-power) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/docker) <br/> |
|Friday 5/28| [Bayesian Intuition](https://www.youtube.com/watch?v=HZGCoVF3YvM) <br/> [Introduction to Bayesian statistics part I](https://mathcs.clarku.edu/~djoyce/ma218/bayes1.pdf) <br/> [Introduction to Bayesian statistics part II](https://mathcs.clarku.edu/~djoyce/ma218/bayes2.pdf) <br/>  |  | [Intro to Bayesian Statistics](https://github.com/GalvanizeDataScience/bayes-intro) ([std](standards/bayes-intro.md)) <br/>[Bayesian Hypothesis Testing](https://github.com/GalvanizeDataScience/bayes-testing) ([std](standards/bayes-testing.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/bayes-intro) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/bayes-testing) <br/> |
<br/>

### Week 3: Big Data
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 5/31|  |  | Holiday (Memorial Day) <br/> |  | |
|Tuesday 6/1| [SQL Zoo](https://sqlzoo.net) (tutorial 1&ndash;9) <br/> [Visual Explanation of Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) <br/>  | [What is SQL?](https://www.youtube.com/watch?v=27axs9dO7AE) <br/>  | [Assessment 2](https://learn-2.galvanize.com/cohorts/2286) <br/> [Introduction to SQL](https://github.com/GalvanizeDataScience/sql-intro/tree/2021-01-update) ([std](standards/sql-intro.md)) <br/>[Advanced SQL](https://github.com/GalvanizeDataScience/sql-advanced) ([std](standards/sql-advanced.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/sql-intro) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/sql-advanced) <br/> |
|Wednesday 6/2| [Little book of MongoDB](http://openmymind.net/mongodb.pdf) <br/> [Basic Web Scaping](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe) <br/> [Web Scraping Using BeautifulSoup](https://www.dataquest.io/blog/web-scraping-tutorial-python/) <br/>  | [Understanding MongoDB](https://www.youtube.com/watch?v=HWZRio7ukrk) <br/>  | [MongoDB](https://github.com/GalvanizeDataScience/mongo-db)  <br/>[Web Scraping](https://github.com/GalvanizeDataScience/web-scraping) ([std](standards/web-scraping.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/mongo-db) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/web-scraping) <br/> |
|Thursday 6/3| [AWS setup](https://github.com/GalvanizeDataScience/unix/blob/master/setup_aws.md) <br/> [Getting Started with AWS](https://aws.amazon.com/start-now/) <br/> [About AWS](https://aws.amazon.com/about-aws/) <br/>  | [What is AWS in 5 minutes](https://www.youtube.com/watch?v=3XFODda6YXo) <br/>  | [AWS](https://github.com/GalvanizeDataScience/aws) ([std](standards/aws.md)) <br/>[SQL and Dataframes in Spark](https://github.com/GalvanizeDataScience/spark-dfs) ([std](standards/spark-dfs.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/aws) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/spark-dfs) <br/> |
|Friday 6/4|  |  | [Spark Case Study](https://github.com/GalvanizeDataScience/spark-case-study)  <br/>| XXX | |
<br/>

### Week 4: Unit 1 Capstone
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 6/7|  |  | [Assessment 3](https://learn-2.galvanize.com/cohorts/2286) <br/> Begin Capstone 1 <br/> |  | |
|Tuesday 6/8|  |  | |  | |
|Wednesday 6/9|  |  | |  | |
|Thursday 6/10|  |  | |  | |
|Friday 6/11|  |  | Presentation in afternoon <br/> |  | |
<br/>

### Week 5: Supervised Learning and Regression
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 6/14| [K-Nearest Neighbors](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (pg 39&ndash;42,104&ndash;109) <br/> [Classifying with k-Nearest Neighbors](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (Section 2.1) <br/> [KNN (Learn)](https://learn-2.galvanize.com/cohorts/2286/blocks/244/content_files/knn/README.md) <br/> [The Bias-Variance Trade-Off](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (2.2.2) <br/> [Cross Validation](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (5&ndash;5.1.4) <br/> [Bias-Variance (Learn)](https://learn-2.galvanize.com/cohorts/2286/blocks/244/content_files/bias-variance/readme.md) <br/> [Cross Validation (Learn)](https://learn-2.galvanize.com/cohorts/2286/blocks/244/content_files/cross-validation/readme.md) <br/>  | [StatQuest - KNN](https://www.youtube.com/watch?v=HVXime0nQeI) <br/> [Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) <br/>  | [K-Nearest Neighbors](https://github.com/GalvanizeDataScience/knn) ([std](standards/knn.md)) <br/>[Cross Validation](https://github.com/GalvanizeDataScience/cross-validation) ([std](standards/cross-validation.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/knn) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/cross-validation) <br/> |
|Tuesday 6/15| [Practical Regression](https://cran.r-project.org/doc/contrib/Faraway-PRA.pdf) <br/>  | [Linear Regression(video)](https://www.youtube.com/watch?v=nk2CQITm_eo) <br/> [Linear Regression(blog)](https://towardsdatascience.com/linear-regression-using-python-b136c91bf0a2) <br/>  | [Predictive Linear Regression](https://github.com/GalvanizeDataScience/predictive-linear-regression) ([std](standards/predictive-linear-regression.md)) <br/>[Inferential Regression](https://github.com/GalvanizeDataScience/inferential-regression) ([std](standards/inferential-regression.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/predictive-linear-regression) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/inferential-regression) <br/> |
|Wednesday 6/16| [Introduction to Algorithms](http://ressources.unisciel.fr/algoprog/s00aaroot/aa00module1/res/%5BCormen-AL2011%5DIntroduction_To_Algorithms-A3.pdf) (Chapter 2 pg 16&ndash;42) <br/> [Regularization](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (6-6.1 pg 203&ndash;214,Optional) <br/> [Shrinkage Methods](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (6.2 pg 214&ndash;228) <br/> [Regularization (Learn)](https://learn-2.galvanize.com/cohorts/2286/blocks/244/content_files/regularized-regression/readme.md) <br/>  | [Regularization](https://www.youtube.com/watch?v=KvtGD37Rm5I&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=40) <br/>  | [Algorithmic Complexity](https://github.com/GalvanizeDataScience/algorithmic-complexity) ([std](standards/algorithmic-complexity.md)) <br/>[Regularized Regression](https://github.com/GalvanizeDataScience/regularized-regression) ([std](standards/regularized-regression.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/algorithmic-complexity) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/regularized-regression) <br/> |
|Thursday 6/17| [Logistic Regression](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (Chapter 5 pg 83&ndash;90) <br/> [Logistic Regression](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (pg 127&ndash;137) <br/>  | [Logistic Regression](https://www.youtube.com/watch?v=OCwZyYH14uw) <br/> [ROC curves](https://www.dataschool.io/roc-curves-and-auc-explained/) <br/>  | [Logistic Regression](https://github.com/GalvanizeDataScience/logistic-regression) ([std](standards/logistic-regression.md)) <br/>[Decision Rules](https://github.com/GalvanizeDataScience/decision-rules) ([std](standards/decision-rules.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/logistic-regression) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/decision-rules) <br/> |
|Friday 6/18|  |  | [Regression Case Study](https://github.com/GalvanizeDataScience/regression-case-study)  <br/>| XXX | |
<br/>

### Week 6: Nonlinear Supervised Learning
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 6/21| [Andrew Ng notes](http://cs229.stanford.edu/notes/cs229-notes1.pdf) (1&ndash;7,16&ndash;19) <br/> [Neural Networks Demystified](https://www.youtube.com/watch?v=bxe2T-V8XRs) (Parts 1&ndash;7) <br/> [What is a Neural Network](https://www.youtube.com/watch?v=aircAruvnKk) (Parts 1 and 2) <br/> [Neural networks and deep learning with Torch](https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/) (Lecture 9) <br/>  | [Gradient Decent](https://www.coursera.org/lecture/machine-learning/gradient-descent-8SpIM) <br/> [Multi-layer Perceptrons](https://www.youtube.com/watch?v=bH6VnezBZfI) <br/>  | [Assessment 4](https://learn-2.galvanize.com/cohorts/2286) <br/> [Gradient Descent](https://github.com/GalvanizeDataScience/gradient-descent) ([std](standards/gradient-descent.md)) <br/>[Multi-Layer Perceptrons](https://github.com/GalvanizeDataScience/perceptrons) ([std](standards/perceptrons.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/gradient-descent) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/perceptrons) <br/> |
|Tuesday 6/22| [Introduction to Time Series Analysis](https://algorithmia.com/blog/introduction-to-time-series) <br/> [Forecasting: principles and practice](https://otexts.com/fpp3/) (ch 1&ndash;3,8,9) <br/> [Time Series Analysis and its Applications](https://www.stat.pitt.edu/stoffer/tsa4/tsa4.pdf) (ch 1&ndash;3) <br/> [ARIMA Models in Python](http://conference.scipy.org/proceedings/scipy2011/pdfs/statsmodels.pdf) <br/> [Recursion](https://runestone.academy/runestone/books/published/pythonds/Recursion/toctree.html) <br/> [Recursion](https://github.com/GalvanizeDataScience/welcome/tree/master/readings/recursion) <br/> [Visual Introduction to Decision Trees](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) <br/> [Decision Trees](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (3&ndash;3.1 pg 37&ndash;48) <br/> [Decision Trees (Learn)](https://learn-2.galvanize.com/cohorts/2286/blocks/244/content_files/dec_tree/README.md) <br/>  | [Decision Trees](https://www.youtube.com/watch?v=7VeUPuFGJHk) <br/>  | [Time Series](https://github.com/GalvanizeDataScience/time-series) ([std](standards/time-series.md)) <br/>[Decision Trees](https://github.com/GalvanizeDataScience/decision-trees) ([std](standards/decision-trees.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/time-series) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/decision-trees) <br/> |
|Wednesday 6/23| [Ensembles](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (8.2 pg 316&ndash;321) <br/>  | [Random Forest](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&t=13s) <br/>  | [Random Forests - Implementation](https://github.com/GalvanizeDataScience/random-forests-implementation) ([std](standards/random-forests-implementation.md)) <br/>[Random Forests - Application](https://github.com/GalvanizeDataScience/random-forests-application) ([std](standards/random-forests-application.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/random-forests-implementation) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/random-forests-application) <br/> |
|Thursday 6/24| [Boosting](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (8.2.3 pg 321&ndash;323) <br/> [Boosting Methods](https://web.stanford.edu/~hastie/ElemStatLearn/download.html) (10&ndash;10.6 pg 337&ndash;350,Optional) <br/>  | [Gradient Boosting](https://www.youtube.com/watch?v=3CC4N4z3GJc) <br/>  | [Boosting - Implementation](https://github.com/GalvanizeDataScience/boosting-implementation) ([std](standards/boosting-implementation.md)) <br/>[Gradient Boosted Regressors](https://github.com/GalvanizeDataScience/gradient-boosted-regression) ([std](standards/gradient-boosted-regression.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/boosting-implementation) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/gradient-boosted-regression) <br/> |
|Friday 6/25|  |  | [Supervised Learning Case Study](https://github.com/GalvanizeDataScience/supervised-learning-case-study)  <br/>| XXX | |
<br/>

### Week 7: NLP and Unsupervised Learning
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 6/28| [Digital Image Processing Basics](https://www.geeksforgeeks.org/digital-image-processing-basics/) <br/> [Convolutional Neural Networks](https://cs231n.github.io/convolutional-networks/) <br/> [Intuitive Explanation of CNNs](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/) <br/>  | [Image processing](https://medium.com/future-vision/image-processing-and-its-future-implications-4-significant-benefits-65e8ead8d617) <br/> [Edge Detection](https://www.youtube.com/watch?v=XuD4C8vJzEQ&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=2) <br/>  | [Assessment 5](https://learn-2.galvanize.com/cohorts/2286) <br/> [Image Processing](https://github.com/GalvanizeDataScience/image-processing) ([std](standards/image-processing.md)) <br/>[Convolutional Neural Networks](https://github.com/GalvanizeDataScience/convolutional-neural-nets) ([std](standards/convolutional-neural-nets.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/image-processing) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/convolutional-neural-nets) <br/> |
|Tuesday 6/29| [Text Feature Extraction I](http://blog.christianperone.com/?p=1589) <br/> [Text Feature Extraction II](http://blog.christianperone.com/?p=1747) <br/> [Text Feature Extraction III](http://blog.christianperone.com/?p=2497) <br/> [NLP](http://www.datascienceassn.org/sites/default/files/Natural%20Language%20Processing%20with%20Python.pdf) (Sections 1.1&ndash;1.7) <br/> [NLP in Python](http://www.datascienceassn.org/sites/default/files/Natural%20Language%20Processing%20with%20Python.pdf) (3.6 pg 107&ndash;108) <br/> [Scalability of Semantic Analysis in NLP](https://radimrehurek.com/phd_rehurek.pdf) (Sections 1.1&ndash;1.7) <br/>  | [Basics of NLP](https://www.youtube.com/watch?v=d4gGtcobq8M) <br/> [Naive Bayes](https://www.youtube.com/watch?v=NFd0ZQk5bR4) <br/>  | [Natural Language Processing](https://github.com/GalvanizeDataScience/nlp) ([std](standards/nlp.md)) <br/>[Text Classification and Naive Bayes](https://github.com/GalvanizeDataScience/text-classification) ([std](standards/text-classification.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/nlp) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/text-classification) <br/> |
|Wednesday 6/30| [Clustering](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (pg 385&ndash;400) <br/> [PCA](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (ch 10.2 pg 374&ndash;385) <br/> [PCA Explained Visually](https://setosa.io/ev/principal-component-analysis/) <br/>  | [4 Types of Clustering](https://www.youtube.com/watch?v=Se28XHI2_xE) <br/> [StatsQuest - PCA](https://www.youtube.com/watch?v=HMOI_lkzW08) <br/>  | [Clustering](https://github.com/GalvanizeDataScience/clustering) ([std](standards/clustering.md)) <br/>[Principal-Component Analysis](https://github.com/GalvanizeDataScience/pca) ([std](standards/pca.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/clustering) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/pca) <br/> |
|Thursday 7/1| [SVD](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 11) <br/> [The why and how of NMF](https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/) <br/> [NMF: A Simple Tutorial in Python](http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/) <br/>  | [SVD](https://www.youtube.com/watch?v=gXbThCXjZFM&t=13s) <br/>  | [Singluar Value Decomposition](https://github.com/GalvanizeDataScience/svd) ([std](standards/svd.md)) <br/>[Topic Modeling with NMF](https://github.com/GalvanizeDataScience/topic-modeling) ([std](standards/topic-modeling.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/svd) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/topic-modeling) <br/> |
|Friday 7/2|  |  | [NLP Case Study](https://github.com/GalvanizeDataScience/nlp-case-study)  <br/>| XXX | |
<br/>

### Solo Week
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 7/5|  |  | Memorial Day; Relax and review <br/> |  | |
|Tuesday 7/6|  |  | |  | |
|Wednesday 7/7|  |  | |  | |
|Thursday 7/8|  |  | |  | |
|Friday 7/9|  |  | |  | |
<br/>

### Week 8: Unit 2 Capstone
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 7/12|  |  | [Assessment 6](https://learn-2.galvanize.com/cohorts/2286) <br/> Begin Capstone 2 <br/> |  | |
|Tuesday 7/13|  |  | |  | |
|Wednesday 7/14|  |  | |  | |
|Thursday 7/15|  |  | |  | |
|Friday 7/16|  |  | Presentation in afternoon <br/> |  | |
<br/>

### Week 9: Advanced Topics 1
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 7/19| [Flask](http://flask.pocoo.org/) <br/> [Flask Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) <br/> [HTTP Methods](http://www.w3schools.com/tags/ref_httpmethods.asp) <br/>  |  | [Building Data Products with Flask](https://github.com/GalvanizeDataScience/flask) ([std](standards/flask.md)) <br/>[Markov-Chain Monte Carlo](https://github.com/GalvanizeDataScience/mcmc) ([std](standards/mcmc.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/flask) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/mcmc) <br/> |
|Tuesday 7/20| [Social Network Analysis](http://www.asecib.ase.ro/mps/Social%20Network%20Analysis%20for%20Startups%20[2011].pdf) (ch 2 pg 19&ndash;38) <br/> [Graphs](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 10.1&ndash;10.2 pg 343&ndash;356) <br/> [Guide to LDA](https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d) <br/>  |  | [Introduction to Graphs](https://github.com/GalvanizeDataScience/graphs-searching) ([std](standards/graphs-searching.md)) <br/>[Latent Dirichlet Allocation](https://github.com/GalvanizeDataScience/latent-dirichlet-allocation) ([std](standards/latent-dirichlet-allocation.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/graphs-searching) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/latent-dirichlet-allocation) <br/> |
|Wednesday 7/21| [Content-Based Recommenders](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 9.1&ndash;9.2 pg 307&ndash;320) <br/> [Collaborative filtering](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 9.3 pg 320&ndash;327) <br/> [Collaborative filtering&ndash;based recommendation engines](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (14.4-14.5 pg 286&ndash;295) <br/>  |  | [Content-Based Recommenders](https://github.com/GalvanizeDataScience/content-based-recommenders) ([std](standards/content-based-recommenders.md)) <br/>[Similarity-Based Recommenders](https://github.com/GalvanizeDataScience/similarity-based-recommenders) ([std](standards/similarity-based-recommenders.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/content-based-recommenders) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/similarity-based-recommenders) <br/> |
|Thursday 7/22| [Dimensionality Reductions](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 9.4&ndash;9.5 pg 328&ndash;340)) <br/> [Matrix Factorization Techniques](https://datajobs.com/data-science-repo/Recommender-Systems-%5BNetflix%5D.pdf) <br/>  |  | [Factorization Recommenders](https://github.com/GalvanizeDataScience/factorization-recommenders) ([std](standards/factorization-recommenders.md)) <br/>[Recommender Case Study](https://github.com/GalvanizeDataScience/recommender-case-study)  <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/factorization-recommenders) <br/> |
|Friday 7/23|  |  | [Recommender Case Study](https://github.com/GalvanizeDataScience/recommender-case-study)  <br/>| XXX | |
<br/>

### Week 10: Advanced Topics 2
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 7/26| [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) <br/> [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) <br/>  |  | [Time Series and ARIMA](https://github.com/GalvanizeDataScience/time-series-arima) ([std](standards/time-series-arima.md)) <br/>[Recurrent Neural Networks](https://github.com/GalvanizeDataScience/recurrent-neural-nets) ([std](standards/recurrent-neural-nets.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/time-series-arima) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/recurrent-neural-nets) <br/> |
|Tuesday 7/27| [Autoencoders](http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/) <br/> [Gentle Introduction to Transfer Learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/) <br/> [Transfer Learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/) <br/>  |  | [Autoencoders](https://github.com/GalvanizeDataScience/autoencoders) ([std](standards/autoencoders.md)) <br/>[Transfer Learning](https://github.com/GalvanizeDataScience/transfer-learning) ([std](standards/transfer-learning.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/autoencoders) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/transfer-learning) <br/> |
|Wednesday 7/28| [Multi-armed bandit](http://stevehanov.ca/blog/index.php?id=132) <br/>  |  | [The Multi-Armed Bandit Problem](https://github.com/GalvanizeDataScience/multi-armed-bandit) ([std](standards/multi-armed-bandit.md)) <br/>[Reinforcement Learning](https://github.com/GalvanizeDataScience/reinforcement-learning) ([std](standards/reinforcement-learning.md)) <br/>| XXX | [AM](https://github.com/GalvanizeDataScience/lectures/tree/main/multi-armed-bandit) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/main/reinforcement-learning) <br/> |
|Thursday 7/29|  |  | [Fraud-Detection Case Study](https://github.com/GalvanizeDataScience/fraud-detection-case-study)  <br/>| XXX | |
|Friday 7/30|  |  | [Fraud-Detection Case Study](https://github.com/GalvanizeDataScience/fraud-detection-case-study)  <br/>| XXX | |
<br/>

### Week 11: Unit 3 Capstone
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 8/2|  |  | Begin Capstone 3 <br/> |  | |
|Tuesday 8/3|  |  | |  | |
|Wednesday 8/4|  |  | |  | |
|Thursday 8/5|  |  | |  | |
|Friday 8/6|  |  | |  | |
<br/>

### Week 12: Showcase
| Day | Readings| Intro+videos| Repos (Standards) | Lead | Lecture Materials | 
|:--:|:------------------------------|:------------------------------|:--|:--:|:--:| 
|Monday 8/9|  |  | |  | |
|Tuesday 8/10|  |  | |  | |
|Wednesday 8/11|  |  | |  | |
|Thursday 8/12|  |  | Demo Day <br/> |  | |
|Friday 8/13|  |  | Graduation <br/> |  | |


## Textbooks
* [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf): The book we use for the majority of machine learning readings.
* [Elements of Statistical Learning](https://web.stanford.edu/~hastie/Papers/ESLII.pdf): If ISLR doesn't have enough detail for you, then look in ESL by the same authors.
* [Machine Learning In Action](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing)
* [Deep Learning Book](http://www.deeplearningbook.org/) Intended as a deep learning text, its introductory treatment of probability, linear algebra and mathematics is excellent.
* [Forecasting: Principles and Practice](https://otexts.com/fpp2/) We introduce forecasting but it's a specialized discipline. This free text expands on the subject.

### Optional Texts
* [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)
* [Doing Data Science](http://www.amazon.com/Doing-Data-Science-Straight-Frontline/dp/1449358659): One of the best treatments of the field with plenty of case studies.
* [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do): Some of the `pandas` methods have changed (always reference `pandas` [online documentation](http://pandas.pydata.org/)) but a solid book on data analysis in Python.
* [Practical Data Science with R](http://www.manning.com/zumel/): through we will not use R, this is a stellar book for its content and theory.

## Video Series
* [Youtube lectures by Hastie and Tibshirani on Statistical Learning](https://www.youtube.com/watch?v=5N9V07EIfIg&list=PLOg0ngHtcqbPTlZzRHA2ocQZqB1D_qZ5V)
* [StatsQuest](https://www.youtube.com/user/joshstarmer) - A goofy but clear explanation of statistics and machine learning concepts.
* [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) Self-described as some combination of math and entertainment, this channel has explanations for many machine learning topics.

## Getting Help
* [Data Science Stack Exchange](http://datascience.stackexchange.com/)
* [Stats Stack Exchange](http://stats.stackexchange.com/)

## References

### Machine Learning
* [Machine Learning in Action](http://www.manning.com/pharrington/)
* [Programming Collective Intelligence](http://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325)
* [Machine Learning for Hackers](http://shop.oreilly.com/product/0636920018483.do)
* [An Introduction to Machine Learning](http://alex.smola.org/drafts/thebook.pdf)

### Statistics
* [Probabilistic Programming and Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
* [Think Stats](https://greenteapress.com/wp/think-stats-2e/)
* [Think Bayes](http://www.greenteapress.com/thinkbayes/)
* [All of Statistics](http://www.stat.cmu.edu/~larry/all-of-statistics/)
* [Mostly Harmless Econometrics](http://www.amazon.com/Mostly-Harmless-Econometrics-Empiricists-Companion/dp/0691120358)

### Computer Science/Programming
* [Think Python](https://greenteapress.com/wp/think-python-2e/)
* [Think Complexity: Analysis of Algorithms](http://greenteapress.com/complexity2/html/thinkcomplexity2003.html#sec20)


### Numpy/Scipy
* [scipy Lectures](https://scipy-lectures.github.io/intro/numpy/index.html)
* [Crash Course in Python for Scientist](http://nbviewer.ipython.org/gist/rpmuller/5920182)
* [Scientific Python Lectures](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-2-Numpy.ipynb)
* [Python Bootcamp Lectures](https://nbviewer.jupyter.org/github/profjsb/python-bootcamp/blob/master/Lectures/05_NumpyPandasMatplotlib/IntroNumPy.ipynb)
* [scipy Lectures](https://scipy-lectures.github.io)

### SQL
* [http://sqlfiddle.com/](http://sqlfiddle.com/)
* [http://use-the-index-luke.com/](http://use-the-index-luke.com/)
* [SQL School](http://sqlschool.modeanalytics.com/)


### scikit-learn
* [Introduction to Machine Learning with sklearn](http://researchcomputing.github.io/meetup_spring_2014/python/sklearn.html)
* [scikit-learn workshop](https://github.com/jakevdp/sklearn_pycon2014)
* [Machine Learning Tutorial](https://github.com/amueller/tutorial_ml_gkbionics)
* [Introduction to scikit-learn](http://nbviewer.ipython.org/github/tdhopper/Research-Triangle-Analysts--Intro-to-scikit-learn/blob/master/Intro%20to%20Scikit-Learn.ipynb)
* [Data analysis with scikit-learn](http://sebastianraschka.com/Articles/2014_scikit_dataprocessing.html)
* [Advanced Machine Learning with scikit-learn](https://us.pycon.org/2013/community/tutorials/23/)

### Extra
* [University of Colorado Computational Science workshops](http://researchcomputing.github.io/meetup_spring_2014/)
* [Networkx tutorial](http://snap.stanford.edu/class/cs224w-2012/nx_tutorial.pdf)

