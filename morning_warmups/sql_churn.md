## SQL Practice

### Tables

You have a SQL database of advertisers on your site and advertising campaigns.

**Table: _advertisers_**

| Column |  Type  |
|------------|---|
|  id  | int, primary key |
| name | string |
| city | string |
| state | string |
| business_type | string |

**Table: _campaigns_**

| Column |  Type  |
|--------|--------|
| campaign_id | int, primary key |
| advertiser_id | int, foreign key |
| start_date | date |
| duration | int |
| daily_budget | real |

### Questions
You would like to determine which advertisers are *churning*, which means leaving the site. First, we define churn as if a user hasn't had an ad running for 14 days.

1. We want to create a table for easy exporting on our churn prediction problem. Write a query to generate the following table:

**Table: _churn_**

| Column | Type |
|--------|------|
| advertiser_id | int |
| name | string |
| city | string |
| state | string |
| business_type | string |
| churn | bool |

The first 5 columns are from the advertisers table. The churn column has a boolean value of whether or not they have churned. Keep in mind that you'll need to use the duration to determine if the ad is still running. Checkout the documentation on postgres [time types](https://www.postgresql.org/docs/8.2/static/functions-datetime.html).


2. Say we have another table that has predicted results of churn.

**Table: _predicted_churn_**

| Column | Type |
|--------|------|
| advertiser_id | int |
| churn_prediction | bool |

Write a query using this table and the one you created in `1` to calculate each of the following metrics:
 * accuracy
 * precision
 * recall (aka sensitivity)
 * specificity

 The [confusion matrix wikipedia page](http://en.wikipedia.org/wiki/Confusion_matrix) has all of the metrics defined nicely in case you are getting them mixed up.
