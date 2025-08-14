Connecting to MongoDB in Python.

Unit Overview.
    In this unit, you'll learn how to connect a Python application to a MongoDB Atlas cluster by using PyMongo, the official MongoDB driver for synchronous Python applications. First, you'll learn what MongoDB drivers are and how they’re used to connect applications to MongoDB. Next, you'll install PyMongo by using the pip package installer and explore best practices when creating a MongoClient instance. Finally, you'll learn how to troubleshoot some common connection and authentication issues.

Lesson 1: Using MongoDB Python Client Libraries.

    What database drivers are.
        Python applications require a set of libraries to interact with MongoDB.
        Drivers are the middleware between your application and your database.
        The official MongoDB drivers establish secure connections to a MongoDB cluster and execute database operations on behalf of client applications.
        MongoDB has two official Python drivers:
            PyMongo:
                For synchronous applications.
            Motor:
                For asynchronous Python applications.

    How MongoDB drivers are used to connect Python applications to MongoDB.
        The official MongoDB drivers:
            Adhere to language best practices.
            Allow full use of MongoDB deployment functionality.
            Make upgrading easier.
        In MongoDB website are:
            Usage examples.
            Driver fundamentals.
            API documentation.
            References.


Lesson 2: Connecting to an Atlas Cluster in Python Applications.
    Create a directory and a virtual enviroment.
    Instll PyMongo, the official MongoDB driver for synchronous Python applications.
    Connect a MongoClient instance.
    Use a single MongoClient (could be use on all databases).

    Apart: To install pip inside a venv:
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python get-pip.py

    Go to Atlas. -> Connect with my cluster -> Connect to your application Drivers -> Copy the connection string -> check connection.py file
    (we got connected from a python file).

    For a secure conection use: .env and instal dotenv with:     pip install python-dotenv

    Notes:
        An application should use a single MongoClient instace for all database requests.
        This is because creating MongoClients is resource intensive.
        Creating a new MongoClient for each request will degrade the application's performance.


Lesson 3: Troubleshooting a MongoDB Connection in Python Applications.

    It's common to experience connectivity issues when learning.
    Connectivity issues may result from systems put in place to protect your database.
    MongoDB has resources to help.

    Possible errors:
        Network Access -> Add IP Access List Entry. In the Atlas dashboard.
        Authentication -> Check the correct user and password.


Conclusion:
    Connecting to MongoDB in Python
        In this unit, you learned how to:
            Install the PyMongo driver by using the pip package installer.
            Connect a Python application to a MongoDB Atlas cluster.
            Use a single MongoClient instance for all database requests.
            Troubleshoot common connection and authentication issues.