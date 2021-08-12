## Solutions to Mongo Exercise

1. Import data into MongoDB

   `mongoimport --db clicks --collection log < click_log.json`

2. Use the clicks database

   `use clicks;`

3. Count the number of entries in the log table

   `db.log.count() #3069`

4. Print the first 10 entries

   `db.log.find().limit(10)`

5. Count the number of entries with the city `San Francisco`

   `db.log.find({cy: 'San Francisco'}).count()`

6. Count the distinct types of web browser.

   `db.log.distinct('a').length`

7. Count the `Opera` and `Mozilla` users.
   
   ` db.log.find({$or: [{'a': /Mozilla/}, {'a': /Opera/}]}, {'a': 1}).count()`


8. Convert field `t` to datetime object

   ```
   db.log.find({'t': {$exists: true}}).forEach(function(entry) {
    db.log.update({_id: entry._id}, {
                $set: {'t': new Date(entry.t * 1000)}
    })
   })

   # Check type
   typeof db.log.findOne({'t': {$exists: true}}).t
   ```

9. Sort the clicks by time

   ```
   db.log.find({'t': {$exists: true}}).sort({'t': 1})

   start = new Date("2013-05-17T07:09:57Z")
   end = new Date("2013-05-17T08:09:57Z")

   db.log.count({t: {'$gte': start, '$lt': end}}) #2949
   ```

10. Find most popular clicks

   ```
   db.log.aggregate(
            [
                {$group : {_id: '$u', count: {$sum : 1}} },
                {$sort: {count: -1}},
                {$limit: 1}

            ])
   ```

Extra Credit:

```
// flip lat, long
db.log.find().forEach(function(doc) {
    if (doc.ll) {
        db.log.update({_id: doc._id }, {$set : { ll : [doc['ll'][1], doc['ll'][0]]}});
    }
})

// add geo index
db.log.ensureIndex({ ll : "2d"})

// query with 50 miles of SF
db.log.find({ ll: { $near: [-122.4167, 37.7833], $maxDistance: 50/3959}}).pretty()
```


