The purpose of this test is to test your ability to build tools to collect, normalize, store, analyze and visualize “real world” data. The test is designed to take about four hours, but it is not timed. Please try to deliver your results within 24 hours.

You may also use any tools or software on your computer, or that are freely available on the Internet. We prefer that you use simpler tools to more complex ones and that you are “lazy” in the sense of using third party APIs and libraries as much as possible. (However, use of obscure, undocumented “black box” libraries is discouraged.)

Do as much as you can, as well as you can. Prefer efficient, elegant solutions. Prefer scripted analysis to unrepeatable use of GUI tools. For data security and transfer time reasons, you have been given a relatively small data file. Prefer solutions that do not require the full data set to be stored in memory.

There is certainly no requirement that you have previous experience working on this kind of problem, or that you be able to finish everything. Rather, we are looking for an ability to research and select the appropriate tools for an open­ended problem and implement something meaningful. We are also interested in your ability to work on a team, which means considering how to package and deliver your results in a way that makes it easy for us to review them. Undocumented code and data dumps is virtually useless; Commented code and a clear writeup with elegant visuals is ideal. Also consider how asking targeted questions to members of our team may allow you to get more done in less time.

## The Problem: Transform and Analyze Restaurant Data

### Part 1: Data Preparation and Reporting
You have been provided with a tab delimited data file called “merchant_stats.txt” that contain an extract of aggregated statistics based on credit card transactions and other data sources. A data dictionary for these files is attached.

Your first task is to create smaller data extracts of these files, then answer some basic questions about the data. Many of these questions could be answered with simple SQL queries if the data were loaded into a relational database such as MySQL or SQLite, but this is optional. You may also write analysis scripts to do the same job.

1. Write a script to extract the records from region 623 corresponding to the "OVERALL" segment.

2. Answer the following questions about the data.
    * How many merchants are there in each category?
    * Is merchant category (category_id) a function of MCC (merchant category code)?
    * What merchant categories have the highest daily transaction volumes on average? The lowest? Your own interesting question?

3. If you have not used a relational database to this point, could you nonetheless write SQL queries against these tables that would answer the given questions?


### Part 2: Clustering / Mining / Prediction
For this part, you may work with the full data files or any subset of data as you see fit. Can you find interesting patterns in the merchant data? For example, how would you identify the "best" merchants in a category? Can you find merchants that have disproportionate appeal to one or two customer segments? Are the merchant locations clustered? Can you find "hot" neighborhoods with clusters of popular merchants?

This is an open­ended question and you are free to answer as you see fit. In fact, we would love it if you find an interesting way to look at the data that we haven't thought of! Please provide us with both your code and an informative write­up of your results. If you do not have time to implement your solution, a detailed, actionable description of how you would attack the problem would also count in your favor.

### Resources
This data can be found on the time campsule under `data/challenges/c1`.

`merchant_stats.txt` - Data Dictionary Primary key is (uid,segment).

| Field       | Type       | Description            |
| ----------- | ---------- | ---------------------- |
| uid         | bigint(20) | Unique ID for merchant |
| mcc         | int(11)    | MCC (Merchant category code) associated with transactions in Bundle cards data |
| merchant_zip | varchar(5) | Merchant zip code, populated from matched merchant listing data |
| region | int(11) | region ID (Foreign key to DMA code listing in merchant_staging.zip_dma table) |
| category_id | int(11) | Bundle assigned category ID, based on numerous data sources. |
| segment | varchar(50) | Customer Segment statistics correspond to. |
| price_point | int(11) | Integer 1 to 5 indicating quintile of merchant's median (average?) transaction size |
| online | int(11) | Flag indicating whether merchant primarily does business online. |
| hh_count | int(11) | Number of households transacting with this merchant |
| txn_count | int(11) | Number of transactions by this segment at this merchant |
| txn_pct | double | Percentage of merchant transactions coming from this segment (Unweighted) |
| days_open | int(11) | Number of calendar days between first and last observed transactions for this merchant. |
| txn_mean | double | Mean transaction size in dollars |
| txn_median | double | Median transaction size in dollars |
| spend | double | Total dollars spent by this segment at this merchant |
| spend_mean | double | Mean spend per household by this segment at this merchant |
| freq_mean | double | Mean number of transactions per household by this segment at this merchant |
| pct_repeat | double | Percentage of customers from this segment that returned at least twice. |
| daily_txns | double | Mean daily transaction count (txn_count / days_open) |
| pop_index | double | ratio of daily transactions to the category average = daily_txns / category_average_daily_txns |
| price_index | double | ratio of average transaction cost to the category average = txn_mean / category_average_txn_mean |
| spend_index | double | ratio of average spending to the category average = spend_mean / category_average_spend_mean (no longer used) |
| freq_index | double | ratio of average frequency to the category average = freq_mean / category_average_freq_mean |
| repeat_index | double | ratio of pct_repeat to the average of pct_repeat in the category (no longer used)￼|
| pop_pct | double | Quantile of pop_index, force ranked to a uniform distribution (0­100) |
| freq_pct | double | Quantile of freq_index, force ranked to a uniform distribution (0­100) |

  
---------
`merchant_names.txt` - Data Dictionary.

| Field | Type | Description |
| ----- | ---- | ----------- |
| uid | bigint(20) | Unique ID for merchant (primary key) |
| y | decimal(9,6) | x coordinate of merchant location |
| x | decimal(9,6) | y coordinate of merchant location |
