import psycopg2

connection = psycopg2.connect(database="pythondb", user='firman', password='alifia', host='127.0.0.1', port= '5432')

getConnection = connection.cursor()

sql = '''UPDATE EMPLOYEE SET first_name = 'Firman Azhar', last_name='Riyadi' WHERE age = 25''';
getConnection.execute(sql)

print('update data success')

connection.commit()
connection.close()