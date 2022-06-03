import moment
from utils.algorithmUtils import AlgorithmUtils

class AlgorithmHandler():
    def generateHistory(contentQuery, userQuery, numberOfStreamings, connection):
        algorithmUtils = AlgorithmUtils(connection)

        contentList = algorithmUtils.fetchContentResult(contentQuery)
        userList = algorithmUtils.fetchUserResult(userQuery, numberOfStreamings)

        algorithmUtils.insertHistory(contentList, userList)

