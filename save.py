import pymongo


class Db:
    def __init__(self):
        # self.client = pymongo.MongoClient('mongodb+srv://ryan:fzIapNOmU9oAu2h6@ri-stgev.mongodb.net/test?retryWrites=true')
        self.client = pymongo.MongoClient()
        self.db = self.client.game

    def save_score(self, score):
        d = {
            'score': score
        }
        self.db.scores.insert_one(d)

    def read_score(self):
        data = self.db.scores.find().sort([('score', -1)]) # data 是一個pymongo物件
        for d in data: # 用for loop把物件每筆資料印出來
            return d['score']
          
        return 0
