import os
import boto3
import json
from dotenv import load_dotenv

class TweetAnalyzer():
    def __init__(self, bDconnection=''):
        self.connection = bDconnection
        self.s3 = boto3.resource('s3')

    def main(self):
        load_dotenv()
        tweets_bucket = self.s3.Bucket(os.getenv('TWEETS_BUCKET_NAME'))

        for object in self.tweets_bucket.objects.all():
            obj = self.s3.Object(os.getenv('TWEETS_BUCKET_NAME'), object.key)
            tweets_list = json.loads(obj.Body.read())

        cursor = self.connection.cursor()

        selectQuery = f"SELECT ID FROM USER WHERE bla LIMIT blabla;"
        print(selectQuery)
        cursor.execute(selectQuery)

        # se o registro praquele filme ainda não tiver sido criado na tabela de análise, criar. se não criar registro
        userQueryResult = cursor.fetchall()
        cursor.close()
