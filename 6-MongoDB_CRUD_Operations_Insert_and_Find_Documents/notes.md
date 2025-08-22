MongoDB CRUD Operations: Insert and Find Documents

Unit Overview:
    In this unit, you will be introduced to CRUD operations in MongoDB by inserting and finding documents. Inserting and finding documents will help you discover the ease and usability of MongoDB. You'll also build your own queries that use comparison and logical operators. Using operators will make your queries more precise and, in turn, make your application easier to develop. Finally, you'll learn how to query elements in an array. Arrays are a crucial data type that you will encounter frequently, so it's important that you have a solid understanding of how to work with them.

Lesson 1: Inserting Documents in a MongoDB Collection.

    Apart: I'm installing MongoDB Shell in my work's PC.
    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v1

    mQINBGPILWABEACqeWP/ktugdlWEyk7YTXo3n19+5Om4AlSdIyKv49vAlKtzCfMA
    QkZq3mfvjXiKMuLnL2VeElAJQIYcPoqnHf6tJbdrNv4AX2uI1cTsvGW7YS/2WNwJ
    C/+vBa4o+yA2CG/MVWZRbtOjkFF/W07yRFtNHAcgdmpIjdWgSnPQr9eIqLuWXIhy
    H7EerKsba227Vd/HfvKnAy30Unlsdywy7wi1FupzGJck0TPoOVGmsSpSyIQu9A4Z
    uC6TE/NcJHvaN0JuHwM+bQo9oWirGsZ1NCoVqSY8/sasdUc7T9r90MbUcH674YAR
    8OKYVBzU0wch4VTFhfHZecKHQnZf+V4dmP9oXnu4fY0/0w3l4jaew7Ind7kPg3yN
    hvgAkBK8yRAbSu1NOtHDNiRoHGEQFgct6trVOvCqHbN/VToLNtGk0rhKGOp8kuSF
    OJ02PJPxF3/zHGP8n8khCjUJcrilYPqRghZC8ZWnCj6GJVg6WjwLi+hPwNMi8xK6
    cjKhRW3eCy5Wcn73PzVBX9f7fSeFDJec+IfS47eNkxunHAOUMXa2+D+1xSWgEfK0
    PClfyWPgLIXY2pGQ6v8l3A6P5gJv4o38/E1h1RTcO3H1Z6cgZLIORZHPyAj50SPQ
    cjzftEcz56Pl/Cyw3eMYC3qlbABBgsdeb6KB6G5dkNxI4or3MgmxcwfnkwARAQAB
    tDdNb25nb0RCIDcuMCBSZWxlYXNlIFNpZ25pbmcgS2V5IDxwYWNrYWdpbmdAbW9u
    Z29kYi5jb20+iQI+BBMBAgAoBQJjyC1gAhsDBQkJZgGABgsJCAcDAgYVCAIJCgsE
    FgIDAQIeAQIXgAAKCRAWDSa7F4W6OM+eD/sE7KbJyRNWyPCRTqqJXrXvyPqZtbFX
    8sio0lQ8ghn4f7lmb7LnFroUsmBeWaYirM8O3b2+iQ9oj4GeR3gbRZsEhFXQfL54
    SfrmG9hrWWpJllgPP7Six+jrzcjvkf1TENqw4jRP+cJhuihH1Gfizo9ktwwoN9Yr
    m7vgh+focEEmx8dysS38ApLxKlUEfTsE9bYsClgqyY1yrt3v4IpGbf66yfyBHNgY
    sObR3sngDRVbap7PwNyREGsuAFfKr/Dr37HfrjY7nsn3vH7hbDpSBh+H7a0b/chS
    mM60aaG4biWpvmSC7uxA/t0gz+NQuC4HL+qyNPUxvyIO+TwlaXfCI6ixazyrH+1t
    F7Bj5mVsne7oeWjRrSz85jK3Tpn9tj3Fa7PCDA6auAlPK8Upbhuoajev4lIydNd2
    70yO0idm/FtpX5a8Ck7KSHDvEnXpN70imayoB4Fs2Kigi2BdZOOdib16o5F/9cx9
    piNa7HotHCLTfR6xRmelGEPWKspU1Sm7u2A5vWgjfSab99hiNQ89n+I7BcK1M3R1
    w/ckl6qBtcxz4Py+7jYIJL8BYz2tdreWbdzWzjv+XQ8ZgOaMxhL9gtlfyYqeGfnp
    hYW8LV7a9pavxV2tLuVjMM+05ut/d38IkTV7OSJgisbSGcmycXIzxsipyXJVGMZt
    MFw3quqJhQMRsA==
    =gbRM
    -----END PGP PUBLIC KEY BLOCK-----

    Every document in our db has to have an _id field.
    It must be Unique.
    If not provided, will be auto-generated.

    Methods:
        Insert a single document:
        Use insertOne() to insert a document into a collection. Within the parentheses of insertOne(), include an object that contains the document data.

        Insert Multiple Documents:
        Use insertMany() to insert multiple documents at once. Within insertMany(), include the documents within an array. Each document should be separated by a comma.


    Lesson 2: Finding Documents in a MongoDB Collection.

        db.collection.find()

        If there are much more results, we can use it command to show more results.
        For specific value:
        db.collection.find({ field: { $eq: <value> } })
        db.collection.find({ field: <value> })
        db.collection.find({ field.object_key: <value>, field.object_key2: <other_value>})
        This las one is equal to:
        db.collection.find({field: {$eleMatch: {key1: value1, ...}}})

        $in
            The $in operator allows us to select all documents that have a field value equal to any of the values specified in the array.
            db.collection.find({
                field: { $in:
                    [value1, value2, ...]
                }
            })


Lesson 3: Finding Documents by Using Comparison Operations.

    $gt
    $lt
    $lte
    $gte

    <field>: { <operator>: <value> }

    Examples:
        db.sales.find({ "items.price": { $gt: 50}})
        db.sales.find({ "items.price": { $lt: 50}})
        db.sales.find({ "customer.age": { $lte: 65}})
        db.sales.find({ "customer.age": { $gte: 65}})


Lesson 4: Querying on Array Elements in MongoDB

    Query arrays in documents, and use $elemMatch

    A normal find will search the value even if is inside an array.
    If I want to search a value which is an element withing an array:
        db.collection.find({ field: { $elemMatch: {$eq: value} } } )
    We can use elemMatch also to select with multiple criteria:
        db.collection.find({ <field> : { $elemMatch: { <query1>, <query2>, ... } } } )
    Example:
        db.sales.find({
  items: {
    $elemMatch: { name: "laptop", price: { $gt: 800 }, quantity: { $gte: 1 } },},})
    

Lesson 5: Finding Documents by Using Logical Operators.

    $and

        db.<collection>.find({ $and: [ {<expression>}, {<expression>}, ...]})

        implicit syntax:
        db.<collection>.find( { <expression>, <expression> } )

    $or

        db.<collection>.find( { $or: [ {<expression>}, {<expression>}, ...]})


    Find a Document by Using Implicit $and
    Use implicit $and to select documents that match multiple expressions. For example:
        db.routes.find({ "airline.name": "Southwest Airlines", stops: { $gte: 1 } })

    Find a Document by Using the $or Operator
    Use the $or operator to select documents that match at least one of the included expressions. For example:
        db.routes.find({
            $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }],
        })

    Find a Document by Using the $and and $or Operator
    Use the $and operator to use multiple $or expressions in your query.
        db.routes.find({
            $and: [
                { $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }] },
                { $or: [{ "airline.name": "American Airlines" }, { airplane: 320 }] },
            ]
        })
    
        Example:
            db.routes.find( {
                $and: [
                    { $or: [
                        { dst_airport: "SEA" },
                        { src_airport: "SEA" }
                    ]},
                    { $or: [
                        { airline: "American Airlines" },
                        { airplane: 320 }
                    ]},
                ]
            })

        We can't store two fields with the same name in the same json object.
        Rule: When including the same operator more than once in your query, you need to use the explicit $and operator.
    

Conclusion:

    CRUD 1 - Inserting and Finding Documents
    In this unit, we learned how to insert and find documents in a collection with MongoDB. We also built queries with the following comparison operators:

    $gt (Greater Than)
    $lt (Less Than)
    $lte ( Less Than or Equal To)
    $gte (Greater Than or Equal To)

    We also used the following logical operators:

    $and
    $or

    Finally, we learned how to query elements in an array and how to use the $elemMatch operator.

    Resources
    Use the following resources to learn more about inserting and finding documents in MongoDB:
    Lesson 1 - Inserting Documents
    MongoDB Docs: insertOne()
    MongoDB Docs: insertMany()

    Lesson 2 - Finding Documents
    MongoDB Docs: find()
    MongoDB Docs: $in

    Lesson 3 - Finding Documents Using Comparison Operators
    MongoDB Docs: Comparison Operators

    Lesson 4 - Querying on Array Elements
    MongoDB Docs: $elemMatch

    MongoDB Docs: Querying Arrays

    Lesson 5 - Finding Documents Using Logical Operators
    MongoDB Docs: Logical Operators
    Associate Certification Course
    Did you know that by completing this unit you've finished 30% of the CRUD content necessary for the Associate Developer Certification exam?
    If you're interested in continuing, your next step is to review the following units:
    Unit 01: Getting Started with MongoDB Atlas
    Unit 02: The MongoDB Document Model
    Unit 03: Connecting to a MongoDB Database
    Unit 05: MongoDB CRUD: Replace and Delete
    Unit 06: MongoDB CRUD: Reading Query Results
    Unit 07: MongoDB Aggregation
    Unit 08: MongoDB Indexes
    Unit 09: MongoDB Atlas Search
    Unit 10: MongoDB Data Modeling
    Unit 11: MongoDB Transactions