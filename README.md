# Using SQL vs NoSQL Databases
The increasing need for storing complex data structures led to the birth of NoSQL databases. This new kind of database system allows developers to store heterogeneous and structureless data efficiently.
In recent years, SQL and NoSQL databases have even begun to merge.
For example, database systems, such as PostgreSQL, MySQL, and Microsoft SQL Server now support storing and querying JSON data.

Read More -> https://realpython.com/introduction-to-mongodb-and-python/

# MongoDB
MongoDB
 . uses collections of documents instead of tables of rows to organize and store data.
 . stores data in flexible JSON-like documents.
 . is a distributed database, so high availability, horizontal scaling, and geographic distribution are built into the system. 
 . provides a powerful query language that supports ad hoc queries, indexing, aggregation, geospatial search, text search


# Installing and Running MongoDB
	instalacion tutoriales -> https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials
	download -> https://www.mongodb.com/try/download/community
	
	pc I7 c:\usuarios\usuario\mongoDB
		compass-1.26.0
			cliente GUI
		
		comunity-4.2.13
			servidor (modo manual)
			esta en el path
			
			view README
			run server:
				mongod
				
			run mongo shell:
				mongo
				Is an interactive JavaScript interface to MongoDB.
				Connects to local server provided by the mongod process at mongod://127.0.0.1:27017.
				
	
	Say you’re planning to use MongoDB to store your tutorials and articles. In that case, you can following command:
	
	> use rptutorials
	> switched to db rptutorials
	
	> show dbs
	> db
	
	> db.tutorial
	
# Agregar datos
	MongoDB stores documents in a format called Binary JSON (BSON).
	MongoDB’s documents are composed of field-and-value pairs and have the following structure:
	
	{
		field1 → value1,
		field2 → value2,
		...
		fieldN → valueN
	}
	
	The value of a field can be any BSON data type: https://docs.mongodb.com/manual/reference/bson-types/

	jSonA = {}
	jSonB = {}
	
	db.tutorial.insertOne(jSonaA)
	db.tutorial.insertMany([jSonA, jSonB])
	
	
	db.tutorial.find()
	db.tutorial.find({author: "Joanna"})

# Using MongoDB With Python and PyMongo
	pip install https://github.com/mongodb/mongo-python-driver
	doc's https://pymongo.readthedocs.io/en/stable/index.html
	
	pip install pymongo
	


# MongoEngine
	While PyMongo is a great and powerful Python driver for interfacing with MongoDB, it’s probably a bit too low-level for many of your projects.
	One library that provides a higher abstraction on top of PyMongo is MongoEngine.
	MongoEngine is an object-document mapper (ODM)
	
	pip install mongoengine
	
	







