# Spark Dataframes and SparkSQL

## Basic

### Part 1: Initiating a `SparkSession`

1\. Initiate a `SparkSession`. A `SparkSession` initializes both a `SparkContext` and a `SQLContext` to use RDD-based and DataFrame-based functionalities of Spark. If you launched a notebook using `bash scripts/jupyspark.sh`, the SparkSession and SparkContext will already be defined as `spark` and `sc`, respectively.

```python
import pyspark as ps
spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("sparkSQL exercise") 
        .getOrCreate()
        )
sc = spark.sparkContext
```

### Part 2: Introduction to SparkSQL

SparkSQL allows you to execute relational queries on **structured** data using
Spark. Today we'll get some practice with this by running some queries on a
Yelp dataset. To begin, you will load data into a Spark `DataFrame`, which can
then be queried as a SQL table.

1\. Load the Yelp business data using the function `.read.json()` from the `SparkSession()` object, with input file `data/yelp_academic_dataset_business.json.gz`.

2\. Print the schema and register the `yelp_business_df` as a temporary
table named `yelp_business` (use the `createOrReplaceTempView` method on your dataframe; this will enable us to query the table later using
our `SparkSession()` object).

Now, you can run SQL queries on the `yelp_business` table. For example:

```python
result = spark.sql("SELECT name, city, state, stars FROM yelp_business LIMIT 10")
result.show()
```

3\. Write a query or a sequence of transformations that returns the `name` of entries that fulfill the following
conditions:

   - Rated at 5 `stars`
   - In the `city` of Phoenix
   - Accepts credit card (Reference the `'Accepts Credit Card'` field by
   ``` attributes.`Accepts Credit Cards` ```.  **NOTE**: We are actually looking for the value `'true'`, not the boolean value True!)
   - Contains Restaurants in the `categories` array.  

   > Hint 1 : `LATERAL VIEW explode()` can be used to access the individual elements
   of an array (i.e. the `categories` array). For reference, you can see the
   [first example](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+LateralView) on this page.

   > Hint 2: In spark, while using `filter()` or `where()`, you can create a condition that tests if a column, made of an array, contains a given value. The functions is [pyspark.sql.functions.array_contains](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.functions.array_contains).

## Advanced

### Part 3: Spark and SparkSQL in Practice

Now that we have a basic knowledge of how SparkSQL works, let's try dealing with a real-life scenario where some data manipulation/cleaning is required before we can query the data with SparkSQL. We will be using a dataset of user information and a data set of purchases that our users have made. We'll be cleaning the data in a regular Spark RDD before querying it with SparkSQL.

1\. Load a dataframe `users` from `data/users.txt` instead using `spark.read.csv` with the following parameters: no headers, use separator `";"`, and infer the schema of the underlying data (for now). Use `.show(5)` and `.printSchema()` to check the result.

2\. Create a schema for this dataset using proper names and types for the columns, using types from the `pyspark.sql.types` module (see lecture). Use that schema to read the `users` dataframe again and use `.printSchema()` to check the result.

Note: Each row in the `users` file represents the user with his/her `user_id, name, email, phone`.

3\. Load an RDD `transactions_rdd` from `data/transactions.txt` instead using `sc.textFile`. Use `.take(5)` to check the result.

Use `.map()` to split those csv-like lines, to strip the dollar sign on the second column, and to cast each column to its proper type.

4\. Create a schema for this dataset using proper names and types for the columns, using types from the `pyspark.sql.types` module (see lecture). Use that schema to convert `transactions_rdd` into a dataframe `transactions`  and use `.show(5)` and `.printSchema()` to check the result.

Each row in the `transactions` file has the columns  `user_id, amount_paid, date`.

5\. Write a sequence of transformations or a SQL query that returns the names and the amount paid for the users with the **top 10** transaction amounts.
