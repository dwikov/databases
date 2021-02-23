
# create db
# psql -d template1
import psycopg2
from faker import Faker
# https://stackabuse.com/working-with-postgresql-in-python/
con = psycopg2.connect(database="dwik", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")

print("Database opened successfully")
cur = con.cursor()
cur.execute('''CREATE TABLE CUSTOMER2
       (ID INT PRIMARY KEY     NOT NULL,
       Name           TEXT    NOT NULL,
       Address            TEXT     NOT NULL,
       AGE              INT NOT NULL,
       review        TEXT);''')
print("Table created successfully")
fake = Faker()
import random
for i in range(100000):
    print(i)
    cur.execute("INSERT INTO CUSTOMER2 (ID,Name,Address,Age,review) VALUES ('"+ str(i)+"','"+fake.name()+"','"+fake.address()+"','"+str(random.randint(18,100))+"','"+fake.text()+"')")
    con.commit()
