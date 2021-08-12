# MongoDB
MongoDB is a popular noSQL database.  Its loose structure makes it well suited for capturing unstructured data, such as that encountered in web scraping.  This sprint will focus on getting up and running with this system.  This is intended to be an individual sprint.


### Using Mongo with Docker
It is highly recommended you get used to using Docker.  See [Using Mongo with Docker](using_mongo_with_docker.md) for detailed instructions.  If you want to install MongoDB see instructions at the end of the assignment.  Again: this is not recommended. 


## Practicing Mongo Queries 

To get familiar with MongoDB, we are going to load in some click-log data from 
a government website and do some basic queries on it. Write your queries in a 
text file. Paste and run the queries in the Mongo shell.

1. Open a ***bash terminal in Docker***, navigate to the directory containing the data in Docker and load in the data with (for more detailed directions [see here](using_mongo_with_docker.md))    
   `mongoimport --db clicks --collection log < click_log.json`

2. **In the Mongo shell on Docker**, run `show dbs;` to make sure the `clicks` database has 
   been created. Run `use clicks;` to use the `clicks` database for your 
   queries.

3. Inspect the `log` collection in your database. How many entries are in the 
   `log` collection? 
   
   If you are not sure about what command to use, you can access the help 
   section by:
    - `help`
    - `db.help()`
    - `db.<collection_name>.help()`

   Mongo also has tab complete, so you can tab complete some of your commands 
   for convenience.  

4. Print out all of the clicks you have stored using `.find()`. Now using 
   `.limit()`, return 10 entries. You can also use `.findOne()` to quickly 
   view the first row and examine the available columns.  

5. Use `.find()` to find all the clicks where `cy` (city) is `San Francisco`. 
   How many are there?

6. Use `.distinct()` to find all the distinct types of web browsers (under the 
   field `a`) people use to visit the sites. Count the the number of distinct web 
   browsers (use `.length` on your distinct list). 

7. Select and count the records where the users have visited a website either 
   from a `Mozilla` or an `Opera` web browser. Search the `a` field using 
   [regex in mongo][mongo-like-query]. 

8. Find the type of the `t` (timestamp) field. You can access the type of a 
   field in an entry by using `typeof db.log.findOne({'t': {$exists: true}}).t`. 
   The field should be a `number` now.
   
   Convert the timestamp field to the date type. You will need to multiply the 
   number by 1000 and then make it a `Date` object (you can create a `Date` 
   object by using `new Date()`). You can loop over each record using 
   `.forEach()` and then [`.update()`][mongo-update] the record (using the `_id`
   field) with the created `Date` object. When you're done, confirm that the 
   data type has been converted. Below is some template code. 

   ```javascript
   db.log.find({'t': {$exists: true}}).forEach(function(entry) {
      // your code to update an entry by _id and set the t field as a new 
      //  Date() object
   })
   ```
   
9. Sort the clicks by the timestamp and find when the first click occurred. 
   How many clicks occurred in the first hour? To answer this, assign the 
   earliest timestamp and timestamp at the one-hour bound to separate variables
   before writing the query.

10. Using Mongo's [aggregation][mongo-aggregation] functionality, can you find 
    what the most popular link clicked is? You will need to use `$group`, 
    `$sum`, and `$sort`.


## AWS MongoDB Installation
You should already have a local Mongo docker container.  Let's practice our AWS skills by spinning up a micro instance and practice installing on a remote machine.

1. To install MongoDB, use your operating system's package manager:
   - Ubuntu Linux: `sudo apt-get install mongodb`

2. Much like Postgres, you will need to launch the server before using Mongo for the first time. 

   - Ubuntu Linux: `sudo /etc/init.d/mongodb start` 

3. Check your installation by opening the MongoDB Client:

   - Open a new terminal and type `mongo` to open up a Mongo shell
   - Type `show dbs;` to show the databases you have
   - You can exit by typing `exit`

4. Resources and quick references to Mongo commands:

   - [MongoDB Cheatsheet][mongo-cheatsheet]
   - [Mongo Docs][mongo-docs]
   - [MongoDB Reference Cards][mongo-ref-cards]



## Extra Credit

MongoDB actually has some [geospatial][mongo-geospatial] facilities (don't 
worry, PostGreSQL has [even better](http://postgis.net/) ones). Using the 
geoindices and Mongo queries, find the following:

1. All clicks within 50 miles of San Francisco
2. All clicks that came from [New England][New-England]

#### CartoDB

[CartoDB](http://cartodb.com/) happens to be one of my favorite tools for 
geospatial analysis (with built in PostGIS querying). Map the clicks across 
the globe.  Visualize clicks over time with a [torque map][torque-map].

### Additional GUI clients

Here are some additional GUI clients if you so want to try (my favorite is RoboMongo):
- [Robomongo (Multiplatform)](http://robomongo.org/)
- [MongoHub (Mac OSX)](https://github.com/fotonauts/MongoHub-Mac) 
   with down-loadable [binary](https://mongohub.s3.amazonaws.com/MongoHub.zip)
- [Humongous (web based)](https://github.com/bagwanpankaj/humongous)

[mongo-download]:http://www.mongodb.org/downloads?_ga=1.2370361.886345798.1422741448
[mongo-install]:https://docs.mongodb.org/master/tutorial/install-mongodb-on-os-x/
[mongo-cheatsheet]:https://blog.codecentric.de/files/2012/12/MongoDB-CheatSheet-v1_0.pdf
[mongo-docs]:http://docs.mongodb.org/v2.2/mongo/
[mongo-ref-cards]:http://semantic.supelec.fr/BigData/downloads/MongoDB-ReferenceCards15.pdf
[mongo-like-query]:http://stackoverflow.com/questions/3305561/how-to-query-mongodb-with-like
[mongo-update]:http://docs.mongodb.org/manual/reference/operator/update/set/
[mongo-aggregation]:http://docs.mongodb.org/manual/reference/sql-aggregation-comparison/
[mongo-geospatial]:http://docs.mongodb.org/manual/administration/indexes-geo/ 
[New-England]:http://en.wikipedia.org/wiki/New_England
[torque-map]:http://blog.cartodb.com/post/66687861735/torque-is-live-try-it-on-your-cartodb-maps-today


### Mac Install (Optional)
You don't need to install locally, however, if you prefer not to use Docker here are the Mac steps.
1. Install Mongo:
   - Mac OS X: `brew install mongodb`

2. Launch the server (note, you'll want to not have Docker running):
   - Mac OS X: `brew services start mongodb`


