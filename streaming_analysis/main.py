import time
import schedule
from models import UserConfig, ContentConfig
from algorithmHandler import AlgorithmHandler
from config.config_local import connection

class ProjetoAlgasMain():
    sec=3
    print("Streaming Analysis starting...")
    print(f"The algorithms will run every {sec} seconds")
    algorithmHandler = AlgorithmHandler()
    user = UserConfig("age", "58")
    content = ContentConfig("genre", "romance")
    schedule.every(sec).seconds.do(algorithmHandler.generateHistory, content, user, connection)

    while True:
        schedule.run_pending()
        time.sleep(1)