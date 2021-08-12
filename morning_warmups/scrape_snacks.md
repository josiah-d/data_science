## Warmup: Scraping

**Include your code and answers in** `scrape_snacks.py`.

This morning we will have a little fun exercise around web scraping to refresh your memory! Scrape [snackdata](http://www.snackdata.com), and use its data to answer the following questions (using mongoDB queries):

1. Create a record in mongoDB for each snack containing the following:
    * Name
    * Number of snack
    * Flavor
    * Cuisine
    * Series
    * Composition
    * Date it became an official snack
    * Description (text before taste description)
    * Taste description

## Extra Credit

1. Use Mongo [references](http://docs.mongodb.org/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/) to link ingredients to one another (in `Composition`)
2. How many snacks are there in total?
 
3. What are the most and least common cuisines?

4. Which is the most common ingredient across snacks? (Hint: Look at composition.)

5. What are the five most recently added snacks?

6. Make a histogram of the dates snacks have been added.
