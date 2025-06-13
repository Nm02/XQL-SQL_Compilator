# About this proyect
This project is a mini-compiler that translates an imaginary language named XQL to the database language SQL.
This project was made for the subject "Compilers" at the Catholic University of Salta (UCASAL).


# XQL
xql is a imaginary programming language.
The language especifications are:

* The program starts with the reserved word INICIO and ends with FIN.
* Each instruction or variable declaration line ends with the character "."
* Only the following data types are allowed: NUMBER, STRING, TIMEDATE.
* Selection statements are aimed at retrieving data from a table in the database. The keyword SELECT, which initiates these statements, indicates the selection operation, followed by a list of fields and the data source, which is preceded by the word FROM. An optional WHERE clause allows filtering the results based on certain conditions, and the statement ends with APPLIES.
* Table declaration statements are aimed at creating new tables. They start with DESIGN TABLE followed by the table name, then WITH, and in parentheses the list of fields separated by commas. Each field and its corresponding data type are separated by a hyphen.
* Update statements in XQL are designed to modify existing records in a table. These statements are structured with the initial keyword MODIFY, which indicates the update operation, followed by the table name, FIELD, and a list of fields with the new values to be assigned. "TO" is used as the symbol for assigning a new value. Updates are applied only to records that meet a condition specified by IF.
* Deletion statements allow records to be deleted from a table in the database. These statements begin with DROP TABLE, which indicates the delete operation, followed by the name of the table.
* The conditional part of selection and update operations in XQL must contain typical relational expressions.
* Line comments start with /* and can be written anywhere in the program.



