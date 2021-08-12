# Using MongoDB with Docker
Courtesy Moses Marsh, Lead DSI instructor   

To create & start a container running the mongodb server,
```bash
$ docker run --name mongoserver -p 27017:27017 -v "$PWD":/home/data -d mongo
```
- the `-v` flag connects the filesystem in the container to your computer's filesystem. See the documentation for [docker volumes](https://docs.docker.com/storage/volumes/). 
  - Here, the container's folder `/home/data` will be mapped to whichever folder you ran the `docker run` command from (`$PWD`). If you want to make your entire home folder visible to the docker container, navigate to `~` before running the above command. If you only want the container to see, say, a folder you cloned from github, navigate to `/path/to/repo_folder` first. Any changes made to files in this folder are immediately visible to the container and your native file system. 

To start this container in the future, use the `start` command:
```bash
$ docker start mongoserver
```

To access the mongo terminal in the container,
```bash
$ docker exec -it mongoserver mongo
```
# Loading data into MongoDB
Suppose you have some data in `~/path/to/data_dump/really_important.json`. Assuming you ran `docker run` from your home folder `~`, you can access the file from the container as follows:
```bash
$ docker exec -it mongoserver bash
$ cd /home/data/path/to/data_dump/
$ mongoimport --db database_name --collection collection_name < really_important.json
```
This last command loaded the records in `really_important.json` into a collection in a database in the MongoDB server running in a docker container. 

# Using the MongoDB terminal  
Make sure you start the mongoserver: 
```bash
$ docker start mongoserver
```
Now, you have a couple options.
### Option 1: Simply start the Mongo shell  
```bash
$ docker exec -it mongoserver mongo
```
But perhaps you'd like to do some file system navigation first?  
### Option 2: File system navigation first
Access the command line within the container:  
```bash
$ docker exec -it mongoserver bash
```
Navigate to you system's home directory (in the container):
```bash
# cd /home/data
```
Start the Mongo shell
```bash
# mongo
```
## Mongo Shell Commands
| command | description | 
|:--|:--|
|`show dbs` | show databases|
|`use db_name` | connect to database `db_name`|
|`show collections` | show collections (tables) in the database|
|`db.collection_name.find()` | return all records in the collection |
|`db.collection_name.find().limit(5)`| return 5 records in the collection|
|`db.collection_name.findOne()` | return one record in the collection|
|`db.collection_name.find().count()` | return the count of all records|
|`db.collection_name.insert({field_name_1:'example_string', field_name_2:['ex_list_item1', 'ex_list_item2']})`|insert a record into the collection. Mongo will create an `_id` field if not provided.|


## Mongo Shell Query Examples

Say we have a collection called `users`. Let's add a few records.
```
db.users.insert({ name: 'Jon', age: '45', friends: [ 'Henry', 'Ashley']})

db.users.insert({ name: 'Ashley', age: '37', friends: [ 'Jon', 'Henry']})

db.users.insert({ name: 'Frank', age: '17',
                  friends: [ 'Billy'], car : 'Civic'})

db.users.find()
```
- Note: The three documents that we inserted into the above database didn't all have the same fields.
- Note: Mongo creates an `_id` field for each document if one isn't provided.


Now let's query these records based on some criteria:
```
db.users.find({ name: 'Jon'})               // find by single field

db.users.find({ car: { $exists : true } })  // find by presence of field

db.users.find({ friends: 'Henry' })         // find by value in array

db.users.find({}, { name: true })   // field selection (only return name)
```
A quick way to figure out how to write a Mongo query is to think about how you would do it in SQL and check out a resource like this Mongo endorsed [conversion guide](https://docs.mongodb.com/manual/reference/sql-comparison/#create-and-alter), or use something like a [query translator](http://www.querymongo.com/).

## Updating
```
// replaces friends array
db.users.update({name: "Jon"}, { $set: {friends: ["Phil"]}})

// adds to friends array
db.users.update({name: "Jon"}, { $push: {friends: "Susie"}})   

// upsert
db.users.update({name: "Stevie"}, { $push: {friends: "Nicks"}}, true)

// multiple updates
db.users.update({}, { $set: { activated : false } }, false, true)
```
[Documentation on updating](https://docs.mongodb.com/manual/reference/method/db.collection.update/)

[Documentation on aggregation](https://docs.mongodb.com/manual/reference/sql-aggregation-comparison/)

# Using PyMongo

First, install the pymongo package (in your system, not the container).
```bash
$ conda install pymongo
```
Make sure your mongoserver docker container is running:
```bash
$ docker start mongoserver
```
Make a database and collection in the Mongo shell to interact with using PyMongo. `database_name` and `collection_name` are proxies for whatever
you want to call the database and the collection:   
```bash
$ docker exec -it mongoserver mongo
# use database_name
# db.collection_name.save( {temp:"temp value to make db and collection"} )
# db.collection_name.find()
```  
The last command verifies that the database, collection, and record have
been created.

Then, on your system in Ipython or in a Python script:  
```python
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['database_name']
table = db['collection_name']
```
Use the `database_name` and `collection_name` you defined before.
Now you can use python to insert, update, and query records.
```python
example_record = {'name':'moses', 'age':31, 'friends':['ted', 'gahl']}

table.insert_one(example_record)

table.update_one({'name':'moses'}, {'$set':{'age':32}})

table.find() # returns a generator for all records

table.find_one() # returns one record

table.find({'age':30}) # find all records with age = 30

table.count_documents({}) # return the count of all records in the collection

# to view all the collections in a database
db.collection_names()
```

Here's the [official tutorial.](https://api.mongodb.com/python/current/tutorial.html)
