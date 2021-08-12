## Warmup: Yelp API

**Include your code and answers in** `scrape_yelp.py`.

For this warmup we will scrape reviews from Yelp.  Just like the NYT (and any large tech company really), Yelp's power comes from its data in aggregate.  They will happily give you information on one restaurant or the text of one review, but it is quite hard to get __ALL__ of the reviews for __ALL__ of the restaurants.

We will be using the Yelp [API](http://www.yelp.com/developers/documentation) and the python [wrapper](https://github.com/yelp/yelp-python).  Look at the examples for how to use the wrapper in Python.

```python
# example in python, functions from wrapper

import yelp.search as yelp

host = "xxxx"
path = "xxxx"

url_params = {'term' : 'bars'}

yelp.request(host, path, url_params)
```

Assume we are building a restaurant recommendation engine based on user reviews.  The first step in this process is to get data.

1. Just like with the NYT you need to register to get an API key [here](http://www.yelp.com/developers/manage_api_keys)
1. Using the [Yelp API](https://www.yelp.com/developers/documentation/v3/business_search) find all Gastropubs in SF.
2. Store these records into MongoDB.
3. How many Gastropubs are there in SF?
