import os
import json
import time
import moment
import schedule
from datetime import datetime
from dotenv import load_dotenv
from log_custom import bcolors
from services.tweet_searcher import TweetSearcher
from utils.tweet_analyzer import TweetAnalyzer

load_dotenv()
search_interval=os.getenv('TWEETS_SEARCH_MINUTES_INTERVAL')
analysis_interval=os.getenv('TWEETS_ANALYSIS_MINUTES_INTERVAL')
query=os.getenv('QUERY')
max_results=os.getenv('MAX_RESULTS')

class Main():
    print(bcolors.GREEN + f'{str(datetime.now())[:-7]} - [Main]' + bcolors.ENDC + ' Tweet Searcher will run' + bcolors.GREEN + bcolors.BOLD + f' every {search_interval} minutes' + bcolors.ENDC)
    print(bcolors.GREEN + f'{str(datetime.now())[:-7]} - [Main]' + bcolors.ENDC + ' Tweet Analyzer will run' + bcolors.GREEN + bcolors.BOLD + f' every {analysis_interval} minutes' + bcolors.ENDC)

    schedule.every(int(search_interval)).minutes.do(lambda: TweetSearcher(query, max_results).main())
    schedule.every(int(analysis_interval)).minutes.do(lambda: TweetAnalyzer.main())

    while True:
        schedule.run_pending()
        time.sleep(1)