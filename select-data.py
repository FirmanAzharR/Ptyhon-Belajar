import psycopg2

connection = psycopg2.connect(database="pythondb", user='firman', password='alifia', host='127.0.0.1', port= '5432')

getConnection = connection.cursor()

sql = '''SELECT*FROM EMPLOYEE''';
getConnection.execute(sql)
data = getConnection.fetchall()

print('get data success :', data)

connection.commit()
connection.close()