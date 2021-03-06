import requests
import os
import json
import boto3
from log_custom import bcolors
from datetime import datetime
from dotenv import load_dotenv

class TweetSearcher():
    def __init__(self, query_parameters = '', max_results = ''):
        load_dotenv()
        self.token = os.getenv('TOKEN')
        self.search_url = os.getenv('SEARCH_URL')
        self.film = query_parameters
        self.query_params = {'query': query_parameters, 'tweet.fields': 'author_id,created_at,geo,in_reply_to_user_id,lang,possibly_sensitive,source', 'max_results': max_results}

    def bearer_oauth(self, r):
        r.headers["Authorization"] = f"Bearer {self.token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        r.headers["Content-Type"] = f"application/x-www-form-urlencoded;charset=UTF-8"
        return r

    def connect_to_endpoint(self, url, params):
        print(bcolors.CYAN + f'{str(datetime.now())[:-7]} - [Twitter API]' + bcolors.ENDC + ' Request:', { 'url':url, 'params':params })
        response = requests.get(url, auth=self.bearer_oauth, params=params)
        print(bcolors.CYAN + f'{str(datetime.now())[:-7]} - [Twitter API]' + bcolors.ENDC + ' Response:', response)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def main(self):
        json_response = self.connect_to_endpoint(self.search_url, self.query_params)
            
        for tweet in json_response.get('data'):
            tweet.update({ 'content': self.film })
            
        tweets_reacheds = len(json_response.get('data'))
        file_name = f'{datetime.now().timestamp()}_PREPROCESSED_TWEETS.json'
        if (tweets_reacheds > 0):
            print(bcolors.CYAN + f'{str(datetime.now())[:-7]} - [Twitter API]' + bcolors.ENDC + bcolors.PURPLE + bcolors.BOLD + f' {tweets_reacheds} tweets' + bcolors.ENDC + ' foram encontrados e salvos no arquivo ' + bcolors.PURPLE + bcolors.BOLD + file_name + bcolors.ENDC)

            s3 = boto3.resource('s3')
            s3.Bucket('mateus-streaming-analysis-sptech-bucket-tweets').put_object(Key=file_name, Body=str(json.dumps(json_response.get('data'), indent=2, sort_keys=True)))

        else:
            print(bcolors.CYAN + f'{str(datetime.now())[:-7]} - [Twitter API] Nenhum tweet foi encontrado.' + bcolors.ENDC)
