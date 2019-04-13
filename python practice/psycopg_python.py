import psycopg2
import time

#Number of rows to add in each batch
n = 10000

#Generate single insert into our query
single_query = """INSERT INTO post(user_id,post_text) VALUES (1, 'Single Query');"""

#Generate single Big Batch query
big_query = "INSERT INTO post(user_id, post_text) VALUES"
for i in range(n):
	big_query += "(1, 'Single Big Batch Queries'),"
big_query = big_query.strip(',') + ';' # Replace Trailing ',' with ';'

#Database Connection to PostgreSQL
# password = open('password.txt', 'r').read()
# conn = psycopg2.connect("dbname=my_db user=postgres password={}".format(password))
conn = psycopg2.connect(
	database = "my_db",
	user = "postgres",
	password = "ramesh",
	host = "localhost",
	port = "5432",
	
)
cur = conn.cursor()

#Time of n individual queries
start_time = time.time()
for i in range(n):
	cur.execute(single_query)
conn.commit
stop_time = time.time()
print("{} individual queries took {} seconds".format(n, stop_time - start_time))


#Time of big Single batch query
start_time = time.time()
cur.execute(big_query)
conn.commit()
stop_time = time.time()
print("The query time of single query with {} rows took {} seconds".format(n,stop_time - start_time))

#close both cursor and connection  to database
cur.close()
conn.close()