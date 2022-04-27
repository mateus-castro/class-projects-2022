import moment
from random import randint

from pytz import HOUR

class AlgorithmUtils():
    def __init__(self, bDconnection=''):
        self.connection = bDconnection

    def fetchContentResult(self, whereSyntax):
        cursor = self.connection.cursor()

        selectQuery = f"SELECT ID FROM CONTENT WHERE {whereSyntax};"
        print(selectQuery)
        cursor.execute(selectQuery)

        contentQueryResult = cursor.fetchall()
        cursor.close()
        return contentQueryResult

    def fetchUserResult(self, whereSyntax, numberOfStreamings=1000):
        cursor = self.connection.cursor()

        selectQuery = f"SELECT ID FROM USER WHERE {whereSyntax} LIMIT {numberOfStreamings};"
        print(selectQuery)
        cursor.execute(selectQuery)

        userQueryResult = cursor.fetchall()
        cursor.close()
        return userQueryResult

    def insertHistory(self, contentIdList, userIdList):
        cursor = self.connection.cursor()
        insertList = self.formatDataToInsert(
            contentIdList, userIdList)
        insertQuery = f"INSERT INTO HISTORY VALUES {insertList};"
        print(insertQuery)
        cursor.execute(insertQuery)
        self.connection.commit()
        print("[DB Connection] Data was inserted successfully")
        cursor.close()

    def formatDataToInsert(self, contentIdList, userIdList):
        formattedList = "" 
        for user in userIdList:
            createTime=moment.date("20/04/2022").replace(hours=randint(0, 10), minutes=randint(0, 59), seconds=randint(0, 59)) # matutino
            # createTime=moment.date("20/04/2022").replace(hours=randint(11, 17), minutes=randint(0. 59), seconds=randint(0, 59)) # vespertino
            # createTime=moment.date("20/04/2022").replace(hours=randint(18, 24), minutes=randint(0. 59), seconds=randint(0, 59)) # noturno
            formattedList += f"(null, {user['ID']}, {contentIdList[randint(0, len(contentIdList)-1)]['ID']}, '{str(randint(0, 100))}', '{str(randint(0, 5))}', '{str(createTime)}'), "

        return formattedList[:-2]