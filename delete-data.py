import psycopg2

connection = psycopg2.connect(database="pythondb", user='firman', password='alifia', host='127.0.0.1', port= '5432')

getConnection = connection.cursor()

sql = '''DELETE FROM employee where age=23''';

getConnection.execute(sql)

print("delete data successfully !")

connection.commit()
connection.close()