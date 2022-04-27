from datetime import datetime
import moment
import math
from algorithmUtils import AlgorithmUtils
from random import randint

class AlgorithmHandler():
    # TODO terminar o select e fazer as primeiras amostragens de dados
    def generateHistory(content, user, connection):
        numberOfStreamings = randint(50, 900) # números de usuários assistindo simultâneamente -> vai ser bom pra demonstrar o horário do dia em que as pessoas mais consomem streaming
        algorithmUtils = AlgorithmUtils(connection)

        contentList = algorithmUtils.fetchContentResult(content.getColumn(), content.getValue())
        userList = algorithmUtils.fetchUserResult(user.getColumn(), user.getValue(), numberOfStreamings)

        algorithmUtils.insertHistory(contentList, userList)

