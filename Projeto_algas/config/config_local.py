import pymysql.cursors

connection=pymysql.connect(
    user= 'aluno',
    host= 'localhost',
    password= 'sptech',
    database= 'test_script',
    cursorclass=pymysql.cursors.DictCursor
    )