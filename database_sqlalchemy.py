import sqlalchemy as db

# Creating an engine. It allows several connections to a database
engine = db.create_engine('sqlite:///movies.db')

# Creating a connection to the database. Proxy to the 'connect' function in the
# Python Api
connection = engine.connect()

metadata = db.MetaData()

# Creating or Loading an existing table in the database
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# The query statement
query = db.select([movies])

# The result proxy, synonymous to the 'cursor' function in the Python API
result_proxy = connection.execute(query)
# The actual result of the query in the form of a List object
result_set = result_proxy.fetchall()

# Accessing the objects in the result list
print(result_set[0])
print(result_set[:2])

query = db.select([movies]).where(movies.columns.Director == 'Martin Scorsese')

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

print(result_set[0])

query = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", Year=1960)

connection.execute(query)

query = db.select([movies])

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

print(result_set)
