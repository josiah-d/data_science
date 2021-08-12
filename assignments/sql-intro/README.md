# Structured Query Language (SQL)

## Learning Objectives

* Creating a database and populating it (putting data in it)
* Introduction to querying database tables
* Filtering database tables for specific records
* Querying multiple tables at once
* Working with sets
* Grouping and Aggregation

## Introduction

Structured Query Language (SQL) is the most common language for storing and manipulating data in  relational databases, which are databases based on collections of rectangular tables with named columns. As such, most data scientists make frequent use of SQL, and almost all make occasional use
of it.  Whether for generating reports, obtaining data to use in a machine learning model, or implementing a product based on data, using SQL is one of the most important skills you will master during this course. In this sprint, we'll be gaining familiarity with SQL fundamentals. We'll start with basic querying, and move on to joins, aggregations, subqueries, and working with sets. 

## The Basics

To start, read  [SQL for Data Scientists](http://bensresearch.com/downloads/SQL.pdf)  and become familiar with basic SQL commands, inner and outer joins, and basic grouping and aggregation functions.

We will be using [PostgresSQL](http://www.postgresql.org/), also known as Postgres, in this exercise, a popular implementation of SQL (there are many others, like MySQL and SQLite). PostgreSQL is fast, works well with both small and large amounts of data, and has useful extensions, such as [PostGIS](http://postgis.net/) for working with geographical data. The standard SQL commands you will practice using PostgreSQL will work in any SQL implementation.

While PostgreSQL mainly [adheres](https://www.postgresql.org/docs/current/features.html) to the [ISO SQL standard](https://en.wikipedia.org/wiki/SQL#Current_standard), there are a few extra functions implemented that we'll be using in later sprints. Check out the [PostgreSQL tutorial](http://www.postgresqltutorial.com/), which gives an overview of PostgreSQL's syntax and will be your reference going forward.

## Assignment

In [today's assignment](assignment.ipynb), you'll be using a GUI database tool, [DBeaver](https://dbeaver.io), for most of your work. The assignment is in a Jupyter Notebook that also contains solutions that are initally hidden but you can reveal after you have tried to answer each question. We suggest you fork this repository and clone it to your local machine so that you can modify, save, and push back to your Github your version of the assignment notebook.

At the end of the lecture, there are directions on how to connect to a database through Python but these will be covered in greater detail in the afternoon. Once you have a satisfactory answer to a question, remember to copy your SQL query to a text file for safekeeping. You'll submit all your finished queries at the end of the day as a pull request. Remember: _Commit Early, Commit Often_

## References

* [ModeAnalytics: The SQL Tutorial for Data Analysis](http://sqlschool.modeanalytics.com/)
* [PostgreSQL Tutorial from the Official Documentation](http://www.postgresql.org/docs/7.4/static/tutorial.html)
* [Postgres Guide](http://postgresguide.com/)
* [Statistics in SQL](https://github.com/tlevine/sql-statistics)
* [A Gentle Introduction to SQL Using SQLite](https://a-gentle-introduction-to-sql.readthedocs.io/en/latest/)
* [The fast-track, hands-on, no-nonsense introduction to SQL](https://techblog.rosedu.org/sql.html)
* [Introduction to SQL for Data Scientists (PDF)](http://bensresearch.com/downloads/SQL.pdf)

### Joins

* [A Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)
* [SQL Joins Explained](https://chartio.com/education/sql/joins)
