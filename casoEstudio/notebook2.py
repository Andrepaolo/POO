import datetime
last_id = 0
class Note:
    
    def __init__(self, memo, tags=""):

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):

        return filter in self.memo or filter in self.tags

