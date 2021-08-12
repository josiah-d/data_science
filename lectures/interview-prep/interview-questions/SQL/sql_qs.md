1. You have the following tables

```
employees
    employee_id, name, department, salary

hired
    employee_id, date, department, salary
```

`employees` contains the current data about employees. `hired` contains has an entry for each time an employee is hired. Note that the department and salary could be different if the data has changed since they were hired.

- 1.1 Write a query to get the employee with the second highest salary.

- 1.2 Write a query to get the average salary for each department.

- 1.3 Find the user who has the highest salary increase since their start date.

- 1.4 What percent of current employees switched departments in under a year?


2. You are given the two tables. The first two rows of each table are shown.

    registrations
    
    | userid | date       |
    | ------ | ---------- |
    |      2 | 2014-03-07 |
    |      5 | 2013-12-21 |

    logins
    
    | userid | date       |
    | ------ | ---------- |
    |      2 | 2014-03-10 |
    |      2 | 2014-03-11 |

    Each user has one entry in the registrations table and any number of entries in the logins table.

    Write a query that gives the number of times each user logged in in their first week (i.e. within 7 days after registration)

    First write a query which doesn't include the users which have never logged in. Once you have that, add them with value 0.


3. Facebook prompts users with questions to answer to fill in their profile. You have the following table showing which questions the users have answered.

    | userid | questionid |
    | ------ | ---------- |
    |     10 |          4 |

    Each user will have an entry in the table for each question they've answered.

    Write a query which gives, for each individual user, a question to suggest for them to answer.


4. You are running an A/B test to test out a new feature. You have the following tables:

    test_groups
    
    | userid | group   |
    | ------ | ------- |
    |      3 | CONTROL |
    |     10 |       A |

    opt_out
    
    | userid |
    | ------ |
    |     14 |

    following
    
    | follower | followee |
    | -------- | -------- |
    |       10 |       14 |
    
    (This means user 10 is following user 14)

    The opt_out table contains the users which have opted out of receiving email.

    We would like to send an email to all the users who are in the test group A, who have not opted out of reviewing email and are following fewer than 30 users.


5. Write a query that gets all the users which have not received at least one message every day over the past 30 days.

    messages
    
    | sender | recipient | date       |
    | ------ | --------- | ---------- |
    |     12 |         3 | 2013-08-19 |

6. Given the below table *Content*, find the distribution for the number of comments on an *originating post* on '2015-09-07'.
   An *originating post* is the first post when person posts to her newsfeed. Basically, the number of posts on '2015-09-07' that received 0 comments, 1 comment, 2 comments, .... max comments.

    | Column | Type | Example |
    | --- | --- | --- |
    | ContentID | INT | 1 |
    | UserID | INT | 2 |
    | Date | Date | '2015-09-15' |
    | Type | VARCHAR(50) | One of ['like', 'url', 'comment', 'photo', 'share', etc] |
    | ReferenceID | INT | The ContentID for the original post; NULL if this is an original post  |
