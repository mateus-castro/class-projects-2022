class ContentConfig:
    def __init__(self, column='', value=''):
        self.contentColumn = column
        self.contentValue = value

    def getColumn(self):
        return self.contentColumn

    def getValue(self):
        return self.contentValue