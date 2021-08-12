import requests, pymongo, json, time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup


# Url for NYT dev api
NYT_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
API_KEY = '81a22f3f3c6dfe5cd7d36d5a345117cd:3:66835804'

def init_mongo_client():
    # Initiate Mongo client
    client = pymongo.MongoClient()

    # Access database created for these articles
    db = client.nyt2015
    
    # Access collection created for these articles
    coll = db.articles

    # Access articles collection in db and return collection pointer.
    return db.articles


def call_api(url, payload, p=0):
    # Add the 'page' parameter to the payload.
    payload['page'] = p

    # Get the requested url. Error handling for bad requests should be done in
    # the calling function.
    return requests.get(url, params=payload)


def get_response(r):
    # Use json.loads to read the response text
    raw = json.loads(r.text)

    # Return the meta (hits, etc.) and docs (containing urls'n'stuff) back
    return raw['response']['meta'], raw['response']['docs']


def get_soup(url):
    # Header to be passed in to NYT when scraping article text.
    agent  = 'DataWrangling/1.1 (http://zipfianacademy.com; '
    agent += 'class@zipfianacademy.com)'
    headers = {'user_agent': agent}

    # Wrap in a try-except to prevent a maxTry connection error from erroring
    # out the program. Return None if there are any issues.
    try:
        r = requests.get(url, headers=headers)
    except:
        return None

    # Just in case there was a normal error returned. Pass back None.
    if r.status_code != 200: return None

    # Otherwise return a soupified object containing the url text encoded in
    # utf-8. Will toss back errors on some pages without the encoding in place.
    return BeautifulSoup(r.text.encode('utf-8'))


def get_body_text(docs):

    # Grab the url from each document, if it exists, then scrape each url for
    # its body text. If we get any errors along the way, continue on to the
    # next document / url to be scraped.
    result = []
    for d in docs:

        # Make a copy of the doc's dictionary
        doc = d.copy()

        # If there's no url (not sure why this happens sometimes) then ditch it
        if not doc['web_url']:
            continue

        # Scrape the doc's url, return a soup object with the url's text.
        soup = get_soup(doc['web_url'])
        if not soup:
            continue

        # Find all of the paragraphs with the correct class.
        # This class tag is specific to NYT articles.
        body = soup.find_all('p', class_= "story-body-text story-content")
        if not body:
            continue

        # Join the resulting body paragraphs' text (returned in a list).
        doc['body'] = '\n'.join([x.get_text() for x in body])

        print doc['web_url']
        result.append(doc)

    return result


def remove_previously_scraped(coll, docs):
    # Check to see if the mongo collection already contains the docs returned
    # from NYT. Return back a list of the ones that aren't in the collection to
    # be scraped.
    new_docs = []
    for doc in docs:
        # Check fo the document id in mongo. If it finds none, append to
        # new_docs
        cursor = articles.find({'_id': doc['_id']}).limit(1)
        if not cursor.count() > 0:
            new_docs.append(doc)

    if new_docs == []:
        return None

    return new_docs


def get_end_date(dt):
    # String-ify the datetime object to YYYMMDD, which the NYT likes.
    yr   = str(dt.year)
    mon = '0' * (2 - len(str(dt.month))) + str(dt.month)
    day = '0' * (2 - len(str(dt.day))) + str(dt.day)
    return yr + mon + day


def scrape_articles(coll, last_date):
    page = 0
    while page <= 10:
        print 'Page:', page

        # Request all of the newest articles matching the search term
        payload  = {'sort': 'newest',
                    'end_date': get_end_date(last_date),
                    'api-key': API_KEY}

        # Call the API with BaseURL + params and page
        r = call_api(NYT_URL, payload, page)

        # Increment the page before we encounter any potential errors
        page += 1

        # Check to see if the metadata didn't come back. USUALLY happens if
        # page > 100. When it does, reset the whole thing, roll the date back
        # one day, sleep for a couple seconds, then keep going.
        if r.status_code != 200:
            page = 0
            last_date += relativedelta(days=-1)
            print 'End Date:', get_end_date(last_date)
            time.sleep(2)
            continue
            
        # Get the meat data & documents from the request
        meta, docs = get_response(r)

        # Check if docs are already in the database
        new_docs = remove_previously_scraped(coll, docs)
        if not new_docs: continue

        # Grab only the docs that have these tags
        docs_with_body = get_body_text(new_docs)

        for doc in docs_with_body:
            try:
                # Insert each doc into Mongo
                coll.insert(doc)
            except:
                # If there's any error writing it in the db, just move along.
                continue


if __name__ == '__main__':

    # Initialize db & collection
    articles = init_mongo_client()

    # Set the initial end date (scraper starts at this date and moves back in
    # time sequentially)
    last_date = datetime.now() + relativedelta(days=-2)

    # Pass the database collection and initial end date into main function
    scrape_articles(articles, last_date)