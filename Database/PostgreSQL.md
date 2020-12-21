# PostgreSQL Interview Prep

* What is the process of splitting a large table into smaller pieces called in PostgreSQL?
  * It is called table partitioning.
  
* What is a partitioned table in PostgreSQL?
  * The partitioned table is a logical structure. It is used to split a large table into smaller pieces, which are called partitions.

* What purpose does pgadmin in PostgreSQL serve?
  * The pgadmin in PostgreSQL is a data administration tool. It serves the purpose of retrieving, development, testing, and maintaining databases.

* How can you avoid unnecessary locking of a database?
  * We can use MVCC (Multi-version concurrency control) to avoid unnecessary locking of a database.

* What is PL/Python? 
  * PL/Python is a procedural language to which PostgreSQL provides support.

* Which are the methods PostgreSQL provides to create a new database?
  * Using CREATE DATABASE, an SQL command
  * Using created a command-line executable

* How do you delete the database in PostgreSQL?
  * Using DROP DATABASE, an SQL command
  * Using dropdb a command-line executable
  
* What does a schema contain?
  * A schema contains tables along with data types, views, indexes, operators, sequences, and functions.
  
* What are the different operators in PostgreSQL?
  * The PostgreSQL operators include - Arithmetic operators, Comparison operators, Logical operators, and Bitwise operators.

* What are database callback functions called? What is its purpose?
  * The database callback functions are called PostgreSQL Triggers. When a specified database event occurs, the PostgreSQL Triggers are performed or invoked automatically.

* What indexes used?
  * Indexes are used by the search engine to speed up data retrieval.

* What does a Cluster index do? 
  * Cluster index sorts table data rows based on their key values.

* What are the benefits of specifying data types in columns while creating a table?
  * Some of these benefits include consistency, compactness, validation, and performance.

* What do you need to do to update statistics in PostgreSQL?
  * To update statistics in PostgreSQL, we need to use a special function called a vacuum.

* What is the disadvantage with the DROP TABLE command in deleting complete data from an existing table?
  * Though the DROP TABLE command has the ability to delete complete data from an existing table, the disadvantage with it is - it removes complete table structure from the database. Due to this, we need to re-create a table to store data.
  
* How can you delete complete data from an existing table?
  *We can delete complete data from an existing table using the PostgreSQL TRUNCATE TABLE command.

* What are the different properties of a transaction in PostgreSQL? Which acronym is used to refer to them?
  * The properties of a transaction in PostgreSQL include Atomicity, Consistency, Isolation, and Durability. 
  * These are referred to by the acronym, namely ACID. 

* What purpose does the CTIDs field serve?
  * The CTIDs field identifies the specific physical rows in a table according to their block and offsets positions in that table.

* Which are the commands used to control transactions in PostgreSQL?
  * The commands used to control transactions in PostgreSQL are BEGIN TRANSACTION, COMMIT, and ROLLBACK.

* What are the main differences between SQL and PostgreSQL?
  * PostgreSQL is an advanced version of SQL.  Some of the differences between these two include the following:
  * Unlike SQL, views in PostgreSQL are not updatable.
  * Another difference is whereas SQL provides computed columns; the same cannot be expected from PostgreSQL.
  * Unlike SQL, in PostgreSQL, you don’t need to create a DLL to see the code what it is doing.
  * PostgreSQL supports dynamic actions whereas SQL doesn’t support them.

* How is security ensured in PostgreSQL?
  * PostgreSQL uses SSL connections to encrypt client or server communications so that security will be ensured.

* What is the function of Atomicity property in PostgreSQL?
  * Atomicity property ensures successful completion of all the operations in a work unit.

* What are the advantages of PostgreSQL?
  * Some of the advantages of PostgreSQL are 
  * open-source DBMS, 
  * community support, 
  * ACID compliance, 
  * diverse indexing techniques, 
  * full-text search, 
  * a variety of replication methods, and 
  * diversified extension functions, etc.

* What does Write-Ahead Logging (WAL) do?
  * The Write-Ahead Logging enhances database reliability by logging changes before any changes or updates are made to the database

* What are some of the important data administration tools supported by PostgreSQL?
  * Some of the important data administration tools supported by PostgreSQL are Psql,  Pgadmin, and Phppgadmin.

* How can you store the binary data in PostgreSQL?
  * We can store the binary data in PostgreSQL either by using the bytes or by using the large object feature.

* What is a non-clustered index?
  * In a non-clustered index, the index rows order doesn’t match the order in actual data.

* What is the purpose of table space in PostgreSQL?
  * It is a location in the disk. In this, PostgreSQL stores the data files, which contain indices and tables, etc.

* Are there any disadvantages with  PostgreSQL?
  * Yes. There are a few disadvantages. Some of these include the following:
  * It is slower than MySQL on the performance front.
  * It doesn’t have the support of a good number of open source applications when compared to MySQL.
  * Since it focuses more on compatibility, changes made to improve the speed need more work.

* What does a token representation in a SQL Statement?
  *In a SQL Statement, a token represents an identifier, keyword, quoted identifier, special character symbol, or a constant.