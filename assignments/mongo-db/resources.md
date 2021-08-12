1. [Mongo](#mongo)
2. [Pymongo](#pymongo)
3. [Requests & Beautiful Soup](#requests-and-beautiful-soup)

## Mongo

1. **Start mongo server:** Use `brew services start mongodb` (Mac OS X) or `sudo /etc/init.d/mongodb start` (Ubuntu Linux) to start MongoDB. 

2. **Open mongo terminal:** Run `mongo` which will open a mongo terminal.

3. **See existing databases:** `show dbs`

4. **Switch to database:** `use mydb`

    *Note:* This will create a new database if the database doesn't exist. Typos are dangerous!!

5. **Insert into collection:** `db.users.insert({name: 'Jon', age: '45', friends: ['Henry', 'Ashley']})`

    This will create the collection `users` if it doesn't already exist.

6. **List collections:** `db.getCollectionNames()`

7. **Get data:** Use a version of the find function

    * `db.users.find()`: get all entries
    * `db.users.findOne()`: get one entry

8. **Querying:** You can also use the `find` function to search via a query.

    * `db.users.find({name: 'Jon'})`: find by a single value of a field
    * `db.users.find({car: {$exists: true}})`: find if a field exists
    * `db.users.find({friends: 'Henry'})`: find by value in an array
    * `db.users.find({}, {name: true})`: return only some fields

9. **Update:** Modify an entry in a collection

    * `db.users.update({name: "Jon"}, {$set: {friends: ["Phil"]}})`
    * `db.users.update({name: "Jon"}, {$push: {friends: "Susie"}})`

Here is some of this code in action.

```
~$ mongo
MongoDB shell version: 2.6.6
connecting to: test

> show dbs
admin  (empty)
local  0.078GB

> use mydb
switched to db mydb

> db.users.insert({name: 'Jon', age: '45', friends: ['Henry', 'Ashley']})
WriteResult({ "nInserted" : 1 })

> db.users.insert({name: 'Ashley', age: '37', friends: ['Jon', 'Henry']})
WriteResult({ "nInserted" : 1 })

> db.users.insert({name: 'Frank', age: '17', friends: ['Billy'], car : 'Civic'})
WriteResult({ "nInserted" : 1 })

> db.users.find()
{ "_id" : ObjectId("55c27eaf241dbcd74eb3b60a"), "name" : "Jon", "age" : "45", "friends" : [ "Henry", "Ashley" ] }
{ "_id" : ObjectId("55c27ebb241dbcd74eb3b60b"), "name" : "Ashley", "age" : "37", "friends" : [ "Jon", "Henry" ] }
{ "_id" : ObjectId("55c27ebc241dbcd74eb3b60c"), "name" : "Frank", "age" : "17", "friends" : [ "Billy" ], "car" : "Civic" }

> db.users.findOne()
{
    "_id" : ObjectId("55c27eaf241dbcd74eb3b60a"),
    "name" : "Jon",
    "age" : "45",
    "friends" : [
        "Henry",
        "Ashley"
    ]
}

> db.users.findOne({name: "Ashley"})
{
    "_id" : ObjectId("55c27ebb241dbcd74eb3b60b"),
    "name" : "Ashley",
    "age" : "37",
    "friends" : [
        "Jon",
        "Henry"
    ]
}

> db.users.update({name: "Jon"}, {$set: {car: "Prius"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.users.findOne({name: "Jon"})
{
    "_id" : ObjectId("55c27eaf241dbcd74eb3b60a"),
    "name" : "Jon",
    "age" : "45",
    "friends" : [
        "Henry",
        "Ashley"
    ],
    "car" : "Prius"
}

> db.users.update({name: "Jon"}, {$push: {friends: "Billy"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.users.findOne({name: "Jon"})
{
    "_id" : ObjectId("55c27eaf241dbcd74eb3b60a"),
    "name" : "Jon",
    "age" : "45",
    "friends" : [
        "Henry",
        "Ashley",
        "Billy"
    ],
    "car" : "Prius"
}
```

*Note how the columns in mongo are not ordered and will possibly come out in different orders each time you print an entry!*

## Pymongo

Let's do the same things using `pymongo`, the python wrapper for mongo.

```python
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.mydb2
coll = db.users

coll.insert({'name': 'Jon', 'age': '45', 'friends': ['Henry', 'Ashley']})
coll.insert({'name': 'Ashley', 'age': '37', 'friends': ['Jon', 'Henry']})
coll.insert({'name': 'Frank', 'age': '17', 'friends': ['Billy'], 'car': 'Civic'})

print "All entries:"
print list(coll.find())
print

print "Just one:"
print coll.find_one()
print

print "Just Ashley:"
print coll.find_one({'name': 'Ashley'})
print

print "Added Jon's car"
coll.update({'name': "Jon"}, {'$set': {'car': "Prius"}})
print coll.find_one({'name': 'Jon'})
print

print "Added Jon's new friend Billy"
coll.update({'name': "Jon"}, {'$push': {'friends': "Billy"}})
print coll.find_one({'name': 'Jon'})
```

Here's the output you should expect:

```
All entries:
[{u'age': u'45', u'_id': ObjectId('55c39fbca3d3d0180a081d7d'),
  u'friends': [u'Henry', u'Ashley'], u'name': u'Jon'},
 {u'age': u'37', u'_id': ObjectId('55c39fbca3d3d0180a081d7e'),
  u'friends': [u'Jon', u'Henry'], u'name': u'Ashley'},
 {u'car': u'Civic', u'age': u'17', u'_id': ObjectId('55c39fbca3d3d0180a081d7f'),
  u'friends': [u'Billy'], u'name': u'Frank'}]

Just one:
{u'age': u'45',
 u'_id': ObjectId('55c39fbca3d3d0180a081d7d'),
 u'friends': [u'Henry', u'Ashley'],
 u'name': u'Jon'}

Just Ashley:
{u'age': u'37',
 u'_id': ObjectId('55c39fbca3d3d0180a081d7e'),
 u'friends': [u'Jon', u'Henry'],
 u'name': u'Ashley'}

Added Jon's car
{u'car': u'Prius',
 u'age': u'45',
 u'_id': ObjectId('55c39fbca3d3d0180a081d7d'),
 u'friends': [u'Henry', u'Ashley'],
 u'name': u'Jon'}

Added Jon's new friend Billy
{u'car': u'Prius',
 u'age': u'45',
 u'_id': ObjectId('55c39fbca3d3d0180a081d7d'),
 u'friends': [u'Henry', u'Ashley', u'Billy'],
 u'name': u'Jon'}
```

## Requests and Beautiful Soup

The [requests](https://pypi.python.org/pypi/requests) module is for getting data from the web (and also sending data). The [beautiful soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) module is for parsing html.

```python
import requests
from bs4 import BeautifulSoup

topic = 'Data_science'
url = 'https://en.wikipedia.org/wiki/{0}'.format(topic)
print 'making request to: {0}'.format(url)
r = requests.get(url)
print 'status code: {0}'.format(r.status_code)
# Note that it's best to explicitly use html.parser
soup = BeautifulSoup(r.text, 'html.parser')
print

print 'first paragraph:'
print soup.find('p').text
print 'number of paragraphs: {0}'.format(len(soup.find('p')))
print

print 'first image:'
print soup.find('img')
print "first image's source:\n{0}".format(soup.find('img')['src'])
print

print 'sections:'
sections = soup.find_all(class_='toctext')
print '\n'.join(section.text for section in sections)
```

Here is the output that you should expect (could be slightly different if the article has changed):

```
making request to: https://en.wikipedia.org/wiki/Data_science
status code: 200

first paragraph:
Data Science is the extraction of knowledge from large volumes of data that
are structured or unstructured,[1][2] which is a continuation of the field
data mining and predictive analytics, also known as knowledge discovery and
data mining (KDD). "Unstructured data" can include emails, videos, photos,
social media, and other user-generated content. Data science often requires
sorting through a great amount of information and writing algorithms to extract
insights from this data.
number of paragraphs: 15

first image:
<img alt="" data-file-height="48" data-file-width="48" height="40"
src="//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png"
srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/60px-Edit-clear.svg.png 1.5x,
//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/80px-Edit-clear.svg.png 2x" width="40"/>
first image's source:
//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png

sections:
Overview
History
Domain specific interests
Criticism
Research areas
Security Data Science
Clinical data science
Genomic data science
Agriculture
Further reading
References
External links
```
