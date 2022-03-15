import pymysql.cursors

connection=pymysql.connect(
    user= 'root',
    host= 'localhost',
    password= 'root',
    database= 'test_script',
    cursorclass=pymysql.cursors.DictCursor
    )