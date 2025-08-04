MongoDB and the Document Model

In this unit, you will learn how the MongoDB document model offers flexibility and durability in order to meet the needs of modern applications. First, learn how documents are structured and the data types that are supported. Then, you'll learn how to create a database and a collection, and insert a document. Finally, you'll start to build a foundation in data modeling by learning concepts such as data relationships, embedding, and referencing.

Introduction to MongoDB.
    How MongoDB is commonly used.
    How data is organized in MongoDB.
    How the MongoDB database relates to Atlas developer data platform.
    Documents:
        Value types.
        Unique identifiers.
        Flexible Schema.
    Atlas Data Explore:
        View and interact with data.
    Objectives to learn:
        Explain fundamental MondoDB concepts.
        Manage data in the Atlas Data Explorer.


Lesson 1: Overview of the Document Model.

    Document structure:
        Documents is the smallest unit of data in mongodb. Multiple documents of an entity is a collection, and multiple collections are a database, and database is stored in a node which is in a cluster.
        Example of a document (field, value pair): field is the identifier and the value is the data itself.
            {
                title: 'Godfinger',
                year: 1964,
                plot: "this is a paragraph"
            }
        The fiels has to be:
            Strings.
            Unique withing the document.
            Descriptive.
        The values can have different data types:
            Strings.
            Numbers.
            Booleans.
            Arrays.
            Document Objects.
            Example:
                {
                    _id: ObjectID('45678654'),
                    plot: "this is a paragraph",
                    genres: ['action', 'adventure', 'thriller'],
                    runtime: 125,
                    imdb: { rating: 7.8, voting: 1254, id: 5557}
                }
        A golden rule in mongodb is that: data that is access together should be stored together in a single document.
        
    JSON vs. BSON:
        JSON example: {"hello": "world"}    human format.
        BSON example: \x16\x00\x00\x00      binary format.

        BSON is an extension of JSON and also provides additional data types as:
            Dates.
            ObjectId.
            Timestamps.
        
    Polimorphic data:
        MongoDb schema is flexible.
        Fields can have differents data types whithing documents in the same collection. And also documents can have some fields than others do not.
        Also we can add new field whiout the need of redesigning a table.
        Documents can hold different types of data like:
            Text.
            Geospatial data.
            Time-series.
            Graph data.

    Limits:
        A document can be a maximum of 16 MB.
        A document can have 100 nested levels.


Lesson 2: Data Types in MongoDB.
    MongoDB data types:
        Boolean:
            True/False.
        Null:
            Absence of a value or not value.
        String:
            Single or double quotes.
        Number:
            Intenger:
                Int32 or Int64.
            Floating-point values:
                Double.
                Decimal128.
        Object:
            Key:value pairs.
        Array:
            Groups of values of any data type.
        Dates:
            Represented as a timestamp.
            Efficient for querying and sorting.
            Epoch (milliseconds since January 1, 1970).
            Dates are:
                Compact, efficient for storage, easy to convert, fast comparisons and computations.
        ObjectId:
            This is unique identifier in MongoDB.
            _id
            Must be unique.
            MongoDb will autommatically generate unique ObjectId for _id.
            The ObjectId consits of:
                Timestamp.
                Random Value.
                Counter.


Lesson 3: Managing Databases, Collections, and Documents in Atlas.

    We are going to use Atlas:
        Navigate data.
        Create a Database.
        Create Collection.
        Add documents.
        Perform a query.


Lesson 4: Data Relationships.

    Start to think about data modeling.
    Funcdational concepts:

        Entities.
            Entities are unique and independent of each other.
            In MongoDB entities are represented by documents and group in collections.
            Example of entities: Each of these entities would correspond a collection of documents in MongoDB.
                Movies.
                Users.
                Comments.

        Attributes.
            Are characteristics that describe an entity.
            Attributes are the fiel-value pair withing the document.

        Realtionships amoung data:
            One to one.
                One entity is related to one other entity.
                Example: A movie is release by a single studio.
            One to many.
                One entity is related to other many entities.
                Example: A movie has multiple cast members.
            Many to many.
                Multiple entities are related to multiple other entities.
                Example: Theaters shown many movies.


Lesson 5: Embedding and Referencing:

    Those concepts are use to model the relationships between Entities.
    The choose between embedding and referencing depends on the relationships in the data.
    On One to One:
        Use embedding
        Keeps data together.
        Simplifies queries.
        Example of Movie to studio:
            {
                _id: ObjectId('sdsdsds'),
                title: "title cccsfdsds",
                studio: 'Universal Pictures'
            }
    For One to many:
        Embedding is preferred but we may want to use references when we have large datasets, or when the data is accessed independently.
        Example of Movie to cast:
        {
            _id: ObjectId('sdsdsds'),
            title: "title cccsfdsds",
            studio: 'Universal Pictures',
            cast: [
                'wefdsadfgfd',              This could be directly its value for embedding or reference id's for referencing.
                'asdfafdfsaddv',
                'asdsfdddvfs'
            ]
        }
    For many to many:
        You iether embedd or refereced or combined both. This will be discouse later.
        It is not recomended bidirectional referencing due to maintenance overhead.
        Also while reference reduces document size, increases complexity of queries needed to retrieve related information.

    Embedding:
        Access as single unit.
        Small, fixed-size related data.
        Minimize database operations.

    Referencing:
        Independent access.
        Large or growing documents.

    
Conclusion:
    In this unit, you learned how to:
        Describe MongoDB’s document model and the structure of documents.
        Explain the purpose of a flexible schema.
        List data types supported by MongoDB.
        Create a database and collection in the Atlas UI.
        Insert a document in a collection using the Atlas UI.
        Identify different types of data relationships: one-to-one, one-to-many, and many-to-many.
        Distinguish between embedding and referencing and when to use them.

    Resources:
        Use the following resources to learn more about MongoDB and the document model:
            Docs: MongoDB Use Cases.
            Docs: Documents.
            Docs: BSON Types.
            Explaining BSON with Examples.
            JSON and BSON.
            Docs: Interact with Your Data in MongoDB Atlas.
            Docs: Data Modeling.
            Embed or Reference Guidelines PDF.
            Docs: Database References.
            Docs: Model one-to-one relationships with embedded documents.
            Docs: Model one-to-many relationships with embedded documents.
            Docs: Model one-to-many relationships with document references.
            MongoDB University: Data Modeling Learning Path.