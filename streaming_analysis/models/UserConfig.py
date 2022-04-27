class UserConfig:
    def __init__(self, column='', value=''):
        self.userColumn = column
        self.userValue = value

    def getColumn(self):
        return self.userColumn

    def getValue(self):
        return self.userValue