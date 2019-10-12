import pymysql.cursors


# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='miniblog',
    charset='utf8mb4',
    port = 3306,
    cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

cursor.execute("SELECT * FROM User")
result = cursor.fetchall()

print(result)

connection.close()
