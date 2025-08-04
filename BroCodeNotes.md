Data is store as field value pair, similar to json but technically is bson (binary javascript object notation).

A document is a group of field value pairs.
A collection is a group of one or more documents.
A database is a group of one or more collections.

Prerequisites: Know OOP.

MongoDB databases explained:
    show dbs
    use database_name
    use new_database    This will create a new db but if is empty will be invisible.
    db.createCollection("collection_name")  This creates a collection in the current db.
    db.dropDatabase()   To delete the current db.
    show collections    To show the collections on the current db.

How to insert documents:
    db.collection_name.insertOne({as many field value pairs as we want})
    db.collection_name.insertMany([{document1},{document2},{document3}])
    db.collection_name.find()  To print all the object.

Data types explaind:
    string
    integer
    double
    boolean
    date: new Date() or new Date("2025-07-28T20:55:55")
    null
    field (like array)
    nested document: {like dicts}

Sort and Limit documents on MongoDB:
    db.collection_name.find().sort({fiel:1})    alphabetical/ascending
    db.collection_name.find().sort({fiel:-1})    reverse alphabetical/descending
    db.collection_name.find().limit(n)          n is the limit
    db.collection_name.find().sort({field:1})limit(n)   sort and limit.

Find method on MongoDB:
    db.collection_name.find({query}, {projection})      query is like where in sql.
    example: db.collection_name.find({name:"Bernardo"})     This will return the specific document.
    also we can add more than one filter like: db.collection_name.find({name:"Bernardo", age:34})
    The projection parameter works a little different: We can type a field to search, like:
    db.collection_name.find({}, {name:true})    this will return all names in that collection.
    db.collection_name.find({}, {_id:false, name:true, age:true})

How to update documents:
    db.colection_name.updateOne(filter, update)
    db.colection_name.updateMany(filter, update)    If filter is a empty {} will select all fields.
    filter is the critirea body
    update parameter is what modifications we will like to apply
    We can add or change with the update parameter
    Example: db.collection_name.updateOne({name:"Bernardo"}, {$set:{preffession:"Engineer"}})
    This would add proffession to that document.
    Example: db.collection_name.updateOne({name:"Bernardo"}, {$unset:{preffession:""}})
    This would remove that field.
    Example: db.collection_name.updateMany({car:{$exists:false}}, {$set:{car:true}})
    This would add a car to everyone who hasn't a car field.

How to delete documents:
    db.collection_name.deleteOne(filter)
    db.collection_name.deleteMany(filter)
    filter is a body.
    Example: db.collection_name.deleteOne({name:"Bernardo"})
    Example: db.collection_name.deleteMany({relegion:false})
    Example: db.collection_name.deleteMany({field:{$exits:false}})   This will delete all which had that field.

Explain comparison operators:
    Are denoted with dollar sign: $
    Returns data based on value comparisons.
    ne is not equal.
    lt is less than.
    lte is less than or equal.
    gt is greater than.
    gte is greater than or equal.
    in checks if is in an array.
    nin checks if is not in an array.
    Example: db.collection_name.find({name:{$ne:"Bernardo}})
    Example: db.collectio_name.find({age:{$gt:10, $lte:80}})
    Example: db.collection_name.find({name:{$in:["Bernardo", "Patricia", "Joy"]})
    Example: db.collection_name.find({name:{$nin:["Bernardo", "Patricia", "Joy"]})

Explain Logical Operators:
    Returns data based on expressions that evaluate to true or false.
    $and
    $not
    $nor
    $or
    Example: db.collection_name.find({$and: [{student:true}, {age:{$lte:55}}]})
    Example: db.collection_name.find({$or: [{student:true}, {age:{$lte:55}}]})
    Example: db.collection_name.find({$nor: [{student:true}, {age:{$lte:55}}]})
    Example: db.collection_name.find({age:{$not:{$gte:55}}})    This will return null even values.

MongoDB indexes explained:
    Indexes support the efficient execution of queries in MongoDB. Wihtout indexes, MongoDB must perform a collection scan, i.e. scan every document in a collection, to select those documents that match the query statement. If an appropiate index exists for a query, MongoDB can use the index to limit the number of documents it must inspect.
    To check the stats of a query:
    db.collection_name.find({name:"Bernardo"}).explain("executionStats")
    To create an index of a document:
    db.collection_name.createIndex({name:1})
    To get all indexes documents:
    db.collection_name.getIndees()
    To drop an index:
    db.collection_name.dropIndex("index_name")

MongoDB collections explained:
    Collection is a group of documents.
    A database is group of collections.
    db.createCollection("collectionName", {capped:true, size:10000000, max:100}, {autoIndexId:false})
    Note: if capped is true we need to specified the size of the db. max is the maximum number of documents.
    To drop a collection: db.collectionName.drop()










































     
































