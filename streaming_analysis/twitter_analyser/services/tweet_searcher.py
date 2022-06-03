import requests
import os
import json
import datetime
from dotenv import load_dotenv

class TweetSearcher():
    def __init__(self, query_parameters = '#netflix OR #netflixbr', max_results = '100'):
        load_dotenv()
        self.token = os.getenv('TOKEN')
        self.search_url = os.getenv('SEARCH_URL')

        # query: parametro pra ver 
        self.query_params = {'query': query_parameters, 'tweet.fields': 'author_id,created_at,geo,in_reply_to_user_id,lang,possibly_sensitive,source', 'max_results': max_results}

    def bearer_oauth(self, r):
        print(self.token)
        r.headers["Authorization"] = f"Bearer {self.token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        r.headers["Content-Type"] = f"application/x-www-form-urlencoded;charset=UTF-8"
        return r

    def connect_to_endpoint(self, url, params):
        response = requests.get(url, auth=self.bearer_oauth, params=params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def main(self):
        json_response = self.connect_to_endpoint(self.search_url, self.query_params)
            
        tweets_reacheds = len(json_response.get('data'))
        file_name = datetime.datetime.now().timestamp()
        if (tweets_reacheds > 0):
            print(f'{tweets_reacheds} tweets foram encontrados')
        f = open(f'../archives/{file_name}_PREPROCESSED_TWEETS.json', 'w')
        f.write(str(json.dumps(json_response.get('data'), indent=20, sort_keys=True)))
        f.close