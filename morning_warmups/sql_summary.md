
## Summary table

Given the following table:

| date | town | price |
| --- | --- | --- |
| 17/12/2015 | SF | 5 |
| 17/12/2015 | AB | 3 |
| 17/12/2015 | SJ | 6 |
| 17/12/2015 | SF | 6 |
| 18/12/2015 | SJ | 4 |
| 18/12/2015 | AB | 2 |

Create a SQL query that displays a summary table limited to towns SF, AB and SJ (ignore other towns):

| date | sf | ab | sj |
| --- | --- | --- | --- |
| 2015-12-17 | 11 | 3 | 6 |
| 2015-12-18 | 0 | 2 | 4 |

Sample code to add the input table to a database:

```sql

-- Add the table to a database:

CREATE TABLE sales (
  date DATE,
  town VARCHAR(10),
  price INTEGER
);

INSERT INTO sales (date, town,price)
VALUES
  (TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'SF', 5),
  (TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'AB', 3),
  (TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'SJ', 6),
  (TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'SF', 6),
  (TO_DATE('18/12/2015', 'DD/MM/YYYY'), 'SJ', 4),
  (TO_DATE('18/12/2015', 'DD/MM/YYYY'), 'AB', 2);

```
