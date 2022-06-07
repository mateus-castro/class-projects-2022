class TweetAnalyzer():
    def __init__(self, bDconnection=''):
        self.connection = bDconnection

    def main(self):
        cursor = self.connection.cursor()

        selectQuery = f"SELECT ID FROM USER WHERE {whereSyntax} LIMIT {numberOfStreamings};"
        print(selectQuery)
        cursor.execute(selectQuery)

        # se o registro praquele filme ainda não tiver sido criado na tabela de análise, criar. se não criar registro
        userQueryResult = cursor.fetchall()
        cursor.close()