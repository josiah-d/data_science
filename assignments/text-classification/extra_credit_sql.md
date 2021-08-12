## Extra Credit: SQL Practice with NLP and NYT data set

In this exercise, you will implement TFIDF using SQL.

Here's an overview of what we'll be doing:

1. Create SQL tables
2. Parse articles: single string of text => tokenized words
3. Index words + documents into SQL tables
4. Using SQL, calculate bag-of-words vectors for each document
5. Apply tf-idf weighting to feature vectors

## Setup

We are going to be building the following SQL tables to contain the article data. You're going to write a python script using `psycopg2`.

__urls__

| id | url | label |
| :--:| :--| :--: |
| 1 | `"http://nyt.com/hotdogs_in_the_park..."`| Dining & Wine |
| 2 | ...| ... |
| ... | ...| ... |

__wordlist__

| id | word |
| :--:| :--|
| 1 | "dog"|
| 2 | "car" |
| ... | ...|

__wordlocation__

| id | url_id | word_id | location|
| :--:| :--| :--| :--|
| 1 | 54 | 2 | 523 |
| 2 | 1 | 1 | 12 |
| ... | ...| ... | ...|

__urls table:__ mapping of url, label => url_id

__wordlist table:__ mapping word => word_id

__wordlocation table:__ connect words => urls. (location is position of word in article, i.e. "dog" is the 12th word in "http://nyt.com/hotdogs_in_the_park...")

You'll be using your work from this morning that extracted the words from the `articles_mongoimport.json`.

1. First create an 'articles' database and the tables you need. Recall how to use `psycopg2`:

    ```python
    import psycopg2

    conn = psycopg2.connect(dbname='articles', user='postgres', host='localhost')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE urls (
                       id integer PRIMARY KEY,
                       url text,
                       label text);''')
    ```

    Primary keys are useful for ensuring that there's only one entry with a given id. They also serve the purpose of making lookups by id fast.

2. Write a for loop to go over all the documents in the dataset and do an SQL insert. Your insert will look something like this:

    ```python
    cur.execute('''INSERT INTO urls VALUES (%d, '%s', '%s'); % (url_id, url, label)''')
    ```

3. Use some method of tokenization from the morning to split your documents into tokens. Also remove stop words and use stemming.

4. Write a loop to go over all of the words in all the documents.

    * If the word is new, add it to the `wordlist` table and assign it an id. It might be helpful to remember these ids in a python dictionary.
    * Add the word to the `wordlocation` table. Note that the columns you need to include are `id`, `url_id`, `word_id` and `location`. The location is what word number it is in the given document. The actual word won't be in this table.

6. You can also uses an [index](http://www.postgresql.org/docs/9.1/static/indexes-intro.html) to make lookups fast. Create indices for the following columns:

    * `word` in the `wordlist` table
    * `word_id` and `url_id` in the `wordlocation` table

7. This is essential what people call an "inverted index". Inverted indices are often used in information retrieval and search to find relevant documents. Write a python function that takes a search query to return all the articles containing those words.

    * You should first tokenize the query in the same manner you tokenized your documents
    * Strip out stop words
    * Use `psycopg2` to run the appropriate SQL query to get the result

## Bag of words

Yay! We now have a text index of (part of) the NYT. Now lets put those words into bags! In a [bag-of-words](http://en.wikipedia.org/wiki/Bag-of-words_model) model, each word has a unique index in the feature vector. This vector will be as wide as our corpus (i.e. the English language). In order to implement this in SQL, we will not need to actually create a separate (and VERY wide) table. This would be somewhat bad. Instead we will use our `wordlist` table. Its second column appropriate maps each word to a position in our feature vectors.

1. For our bag-of-words (and tf-idf) we will be calculating them using our tables.  Bag-of-words should be quite simple now that we have indexed our words.

    Write a query to create a `bag` table, so that we have all the necessary data in one table:
    * Join (INNER should be fine) `wordlocation` and `wordlist` to link a `url_id` with the words the article contains.  We can `GROUP BY` `url_id` and `word`.
    * Do a COUNT on this group to create a new table of our bag of words. Add an additional column of the count of each word. This table should have columns for: `word_id`, `url_id`, and `count`.

    This table is our bag (of words).

2. [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) is a short hop away from a bag.  We basically need to update our counts based on the total occurrence of words across all articles.  I will leave it up to you to use SQL aggregates and the method we have used above to create a [view](http://www.postgresql.org/docs/9.2/static/sql-createview.html) for tf-idf weighting as well.

   ![tf](https://upload.wikimedia.org/math/5/c/c/5cc18acd4dbd9be636047fc2a7a10105.png)

   ![idf](https://upload.wikimedia.org/math/6/9/1/691e665ba9ae9448219cedb8365bf961.png)

## Extra Credit: NYT Ranking

 Now that we have our bag of words and tf-idf scores we can start ranking.  Revisiting your query method, we can order our returned results intelligently.

 1. Using what we did at the start of this exercise (but this time in SQL), for a given query return the top three documents ranked by (aggregate) tf-idf score.  In other words, sum the tf-idf scores for the documents that contain the words in the query and return the top 3 that have the highest sums.

 2. The second technique to rank results is to consider where in the document the query occurs.  For a given query:
     * Sum up the word locations (from the wordlocation table) for each word in a query for each document. (if a word appears in multiple locations use the lowest).
     * Rank by lowest word location sum.  To compare these scores with the tf-idf tanking you must normalize them to be between 0 and 1 and invert them where the article with the lowest word location sum gets a 1 on this scale.

 3. Combine the tf-idf ranking and the word location ranking into one aggregate metric.  You may want to weight each differently.  Change the weights and see if it affects the return documents.
