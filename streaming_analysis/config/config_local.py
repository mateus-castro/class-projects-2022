import pymysql.cursors

connection=pymysql.connect(
    user= 'root',
    host= 'localhost',
    password= 'root',
    database= 'streaming',
    cursorclass=pymysql.cursors.DictCursor
    )