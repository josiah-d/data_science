### C3 Energy 
1. Write an algorithm for find mean/median/mode for a continuous 1M stream of numbers. Do this in 20 mins and with minimal complexity. 

2. Re-derive linear regression optimization formulation in closed form for a spline function (flat then gradient) rather than `y = Ax + B`. Use matrix notation and assume tall-skinny problem. Talk about the complexity issues with closed form approach. Then extend to include regularization.
Write an algorithm to merge multi-edge polygons together given the edges and shared edges.

### Baysensors
1. Develop a solution for fusing sensors that are sensing the same goal. Sensors are time unsynchronized and conflict at times. You have some truth data too.

2. Write an algorithm to derive a line that cuts the number of points evenly on both sides of the line on a 2D Cartesian coordinate. e.g. 4 points on the left of the line and 4 points on the right. Assume even number of points.

3. Write a sorting algorithm.

### Facebook
1. How would you bring a metric to product X? Products at Facebook could be as large as News Feed or Ads, and as small as Pokes or Socrates (see below).

    Example 1: How would you assess the health of Facebook’s News Feed? (Define health ?)

    Example 2: Facebook’s Socrates is a box displayed under the Profile Picture of a user that prompts the user to answer questions about themselves, such as favorite movies, books, etc. Given the data about how users have answered questions in the past, design the best algorithm to present the next question that they will answer.

2. Compute the means, median, mode from a table using SQL
    Example: Using the data from this table, calculate the average length (in time) of a conversation on a particular post.

3. Use SQL to do an outer join & a self join.

4. Three ants are on different vertices of an equilateral triangle and can walk along the edges to any other vertex. What's the probability that any 2 of them will collide?

5.  Given a fleet of 50 trucks, each with a full fuel tank and   a range of 100 miles, how far can you deliver a payload? You can transfer the payload from truck to truck, and you can transfer fuel from truck to truck. Extend your answer for n trucks.

6. Given a string, test if it is a palindrome. Given a substring, test if it is a palindrome. Given a string, find all sub strings (not sub sequences) and test if any of them are palindromes. The naive solution takes too long, so can you find a way to test all sub strings in linear time?

Things they are looking for:
* Ask questions to make sure you understand what the question is asking.
* If you suggest any changes to the UI, explain also the engineering implications of those changes. 


### Khan Academy 

1. What's the difference between a decision tree and a decision forest?

2. How would you combat overfitting of a model? 

3. How would you use machine learning to predict a student's success on a subsequent question, based on knowing their performance on past questions they have answered?

4. Define a metric for [X problem were trying to solve].

5. Given this data set, what actions would you suggest be taken to improve user engagement?


### Tapad, Analytics Engineer

1. Which coding languages are you proficient in?  As a follow up, how would you rate your knowledge of Python, Java, and Scala?

2. What experience do you have with Hadoop or other map-reduce frameworks?

3. What experience do you have with databases?  In particular, SQL and Vertica.

4. What experience do you have with data visualization, anything from producing insightful graphs to more interactive d3 type interfaces?  Have you used something like d3?

5. How would you rate your knowledge of statistics?

6. I would also be interested to know why they are looking for a role like this versus a more traditional developer role or something else. 


### Facebook / Homejoy

1. How many McDonalds are there in the US?

2. How many piano tuners are in Seattle?

3. How many baseballs could you fit in a football stadium?


### Ericsson

How would you non-uniformly weight points on a linear regression? Said differently, how would you add weight to certain points and not others?  


### Tagged

1. Resume: Describe clearly what you did in past projects and what are future potential use cases.

2. Questions about modeling, SQL and regression.

3. Can you figure out SQL tricks and write SQL correctly?

4. Do you understand user engagement from user data?

5. How do you increase user engagement?

6. How do you establish a linear regression? What are outcome variables and independent variables? Can you translate the raw data into dummy variables? Think of ways to handle categorical variables.

7. What is cross validation?

8. Think of creative ways to combine features between source users and target users.

9. Can you pick a model to start with among several options with good reasoning?

10. People recommendation question.

11. Collaborative filtering method.

12. Identify the potential problem of cold-start and hot-getting-hotter problem, and propose good solutions.

13. Identify a correct way to establish features we can use in a ML model.

14. Figure out a way to deal with categorical features, or ways to increase the complexity of the model without new data points.

15. Questions on Neural Networks and data sampling.

16. Define user engagement in various ways (for example classification method).

17. Discuss about model selection, categorical variables encoding.

18. Identifying under-fitting problems.


### Walmart (Data Analyst)

1. Develop a recommendation engine for a product. Probability of men (Pm) liking a specific product is generally higher than probability of women liking it (Pf). What is the probability of a match between a man and a woman vs. a woman and a woman. What are the boundaries - that is, if Pm is greater than Pf, what are the likelihoods?

2. You have a clickthrough rate/impressions on two products, the first has a 1/100 CTR and the second has 100/10000 - how do you reconcile these rates and evaluate the performance of these two products?

3. If you were to run two coupon campaigns - one where users are sent popular coupons and the other are sent personalized (recommendation system) coupons, how do you design an experiment to measure the performance?


### Capital One (Data Scientist)

1. Map reduce a list of companies and their revenues sorted by industry.

2. What are the odds of getting at least one roll of 6 on six rolls of a fair die?

3. What are the odds of getting at least TWO rolls of 6 on twelve rolls?

4. What are the odds of getting at least one hundred 6s on six hundred rolls?

5. Whats MapReduce and how does it work?

6. You have a 300GB dat file, and you want to run a computation on the third column. How do you do that? - This is to check whether you know how to use unix commands that work off disk rather than in memory.

7. I give you a dollar and a list of coin denominations. How many different ways can you get change? - generator functions.

8. Case study - what features would you use to determine credit risk given transaction history from the past two years.

9. Explain a simple map reduce problem.

10. Read in a very large file of tab delimitted numbers using python and count frequency of each number (don't overthink this. Use python done in a few lines).

11. Whats more likely: Getting at least one six in 6 rolls, at least two sixes in 12 rolls or at least 100 sixes in 600 rolls?

12. Find all the combinations of change you can for a given amount.

### Yelp

1. Reservoir sampling (not only understanding, but also the code and the math behind it).

2. AB Testing on web site ad performance - ie, what are the locations on a web page that you can account and measure changes in user behavior.

3. If you had a magic wand and you can choose to send 100000 users to any number of businesses to improve Yelp’s functionality, what would you do?


### DeNA

1. 1000 players played level 1 in a mobile game. only 200 moved to level 2, what are the kinds of questions you would ask to explain this difference?

2. Take this sample SQL database and run queries and make some charts. There’s a discrepancy on X date, what kind of factors would play into this?

3. Player matchmaking features.

4. How do you incentivize users for higher engagement?

5. How would you use data science at our company?


### Accenture

1. What are the ACID properties of a database?

2. What data would you need to understand how company A would better compete with company B?

3. How do computer network architectures work?

4. Explain regression to a non-technical person. 

5. Write a function for the Fibonacci sequence. Explain why you used your approach instead of another.

6. Write a function to check for palindromes.

7. Write a function to calculate the acceleration of a car moving north for 5 minutes.

8. Write a function that returns True if a number (n) is prime, if the number is prime, the function should also return all prime numbers smaller than n.

9. What statistical method would you use to predict X?

10. How would you detect anomalies/fraudulent activity in a stream of a business data?

11. Where do you see yourself in 5 years?

12. Accenture’s Behavioral Interview - ie explain a situation with a coworker with which you had difficulty, greatest accomplishment, etc


### Hired.com

1. Stack Interview problem
    http://www.ardendertat.com/2011/11/08/programming-interview-questions-14-check-balanced-parentheses/


### NTT

1. How would you build a distributed, cloud-based machine learning system (like BigML)?

### Kabbage

1. How would you gauge overfitting?

2. How would you use map reduce to join two data sets on a common key? How would you do this is that key is not unique. 

3. List several ML techniques. Explain logistic regression and it's loss function. 

4. How does A/B testing work? Specifically say you are comparing recommender algorithms on a website. What metric of user behavior might you look at, how would you decide on sample size, etc. 


### Brightroll
The sim utilizes parking meter data available from the SFMTA(https://data.sfgov.org/Transportation/Parking-meters/7egw-qt89). The data dictionary can be found here. You can use absolutely any tools you want to answer the sim questions. Some questions may be easier to answer using a shell; others may be easier to answer using Excel.
Finally, we’re here as resources. You also have full access to the web.

1. How many total meters are included in this data set? 

2. How many smart meters? 

3. How many smart meters are on Geary Blvd? 

4. On how many distinct streets are there parking meters (of any kind)?

5. What are the top 5 streets (street names) with the most meters?

6. Produce a CSV of
    Street Name, Count of Meters

    Make sure the CSV has headers enumerating the fields. If this question takes more than 5 minutes, bug us for hints.

7. Based on the CSV produced in question 6, derive the following summary statistics:
    Mean, Median, Max, Range

8. If you worked for the SFMTA, what are some of the most interesting data here, and why? What data helps address interesting business questions? Are there data missing that would be required to answer pressing questions re: revenue, cost, etc.? Just dive in, have fun, and we’ll dig into your findings.


### LinkedIn
1. You have a table of every LinkedIn connection. Also, we define what a shared connection is below. Answer the below line of questions.

    ```
    Table Columns
    m_id = member id
    c_m_id = connection_member_id
    
    Table example
    m_id, c_m_id
    (user 1), (user 2)
    (user 3, (user 2)
    (user 1), (user 50)
    ...
    (user 50), (user 30)
    (user 51), (user 21)
    ```
    
    Shared Connection Definition
    The first two rows above are an example of 1 shared connection. So you could say "user 1 and user 3 have at least 1 shared connection", as shown here:
    
    ```
    User 1 -- User 2 -- User 3
    ```
    
    Questions
    1. Write a SQL query that finds the number of shared connections between user 1 and user 3
    2. Write a query that does the same thing in your favorite language
    3. Write a SQL query that finds the two users with the highest number of shared connections
    4. OK, now that won't work at scale because there are XX Billion connections. Write an approach that enables you to do this at scale in your favorite language. What algorithm might you consider using?

### Kwh
1. Find the difference in degrees between the hour and minute hand

### Zenefits - Data Analyst (Math Assessment) 
1. Find 2 primes whose SUM is 999.

2. Say you play a game where you roll a standard six-sided die, numbered 1 through 6 on each side. The goal is to get the highest possible roll. After the first try, you have the option of keeping your score, or rolling again. If you choose to roll again, you keep only what you get on the second roll. For example, you might roll a 2 on teh first roll, decide that is too low, and opt to roll again. If you roll a 1 on your second try, you score for that round is a 1. However, if you roll a 6 on the second roll, you score is a 6.  Think of how you would maximize your expected score for a round. What is this value for one round?

3. How many consecutie zeroes are at the end of 100! ?

4. Which SQL statement is used to return only difference values?

    ```
    SELECT DIFFERENCE
    SELECT UNIQUE
    SELECT DISTINCT
    SELECT VALUES
    ```
    
5. A casino has 10 slot machines. Eight of them are "Wheel of Fortune" themed, and two are "Jeopardy" themed. However, you do not know which machines are which. A "Wheel of Fortune" slot machine wins on 20% of its spins, while a "Jeopardy" machine wins on 30%. Say you play a round and are a winner. What is the probability that this is a "Wheel of Fortune" machine? ***Answer as a simplified fraction.***

6. What is the expected number of flips (of a fait coin, i.e. 50% change of heads, 50% change of tails) until you've flipped two heads in a row?

### Questions Not Assigned to a Particular Company

1. What is the difference between precision and recall?
