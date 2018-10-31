import pymongo


class Db:
    def __init__(self):
        # self.client = pymongo.MongoClient('mongodb+srv://ryan:fzIapNOmU9oAu2h6@ri-stgev.mongodb.net/test?retryWrites=true')
        self.client = pymongo.MongoClient()
        self.db = self.client.game
        self.users = self.db.users
        self.scores = self.db.scores

    def save_score(self, score):
        d = {
            'score': score
        }
        self.scores.insert_one(d)

    def read_score(self):
        data = self.scores.find().sort([('score', -1)]) # data 是一個pymongo物件
        for d in data: # 用for loop把物件每筆資料印出來
            return d['score']
          
        return 0

    def sign_up(self, name, id, pwd):
        u = {
            'name': name,
            'id': id,
            'pwd': pwd
        }
        self.users.insert_one(u)
        self.read_users()

    def read_users(self):
        data = self.users.find() # data 是一個pymongo物件
        for user in data: # 用for loop把物件每筆資料印出來
            print(user)
          
        return data

    def search_user(self, id):
        data = self.users.find_one({'id': id}) # data 是一個pymongo物件
        return data

    def sign_in(self, id, pwd):
        user = self.search_user(id)
        if not user:
            print('no user')
            return '查無此帳號'
            
        if pwd != user['pwd']:
            return '密碼錯誤'
            
        return ''

