import psycopg2

connection = psycopg2.connect(database="test", user='firman', password='alifia', host='127.0.0.1', port= '5432')
connection.autocommit = True

getConnection = connection.cursor()

#Preparing query to create a database
sql = '''CREATE database pythonDb''';
#Creating a database
getConnection.execute(sql)
print("Database created successfully")
#Closing the connection
getConnection.close()