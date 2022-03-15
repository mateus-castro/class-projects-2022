import time
import schedule
from algorithm_handler import generate_data
from config.config_local import connection

class ProjetoAlgasMain():
    print("POC Projeto Algas starting...")
    schedule.every(10).seconds.do(generate_data, connection)

    while True:
        schedule.run_pending()
        time.sleep(1)