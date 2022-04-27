import pymysql.cursors

connection=pymysql.connect(
    user= 'aluno',
    host= 'localhost',
    password= 'sptech',
    database= 'streaming',
    cursorclass=pymysql.cursors.DictCursor
    )