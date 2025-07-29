# to use MySQL, PostrgreSQL and otherrelational databasases u need to have server tha client 
# connect on local machine or diffrent machine
# making database handling easier with an object relational mapper
# DjangoORM, SQLAlchemy
# SQL Alchemy
# najpier trzeba zainstalować 'pip install sqlalchemy'
# import components you need to connect to the database and map the table to python objects
from sqlalchemy import(create_engine, select, MetaData, Table, Column, Integer, String)
from sqlalchemy.orm import sessionmaker

# connecting to a database:
dbPath ='datafile2.db'
engine = create_engine('sqlite:///%s' % dbPath) # Creates engine object
metadata = MetaData()
people = Table('people', metadata, # Create 'people' table object
               Column('id',Integer,primary_key=True),
               Column('name',String),
               Column('count',Integer),
               )

Session = sessionmaker(bind=engine) # Create a session
session = Session()
metadata.create_all(engine) # Creates table in database

# inserting some records in SQLAlchemy - many options

#people_ins = people.insert().values(name='Bob',count=1)
#print(str(people_ins))

#session.execute(people_ins)
#session.commit()

# kilka rekordów

#session.execute(people_ins, [
#    {'name':'Jill','count':15},
#    {'name':'Joe','count':10}
#])
#session.commit()
#result = session.execute(select(people))
#for row in result:
#  print(row)

# we can do select operations a bit more directly by instead using the select() method with a, where()
# method to find a particular record

#result = session.execute(select(people).where(people.c.name =='Jill'))
#for row in result:
#  print(row)
# name column -> 'Jill'
# people.c.name -> 'c' name is column, table 'people'

# update() -> for changing values in database
#result = session.execute(people.update().values(count=20).where(people.c.name == "Jill"))
#session.commit()

#result = session.execute(select(people).where(people.c.name == 'Jill'))
#for row in result:
#  print(row)

# MAKING TABLE OBJECTS TO CLASSES
# MAKING A CLASS PEOPLE

from sqlalchemy.orm import declarative_base
Base = declarative_base()
class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)

results = session.query(People).filter_by(name='Jill')
for person in results:
    print(person.id, person.name, person.count)

# inserts can be done just by creating and instance of the mapped class and adding it to the session

new_person = People(name='Jane',count=5)
session.add(new_person)
session.commit()
results = session.query(People).all()
for person in results:
  print(person.id,person.name,person.count)

# updating -> retrieving the record u want update, change the values on the mapped instance and put updated record to
# the session to be written back to the database

jill = session.query(People).filter_by(name='Jill').first()
print(jill.name)
jill.count = 22
session.add(jill)
session.commit()
results = session.query(People).all()
for person in results:
  print(person.id,person.name,person.count)

# deleting is similar to updating: you fetch the record to be deleted and then use the sessions, delete() method to delete it

jane = session.query(People).filter_by(name='Jane').first()
session.delete(jane)
session.commit()
jane = session.query(People).filter_by(name="Jane").first()
print(jane)