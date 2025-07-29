# PostrgreSQL, MySQL, SQLServer -> relational databases
# MongoDB, Redis -> No SQL databases

import sqlite3
conn = sqlite3.connect('datafile.db')
cursor = conn.cursor()
print(cursor)

#cursor.execute('create table people (id integer primary key, name text, count integer)')
#cursor.execute("insert into people (name,count) values ('Bob',1)")
#cursor.execute('insert into people (name,count) values (?,?)',("Jill",15))

conn.commit()

# it's more secure to use a ? for each variable and the pass the variables as a tuple parameter to the execute method
# you can also  use variable names prefixed with ":" in the query and pass in a corresponding dictionary with the values to be inserted

#cursor.execute("insert into people (name,count) values (:username,:usercount)",{"username":'Joe',"usercount":10})

# after a table is populated you can query the data by using sql commands, again using either ? for variable binding or name and dictionaries

result = cursor.execute("select * from people")
print(result.fetchall())

result = cursor.execute("select * from people where name like :name", {"name":"Bob"})
print(result.fetchall())


cursor.execute("update people set count=? where name=?",(20,"Jill"))
result = cursor.execute("select * from people")
print(result.fetchall())

# fetchone -> get one row of the result
# fetchmany -> return an arbitrary number of rows
# iterating over a file

result = cursor.execute("select * from people")
for row in result:
  print(row)

cursor.execute("update people set count=? where name=?",(40,'Jill'))
conn.commit()
conn.close()

# common sqlite3 database operations
# create a connection to a database -> conn = sqlite3.connect(filename)
# create a cursor for a connection -> cursor = conn.cursor()
# execute a queary with the cursor -> cursor.execute(query)
# return the results of a query -> cursor.fetchall(), cursor.fetchone(), cursor.fetchmany(num_rows)
# commit a transaction to a database -> conn.commit()
# close a connection -> conn.close()