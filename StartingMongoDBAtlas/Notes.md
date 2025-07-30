Getting Started with MongoDB Atlas

Unit Overview
In this unit, you'll be introduced to everything you need to know to get started with MongoDB Atlas, our multi-cloud data platform. First, you'll learn the foundations of MongoDB and its architecture. We'll explore what it means for MongoDB to be a distributed database and offer a flexible schema in the form of the document model. Then, you'll get an overview of Atlas and its features, which provide a streamlined experience for working with MongoDB. Finally, you'll deploy your first Atlas cluster and explore the Atlas UI.

Lessons in This Unit
Lesson 1 - Foundations of MongoDB
Lesson 2 - MongoDB Architecture Overview
Lesson 3 - Atlas Overview
Lesson 4 - Deploying an Atlas Cluster
Lesson 5 - Exploring the Atlas UI



Lesson 1: Fundations of MongoDB.

MongoDB is:
    Distributed system architecture.
        Data shared across machines.
        If one machine fails, system can still function.
        Consistent service and reliability.
        Store data close to the source.
        Reduces latency. (The delay between when data is generated or sent and when it becomes available for use).
    Document model.
        Similar to JS Object Notation JSON.
        Documents is the JSON of a entity and a group of documents are a Collection.
        Polymorphic data: Refers to data that can take on multiple types whithin the same structure.
    Flexible schema.
        Each data record can have a unique structure.
        Permit various data types.
        Unstructured or semi-structured data.

        Example:
            Social Media App: 
                Post collection:
                    Text Post:
                        content
                    Photo Post:
                        photo_url
                        caption
                    Video Post:
                        video_url
                        title
                        duration
                    Live Stream Post:
                        date_filmed


Lesson 2: MongoDB Architecture overview.

    MongoDb architecture:
        Hierarchy architecture:
            Cluster
            Node
            Database
            Collection
            Document
        
        Document:
            Object and any related metadata.
            Field-value pairs.
            Data types: strings, numbers, dates, arrays, objects, and more.
        Collections:
            A collection is a group of documents that correspond to an entity.
            Can support multiple entities and different shapes.
        Database:
            We need to know that when we talk about a database we refer to a DBMS like MongoDB or Postgrade, etc.
            A group of collections.
        Nodes:
            A node is an individual mongoDB instance. This instance can be running in a physical machine, virtual machine or a container.
        Cluster:
            Is a group of mongoDB nodes.
            Cluster Types:
                Replica sets: high availability.
                    A group of mongod instances that maintain the same data set.
                    Mongod is the primary daemon process. (Daemon is a program that runs in the background of an OS, performing tasks without direct user interaction).
                Sharded clusters: scaling.

    CAP Theorem:
        It's impossible to simultaneously guarantee consistency, availability, and partition tolerance.
        Consistency:
            Every read receives the most recent write or an error.
        Availability:
            Every request (read or write) receives a response.
        Partition Tolerance:
            The system continues to function despite network partitions.
        MongoDB have Partition Tolerance, so the users have to manage the balance between Consistency and Availability (Read and Write Concerns).

    High availability: replication.
        Replication stores multiple copies of data across multiple nodes.
        Replication ensures that the database remains operational even if one node fails.
    
    Consitency: read and write concerns.
        Read Concern controls the consistency and isolation of tha data read from replica sets or shareded clusters.
        By default Read Concern is set to "local" in mongodb. This means that data is returned from the node where the request was run. This ensures high availability and low latency but can not guarantee consistency. But there are other settings can ensure consistency.

        Write Concern dictates the number of replica set members that must confirm a write operation.
        Write Concern by default is set to "majority". Majority of the replica set confirms the write is successful. Which allows for more consistent write operations.

        Together Read and Write Concerns allow us to balance performance availability and consistency according to your application's needs.
    
    Scaling: sharding.
        Sharding is the mechanism MongoDb uses to scale.
        Sharding provides horizontal scalability.
        You can add more shards to distribute the data.
        Sharding requires careful planning.
        Added complexity.
        Poorly balance clusters can degrade performance.
