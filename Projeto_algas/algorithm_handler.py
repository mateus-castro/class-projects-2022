from datetime import datetime
import moment
import math
from algorithm_utils import size_sum_for, size_sum_while
from random import randint

def generate_data(connection):
    # inicialização dos parâmetros dos algoritmos:
    # os parâmetros são inicializados com valores aleatórios e/ou calculados
    start = 0
    stop = randint(0, 10000)
    step = randint(int(math.floor(stop*.05)), int(math.floor(stop*.25)))
    
    print("[Generating Data] Start: %d | Stop: %d | Step: %d"  % (start, stop, step))

    # execução do algoritmo com estrutura 'while'
    cont_while = 0
    size_while = 0
    dt_inicio_while = datetime.now()
    for valor in range(start, stop, step):
        size_while += size_sum_while(valor)
        cont_while += 1
    dt_fim_while = datetime.now()

    # execução do algoritmo com estrutura 'for'
    cont_for = 0
    size_for = 0
    dt_inicio_for = datetime.now()
    for valor in range(start, stop, step):
        size_for += size_sum_for(valor)
        cont_for += 1
    dt_fim_for = datetime.now()

    # inserção dos dados no banco
    with connection.cursor() as cursor:
        sql = "INSERT INTO `datas` VALUES (null, %s, %s, %s, %s, %s, %s, %s), (null, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(sql, (str((dt_fim_while - dt_inicio_while).total_seconds()).replace(".", ","), str(size_while), str(cont_while), "projeto_algas_while", stop, step, str(moment.now()), str((dt_fim_for - dt_inicio_for).total_seconds()).replace(".", ","), str(size_for), str(cont_for), "projeto_algas_for", stop, step, str(moment.now())))
        print("[DB Connection] Data was inserted successfully")       
    connection.commit()
    cursor.close()