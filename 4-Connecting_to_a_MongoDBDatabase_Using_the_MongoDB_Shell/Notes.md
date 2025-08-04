Connecting to a MongoDB Database Using the MongoDB Shell

Learn how to connect to MongoDB databases by using a connection string and the MongoDB Shell, an enviroment for interacting with MongoDB deployments.

Unit Overview.
    In this unit, you'll learn how to connect to a MongoDB database by using the MongoDB Shell, an environment for interacting with your MongoDB deployments in Atlas, locally, or on another remote source. First, you'll learn where to find your connection string in Atlas so that you can connect to your cluster. You'll also learn the components of a connection string. Then, you'll learn how to install and connect to the MongoDB Shell, as well as troubleshoot common connection errors. Finally, you'll learn some basics of using the MongoDB Shell, such as inserting and retrieving documents, running JavaScript functions, and switching between databases.


Lesson 1: Using MongoDB Connection Strings.
    Before to start working with our data, we need to connect with our Atlas Clouster. To do that we need our connection string.

    Connection string.
        MongoDB provides two formats for the connection string:
            Standard format.
            SRV format.
                This is used by default.
                This indicates the Client (mongodb shell) that the Host name that follows correspond to the DNS SRV Record. Then mongodb Client query the DNS Server for run instances of MongoDB.

    Connection string components.
        This is how a connection string is compose: the [] are optional:
            mongodb[+srv]://[<username>:<password>@]host1[:port1][,...hostN[:portN]][/defaultauthdb][?options]
        Example:
            mangodb+srv://<username>:<password>@cluster0.a56xnxt.mongodb.net:2500/my_ldapdb?retryWrites=true&w=majority
            mongodb     is a required prefix.
            +srv        automatically sets the TLS option to true and tells MongoDB to use the DNS seed list. The DNS seed list has a list of hosts behind it that we connect to.
            <username>:<password>   These are optional but must be provided if control access is enable. In Atlas is needed.
            @cluster0.a56xnxt.mongodb.net:2500  We need to specified the host and the port can be or has one by default 2701.
            defaultauthdb   This is optional to check the user credentials against.
            ?retryWrites=true&w=majority    These are query strings to connection specific options. These are key-value pairs.

    Find it in Atlas UI.
        In the custer we have, there is a Connect button. (I couldn't connect :/).


Lesson 2: Installing and connecting to the MongoDB Shell.

    Follow these commands:
        sudo apt update
        sudo apt install gnupg
        wget -qO- https://www.mongodb.org/static/pgp/server-7.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-7.0.asc
        echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
        sudo apt update
        sudo apt install -y mongodb-mongosh
        mongosh --version

    How to connect to a MongoDB deployment running locally:
        By default MongoDB instances run on the 27017 port.
        If that port is in current use we have to use another.
        Run: mongosh --port 28888   Donn't work for me :/
        But I got connected using the connection string of my cluster :)
    
    Commands while connected with mongosh to my cluster:
        db      will show the name of your database
        use database_name       will switch to that database or create it.
        show collections
        show dbs
        help        will show all commands from mongosh terminal.
        exit        to exit.


Lesson 3: Troubleshooting Connection Errors.

    Type of common errors:
        Network Access errors:
            Check if the IP has access to the cluster.
            Go to Atlas UI and check the Network Access tab.
            There we can add an IP.

        User authentication errors:
            Check if the password is correct. (key sensitive).
            Check if the user exits in Atlas.
            Go to Database Access tab, create a new user and generate a password and sign a role.

        Too many open connections error:
            Atlas clusters can reach its maximum members.
            M0, M2 and M5 clusters have a maximum of 500 open connections.
            Check the current connections.
            Scale cluster to a higher tier.
            Restart application.
            maxPolesize.


Lesson 4: Using the MongoDB Shell.

    Insert and retrive documents:
        insertOne()
        find()

    Write and use JavaScript functions: MongoDB is built on top of nodeJs.
        We can write JS functions exactly js in the mongosh terminal.
            Example: function cube(number) {
                if (typeof number !== 'number') {
                    throw new Error("Input must be a number");
                }
                return number ** 3;
            }
            And press enter.
            Then we can run it like: cube(83)
    
    Load script:
        MongoDB has a load() method that can load JS code.
        Example:
            db = db.getSiblingDB("database_name");
            let result = db.posts.aggregate({
                $sample: { size: 1 },
            });

            print(result.next().body)       print() method is built in MongoDB.

    Switch between databses within a script:
        We can load JS code in mongosh:
            load("randomscript.js")

    Edit commands in editor of choice:
        Use external editor to edit functions within mongosh:
            edit() command to open a function in our editor of choice.
            First we need to configurate our editor with: config.get('editor')
            If not editor is configurated will return null.
            Then do: config.set('editor', 'code')
            Now the editor has been changed.
            To edit a function we can type: edit("function_name")
            And the function will be shown in the editor.
            It opens my editor but the changes aren't made for me :/


Conclusion:
In this unit, you learned how to:

    Define a connection string and how it is used to connect to a MongoDB cluster.
    Locate the connection string for an Atlas cluster.
    Identify the basic components of a standard connection string.
    Install the MongoDB Shell, or mongosh.
    Connect to a local MongoDB instance using mongosh.
    Connect to an Atlas cluster using mongosh.
    Troubleshoot MongoDB Atlas connection errors.
    Retrieve and insert a document using mongosh.
    Write and use a JavaScript function inside a mongosh session.
    Use the db.getSiblingDb() method to change databases within a script.
    Use the load() method to load and run a JavaScript file in mongosh.
    Use an external editor within mongosh.
    
Resources:
    Use the following resources to learn more about connecting to a MongoDB database using the MongoDB Shell:

    Docs: Atlas - Get Connection String.
    Docs: Connection StringsDocs: Install mongosh.
    Docs: Connect to a Deployment.
    MongoDB Shell Options.
    Host.
    Port.
    Username.
    mongodb-js/mongosh (GitHub).
    Docs: Atlas - Troubleshoot Connection Issues.
    Perform CRUD Operations in mongosh.
    Write Scripts.
    db.getSiblingDB().
    load() in mongosh.
    Use an Editor for Commands.