import time
import schedule
from algorithm_handler import generate_data
from config.config_local import connection

class ProjetoAlgasMain():
    sec=10
    print("POC Projeto Algas starting...")
    print(f"The algorithms will run every {sec} seconds")
    schedule.every(sec).seconds.do(generate_data, connection)

    while True:
        schedule.run_pending()
        time.sleep(1)