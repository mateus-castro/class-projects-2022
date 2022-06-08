import os
import boto3
import json
from words_lists.negative import negative_words_list
from words_lists.positive import positive_words_list
from words_lists.generic import generic_words_list
from dotenv import load_dotenv

class TweetAnalyzer():
    def __init__(self, bDconnection=''):
        self.connection = bDconnection
        self.s3 = boto3.resource('s3')
        self.common_words_limit = 5

    def get_common_impressions(self, words_list):
        most_common_words = []
        less_generic_impressions = []

        for word in words_list:
            if word.lower() not in generic_words_list:
                less_generic_impressions += word

        count = 0

        while count < self.common_words_limit:
            common_word = max(set(less_generic_impressions), key=less_generic_impressions.count)
            most_common_words += common_word
            less_generic_impressions = list(filter((common_word).__ne__, less_generic_impressions))
            count += 1

        return ','.join(most_common_words)

    def main(self):
        load_dotenv()
        tweets_bucket = self.s3.Bucket(os.getenv('TWEETS_BUCKET_NAME'))

        for object in self.tweets_bucket.objects.all():
            words_list = []
            negative_impressions = 0
            positive_impressions = 0
            neutral_impressions = 0

            # cria uma lista de palavras com todos os tweets
            obj = self.s3.Object(os.getenv('TWEETS_BUCKET_NAME'), object.key)
            tweets_list = json.loads(obj.get()['Body'].read())
            content = tweets_list[0]['content']

            for tweet in tweets_list:
                if (tweet['lang'] == 'en'):
                    text = tweet['text'].replace(',', '').replace('.', '').replace('?', '')
                    words_list += text.split()
            

            # atribui os pontos de impressão baseados na lista de palavras
            for word in words_list:
                if (word.lower() in positive_words_list):
                    positive_impressions += 1

                elif (word.lower() in negative_words_list):
                    negative_impressions += 1

                elif (word.lower().replace('!', '') in positive_words_list):
                    # caso as palavras estejam seguidas de um ponto de exclamação, é considerado pontos a mais de impressão
                    positive_impressions += 2

                elif (word.lower().replace('!', '') in negative_words_list):
                    # tanto para palavras positivas quanto negativas
                    negative_impressions += 2

                else:
                    # caso não caia em nenhuma dos casos, é atribuido ponto para palavra neutra, como: preposições, substantivos e palavras genéricas
                    neutral_impressions +=1

            common_impressions = self.get_common_impressions(words_list)
            cursor = self.connection.cursor()

            query_values = f'(null, {content}, {common_impressions}, {positive_impressions}, {negative_impressions}, {neutral_impressions})'
            insert_query = f'INSERT INTO RATE_ANALYSIS (ID, CONTENT, IMPRESSIONS, POSITIVE, NEGATIVE, NEUTRAL) VALUES {query_values};'
            print(insert_query)
            cursor.execute(insert_query)
            self.connection.commit()
            print("[DB Connection] Data was inserted successfully")
            cursor.close()
