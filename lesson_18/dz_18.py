import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = 'root',
    password = "16176285",
    database = "pds"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE my_first_db")


mydb = mysql.connector.connect(
    host="localhost",
    user = 'root',
    password = "16176285",
    database = "my_first_db"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE student (id INT, "
#                  "name VARCHAR(255))")

# mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, "
#                  "name VARCHAR(255), salary INT(6))")

# mycursor.execute("ALTER TABLE student ADD PRIMARY KEY (id)")


# sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
# val = [("01", "John")]
# mycursor.executemany(sql, val)

# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


mycursor.execute("SELECT * FROM student")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
# val = [("01", "John", "10000")]
# mycursor.executemany(sql, val)
# mydb.commit()


mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

