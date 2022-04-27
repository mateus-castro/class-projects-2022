class AlgorithmUtils():
    def __init__(self, connection):
        self.connection = connection

    def fetchContentResult(self, contentColumn, contentValue):
        cursor = self.connection.cursor() # TODO testar se passar o cursor como parâmetro funciona
        cursor.execute(f"SELECT ID FROM CONTENT WHERE {contentColumn} = {contentValue}")
        contentQueryResult = cursor.fetchall()
        cursor.close()
        return contentQueryResult

    def fetchUserResult(self, userColumn, userValue, numberOfStreamings = 1000):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT ID FROM CONTENT WHERE {userColumn} = {userValue} LIMIT {numberOfStreamings}")
        userQueryResult = cursor.fetchall()
        cursor.close()
        return userQueryResult

    def insertHistory(self, contentIdList, userIdList):
        cursor = self.connection.cursor()
        insertList = []
                        # # inserção dos dados no banco
        # with connection.cursor() as cursor:
        #     sql = "INSERT INTO `datas` VALUES (null, %s, %s, %s, %s, %s, %s, %s), (null, %s, %s, %s, %s, %s, %s, %s);"
        #     cursor.execute(sql, (str((dt_fim_while - dt_inicio_while).total_seconds()).replace(".", ","), str(size_while), str(cont_while), "projeto_algas_while", stop, step, str(moment.now()), str((dt_fim_for - dt_inicio_for).total_seconds()).replace(".", ","), str(size_for), str(cont_for), "projeto_algas_for", stop, step, str(moment.now())))
        #     print("[DB Connection] Data was inserted successfully")       
        # connection.commit()
        # cursor.close()
        cursor.execute(f"INSERT INTO HISTORY VALUES {insertList}")


# def size_sum_for(n):
#     acumulador=0
#     for i in range(0, n+1):
#         acumulador += sys.getsizeof(i)
#     return acumulador

# def size_sum_while(n):
#     acumulador=0
#     i=0
#     while (i in range(0, n+1)):
#         acumulador += sys.getsizeof(i)
#         i+=1
#     return acumulador