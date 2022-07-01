import psycopg2

connection = psycopg2.connect(database="pythondb", user='firman', password='alifia', host='127.0.0.1', port= '5432')
getConnection = connection.cursor()
getConnection.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = '''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1)
)'''

getConnection.execute(sql)

print("Create table successfully !")
connection.commit()
connection.close()