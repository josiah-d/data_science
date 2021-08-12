## 1. SQL

Assume we have a table called `sales` with the following schema:

|user_id | item_id | sale_price | quantity_sold | quantity_remaining | wholesale_price | source |
|:--:| :--:|:--:|:--:|:--:|:--:|:--:|
| 2 | 45 | 25 | 300 | 120 | 18 | in_store |
| 567 | 5 | 12 | 282 | 360 | 9 | online |
| 57 | 200 | 9 | 84 | 70 | 5.40 | affiliate |
| 10 | 7 | 703 | 14 | 37 | 562 | online |
| ... | ... | ... | ... | ... | ... | ... |

1. Write a SQL query that returns total amount of revenue from the affiliate network.

2. Write a SQL query that returns total amount of revenue from each source.

3. Write a SQL query that returns the net profit for each item:
    - `(quantity_sold * sale_price) - ((quantity_sold + quantity_remaining) * wholesale_price)`
  
4. Write a SQL query that returns the total number of items sold where the sale_price was greater than 20
  
5. Design an algorithm that would tell you the minimum **Sale Price** for a specific item for you to still make a 10% profit if you sold all the remaining stock at that price. 

## 2. Joins 

What is the resulting table of...
1. An inner join
2. A left outer join
3. A full outer join

| employee_id | department_id | name | salary |
|:--:|:--:|:--:|:--:|
| 2 | 1 | Jon | 40000 |
| 7 | 1 | Linda | 50000 |
| 12 | 2 | Ashley | 15000 |
| 1 | 0 | Mike | 80000 |

and

| department_id | location |
|:--:|:--:|
| 1 | NY |
| 2 | SF |
| 3 | Austin |
