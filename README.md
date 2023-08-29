# Using SQL vs NoSQL Databases
The increasing need for storing complex data structures led to the birth of NoSQL databases. This new kind of database system allows developers to store heterogeneous and structureless data efficiently.
In recent years, SQL and NoSQL databases have even begun to merge.
For example, database systems, such as PostgreSQL, MySQL, and Microsoft SQL Server now support storing and querying JSON data.

Read More -> https://realpython.com/introduction-to-mongodb-and-python/

# MongoDB
MongoDB
- uses collections of documents instead of tables of rows to organize and store data.
- stores data in flexible JSON-like documents.
- is a distributed database, so high availability, horizontal scaling, and geographic distribution are built into the system. 
- provides a powerful query language that supports ad hoc queries, indexing, aggregation, geospatial search, text search


# Installing and Running MongoDB

Podemos utilizar esta database como un servicio cloud desde su version [Atlas](https://www.mongodb.com/es/atlas) o descargando la [version comunidad](https://www.mongodb.com/try/download/community) donde la podemos instalar de manera predeterminada como servicio. Tambien trae al cliente GUI Compass.

El servidor queda corriendo en mongod://127.0.0.1:27017

Instalacion [tutorial](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials
)

# Configuracion de MongoDB

Luego de que mongo quedo instalado como un servicio podemos configurarlo desde su [archivo de configuracion](https://www.mongodb.com/docs/manual/reference/configuration-options/#std-label-configuration-options) ubicado en <install directory>\bin\mongod.cfg.

## Configuracion IP.

Por cuestionos de seguridad, la instalacion por defecto restringe para que mongo quede publicado unicamente en localhost. Claro que esto lo podemos cambiar haciendo un nuevo bind

```
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1, local IP
```

y no olvidar abrir el puerto 27017 para las conexiones entrantes.
	


	
Say you’re planning to use MongoDB to store your tutorials and articles. In that case, you can following command:
	
use rptutorials
switched to db rptutorials
	
show dbs
db

db.tutorial
	

# Agregar datos

MongoDB stores documents in a format called Binary JSON (BSON). MongoDB’s documents are composed of field-and-value pairs and have the following structure:
	
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



# Python and Mongo

# Using MongoDB with PyMongo

La [instalacion](https://pypi.org/project/pymongo/) es muy simple: pip install pymongo
	
La [documentacion](https://pymongo.readthedocs.io/en/stable/) actual de PyMongo

La [pagina](https://github.com/mongodb/mongo-python-driver) del proyecto esta en github

Este es un [ejemplo](https://pymongo.readthedocs.io/en/stable/tutorial.html) simple donde asumimos que todo estar corriendo en localhost


# Dicen por ahi q pymongo es muy duro, otras librerias hacen mas facil todo, veamos

