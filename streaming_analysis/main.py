import time
import moment
import schedule
from random import randint
from config.config_local import connection
from algorithmHandler import AlgorithmHandler

contentQuery = "GENRE = 'ROMANCE'"
userQuery = "AGE > 20 and AGE < 35"
sec=10
numberOfStreamings = randint(50, 250) # números de usuários assistindo simultâneamente -> vai ser bom pra demonstrar o horário do dia em que as pessoas mais consomem streaming

class ProjetoAlgasMain():
    print("Streaming Analysis starting...")
    print(f"The algorithms will run every {sec} seconds")
    schedule.every(sec).seconds.do(lambda: AlgorithmHandler.generateHistory(contentQuery, userQuery, numberOfStreamings, connection))

    while True:
        schedule.run_pending()
        time.sleep(1)