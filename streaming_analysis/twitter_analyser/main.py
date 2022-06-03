import os
import json
import time
import moment
import schedule
import datetime
from dotenv import load_dotenv
from random import randint
from config.config_local import connection
from algorithmHandler import AlgorithmHandler
from services.tweet_searcher import TweetSearcher

class Main():
    load_dotenv()
    # contentQuery = "GENRE = 'ROMANCE'"
    # userQuery = "AGE > 20 and AGE < 35"
    # numberOfStreamings = randint(50, 250) # números de usuários assistindo simultâneamente -> vai ser bom pra demonstrar o horário do dia em que as pessoas mais consomem streaming

    # schedule.every(sec).seconds.do(lambda: AlgorithmHandler.generateHistory(contentQuery, userQuery, numberOfStreamings, connection))

    sec=os.getenv('SCHEDULING_SECONDS_INTERVAL')

    print(f'{datetime.datetime.now()} - [Main] Tweet Preprocessed files generating is starting...')
    print(f'The algorithms will run every {sec} seconds')
    schedule.every(sec).seconds.do(lambda: TweetSearcher('#netflix OR #netflixbr', '100').main())


    while True:
        schedule.run_pending()
        time.sleep(1)