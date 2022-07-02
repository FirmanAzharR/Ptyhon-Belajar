from flask import Flask
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(database="pythondb", user='firman', password='alifia', host='127.0.0.1', port= '5432')
getConnection = connection.cursor()

@app.route("/")
def hello():
    return 'Hello World !'

@app.route("/get-all-employee")
def getAllEmployee():
    sql = 'SELECT*FROM employee'
    getConnection.execute(sql)
    result = {}
    data = getConnection.fetchall()
    result["x"] = data
    return result


if __name__ == "__main__":
    app.run()