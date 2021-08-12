from pymongo import MongoClient
import psycopg2
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords


def get_tokens(content):
    stop = set(stopwords.words('english'))
    snowball = SnowballStemmer('english')
    stemmed = (snowball.stem(word) for word in word_tokenize(content))
    return (word for word in stemmed if word not in stop)


def create_tables(cur):
    cur.execute('''DROP TABLE IF EXISTS urls;''')
    cur.execute('''DROP TABLE IF EXISTS wordlist;''')
    cur.execute('''DROP TABLE IF EXISTS wordlocation;''')

    cur.execute(
        '''CREATE TABLE urls (
            id integer PRIMARY KEY,
            url text,
            label text);
        ''')

    cur.execute(
        '''CREATE TABLE wordlist (
            id integer PRIMARY KEY,
            word text);
        ''')

    cur.execute(
        '''CREATE TABLE wordlocation (
            id integer PRIMARY KEY,
            url_id integer,
            word_id integer,
            location integer);
        ''')


def fill_tables(coll, cur):
    words = {}
    url_id = 0
    wordlocation_id = 0

    for article in coll.find():
        location_id = 0
        label = article['section_name']

        cur.execute('''INSERT INTO urls VALUES (%d, '%s', '%s');''' \
                    % (url_id, article['web_url'], label))

        content = ' '.join(article['content']).lower()
        for word in get_tokens(content):
            word = word.replace("'", "''")  # for postgres parsing
            if word not in words:
                word_id = len(words)
                words[word] = word_id
                cur.execute('''INSERT INTO wordlist VALUES (%d, '%s');''' % (word_id, word))
            else:
                word_id = words[word]
            cur.execute('''INSERT INTO wordlocation VALUES (%d, %d, %d, %d);''' \
                        % (wordlocation_id, url_id, word_id, location_id))
            location_id += 1
            wordlocation_id += 1
        url_id += 1

    print "num words:", len(words)
    print "num urls:", url_id
    print "len of wordlocation:", wordlocation_id


def create_indices(cur):
    cur.execute('''CREATE INDEX wordlist_word ON wordlist(word);''')
    cur.execute('''CREATE INDEX wordlocation_word_id ON wordlocation(word_id);''')
    cur.execute('''CREATE INDEX wordlocation_url_id ON wordlocation(url_id);''')

def create_bag_of_words(cur):
    # For our bag-of-words (and tf-idf) we will be calculating them using our tables.
    # Bag-of-words should be quite simple now that we have indexed our words.
    # Write a query to create a bag table, so that we have all the necessary data in one table:
    # Join (INNNER should be fine) wordlocation and wordlist to link a url_id with the words
    # the article contains. We can GROUP BY url_id and word.
    # Do a COUNT on this group to create a new table of our bag of words. Add an additional
    # column of the count of each word. This table should have columns for: word_id, url_id, and count.
    # This table is our bag (of words).
    query = '''
            CREATE TABLE bag_of_words

                AS  SELECT      word_id,
                                url_id,
                                count(*)

                    FROM        wordlist ws

                    JOIN        wordlocation wc
                    ON          ws.id = wc.word_id

                    GROUP BY    word_id, url_id;
            '''
    cur.execute(query)

def create_tfidf_view(cur):
    # CREATE [ OR REPLACE ] [ TEMP | TEMPORARY ] VIEW name [ ( column_name [, ...] ) ]
    #     [ WITH ( view_option_name [= view_option_value] [, ... ] ) ]
    #     AS query
    query = '''
            CREATE VIEW tfidf 
            ( 
                        word_id, 
                        url_id, 
                        tf_idf 
            ) 
            AS
            SELECT  tf.word_id,
                tf.url_id,
                tf.tf / log(document_qty.count / cast(w.count as decimal))

            FROM    (--divide total frequency in doc over max count
                SELECT      b.word_id, 
                        b.url_id, 
                        .5 + .5 * b.count / m.count  tf

                FROM        bag_of_words b
                
                JOIN        (--select word, count for most common words in each doc  
                        SELECT max_freq.url_id, 
                               max_freq.word_id, 
                               max_freq.count

                        FROM   (--calculate word, count for every word in each doc
                            SELECT   b.url_id, 
                                 b.word_id, 
                                 b.count, 
                                 row_number() OVER (partition BY url_id ORDER BY count DESC) rank 
                            FROM     PUBLIC.bag_of_words b)max_freq
                            
                        WHERE  max_freq.rank = 1)m 
                ON          m.url_id = b.url_id)tf 

            JOIN    (--calculate number of documents containing each word
                SELECT      w.word_id, 
                        Count(DISTINCT w.url_id) count
                        
                FROM        PUBLIC.wordlocation w 
                
                GROUP BY    w.word_id)w
            ON  w.word_id = tf.word_id

            JOIN    (
                SElECT COUNT(DISTINCT w.url_id) count

                FROM wordlocation w)document_qty
            ON  TRUE

            ORDER BY tf.tf / log(document_qty.count / cast(w.count as decimal));
  '''
  cur.execute(query)

def main():
    print 1
    client = MongoClient()
    coll = client.nyt_dump.articles
    print [j for i in coll.find() for j in i][0:100], 1/0

    conn = psycopg2.connect(dbname='articles', user='postgres', host='/tmp')
    cur = conn.cursor()
    print 2
    create_tables(cur)
    fill_tables(coll, cur)
    create_indices(cur)
    print 3
    create_bag_of_words(cur)
    print 4
    create_tfidf_view(cur)
    print 5
    conn.commit()
    conn.close()
    print 6


if __name__ == '__main__':
    main()
