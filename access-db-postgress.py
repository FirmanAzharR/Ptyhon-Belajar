import psycopg2

connection = psycopg2.connect(database="test", user='firman', password='alifia', host='127.0.0.1', port= '5432')
getConnection = connection.cursor()

getConnection.execute("select version()")

data = getConnection.fetchone()

print("Connection established to: ",data)

connection.close()