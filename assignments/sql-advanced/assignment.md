# SQL Pipelines from python

## Introduction
The data for this assignment is contained in the socailmedia database in your docker container. 

### How to run your docker container:

1. If you are on your personal computer and haven't set up postgres yet using the docker continer with the pre-loaded data sets, follow [these instructions](https://github.com/GalvanizeDataScience/docker/blob/master/reference/docker_postgres.md) to start a docker container.

### Connect to database

For this assignment we recommend using an IDE like DBeaver to access the postgres database, and write your initial queries. then execute them by accessing the postgres databases through python using a module called psycopg2. Directions for that follow the exercises and will be covered in the afternoon. We encourage you to try out that way of connecting when you come back to this assignment in the future.

There's a lot of calculations that are regularly needed. One thing that we can do is build a table that consolidates all the needed information into one table. We're going to build a pipeline that creates a table that's a snapshot of the system on that given day. In the real world, these tables would be ever changing as users register and do actions on the site. It's useful to have a snapshot of the system taken on every day.

The snapshot will be a table with these columns:

```
userid, reg_date, last_login, logins_7d, logins_7d_mobile, logins_7d_web, opt_out
```

Here's an explanation of each column:

* `userid`: user id
* `reg_date`: registration date
* `last_login`: date of last login
* `logins_7d`: number of the past 7 days for which the user has logged in (should be a value 0-7)
* `logins_7d_mobile`: number of the past 7 days for which the user has logged in on mobile
* `logins_7d_web`: number of the past 7 days for which the user has logged in on web
* `opt_out`: whether or not the user has opted out of receiving email


## Basic

### Part 1: Write the initial SQL pipeline

You are going to use the `psycopg2` module ([documentation](http://initd.org/psycopg/docs/)) to make a pipeline so that if you ran the following command on August 14, 2014, you would get a table called `users_20140814` containing the daily snapshot.

```shell
python create_users_table.py
```

Here's an example of a very simple pipeline which creates a table of the number of logins for each user in the past 7 days.

We hardcode in today as `2014-08-14` since that's the last day of the data, and pass in the timestamp as part of a dictionary in the second argument of `c.execute` to protect against SQL injection.

```python
import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia', user='postgres', host='localhost')
c = conn.cursor()

today = '2014-08-14'

# This is not strictly necessary but demonstrates how you can convert a date
# to another format
ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")

c.execute(
    '''CREATE TABLE logins_7d AS
    SELECT userid, COUNT(*) AS cnt, timestamp %(ts)s AS date_7d
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days'
    GROUP BY userid;''', {'ts': ts}
)

conn.commit()
conn.close()
```

**Don't forget to commit and close your connection!**

Here are some steps to get you started:

1. Create a pipeline like the example above that has the userid, registration date and the last login date.
2. Many Data Scientists build queryies using an IDE like DBeaver we used in the previous lesson, then run that query in the new pipeline (Build and run the query using DBeaver, then run the query again in python) We reccomend you try this approach.
3.	Now try adding an additional column.
	*HINT* Use temporary tables (we can create temporary tables a few different ways, 2 are shown below)

	```sql
	SELECT userid, tmstmp as reg_date
	INTO TEMPORARY TABLE reg_table
	FROM registrations

	CREATE TEMPORARY TABLE logins_7d_2014_08_14 AS
    SELECT userid, COUNT(*) AS cnt
    FROM logins
    WHERE logins.tmstmp > timestamp '2014-08-14' - interval '7 days'
    GROUP BY userid
	```

	The below query would get us towards the pipeline table--note that not every user has logged in within the last 7 days--use a left join.

	```sql
	SELECT reg.userid, reg.reg_date, login_7d.cnt as logins_7d
	FROM reg_table reg
	LEFT JOIN logins_7d_2014_08_14 login_7d
		ON reg.userid=login_7d.userid
	```
## Advanced

### Part 2: Complete the pipeline

Add the remaining fields to the snapshot table. As you add each one, verify the results. Does it produce the correct number of rows? Did the values of any other fields change? Check a couple values to make sure they are correct.

