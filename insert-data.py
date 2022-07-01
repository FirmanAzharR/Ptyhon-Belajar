import psycopg2

connection = psycopg2.connect(database="pythondb", user='firman', password='alifia', host='127.0.0.1', port= '5432')

getConnection = connection.cursor()

sql = '''INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX) VALUES('Firman','Azhar', 25, 'L')''';

getConnection.execute(sql)

print("Data inserted successfully !")

connection.commit()
connection.close()