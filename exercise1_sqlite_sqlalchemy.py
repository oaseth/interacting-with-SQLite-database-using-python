import sqlalchemy as db

engine = db.create_engine("sqlite:///users_sqlalchemy.db")

metadata = db.MetaData()

connection = engine.connect()

users = db.Table("Table", metadata,
                 db.Column("user_id", db.Integer, primary_key=True),
                 db.Column("first_name", db.Text),
                 db.Column("last_name", db.Text),
                 db.Column("email_address", db.Text),
                 )

metadata.create_all(engine)

insertion_query = users.insert().values([
    {"first_name": "Matthew", "last_name": "Thomas",
        "email_address": "mthomas@team.com"},
    {"first_name": "Andrew",  "last_name": "Stift",
        "email_address": "astift@team.com"},
    {"first_name": "Dave", "last_name": "Brown",
        "email_address": "davebr@team.com"},
    {"first_name": "Sandra", "last_name": "Paddy",
        "email_address": "sanddy@team.com"},
    {"first_name": "Christabel", "last_name": "Anderson",
        "email_address": "canderson@team.com"}
])

connection.execute(insertion_query)

selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
