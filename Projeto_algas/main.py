from datetime import datetime
import moment
from config.config_local import connection
import utils
from random import randint

start = 0
stop = randint(0, 10000)
step = stop/randint(stop*.05, stop*.25)

# execução de estrutura 'while'
cont_1 = 0
size_1 = 0
dt_inicio_1 = datetime.now()
for valor in range(start, stop, step):
    size_1 += utils.size_sum_while(valor)
    cont_1 += 1
dt_fim_1 = datetime.now()

# execução de estrutura 'for'
cont_2 = 0
size_2 = 0
dt_inicio_2 = datetime.now()
for valor in range(start, stop, step):
    size_2 += utils.size_sum_for(valor)
    cont_2 += 1
dt_fim_2 = datetime.now()

with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `datas` VALUES (null, %s, %s, %s, %s, %s), (null, %s, %s, %s, %s, %s);"
        cursor.execute(sql, (str((dt_fim_1 - dt_inicio_1).total_seconds()).replace(".", ","), str(size_1), str(cont_1), "projeto_algas_while", str(moment.now()), str((dt_fim_2 - dt_inicio_2).total_seconds()).replace(".", ","), str(size_2), str(cont_2), "projeto_algas_for", str(moment.now())))
    connection.commit()


print('sucesso :>')