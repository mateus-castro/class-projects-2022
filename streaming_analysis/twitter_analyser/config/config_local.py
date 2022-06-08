import pymysql.cursors

connection=pymysql.connect(
    user= 'root',
    host= 'localhost',
    password= 'temp123',
    database= 'streaming',
    cursorclass=pymysql.cursors.DictCursor
    )
