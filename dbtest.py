import pymongo
from datetime import datetime

# 對 mongo資料庫發出請求
client = pymongo.MongoClient("mongodb+srv://user:0000@cluster0.ebqhayk.mongodb.net/?retryWrites=true&w=majority")


'''
資料庫裡面分層
Database -> Collection (類似table)
'''

# 切換 資料庫
# db = client."自訂資料庫名稱"
db = client.hcw_test_db

# 切換 收藏集
# collection = db."自訂資料庫名稱"
collection = db.hcw_test_collection


#!=========================================以下維操作
# 範例資料
dic = {
  'userid':'2wqlk;ek;lkf;s',
  'username':'banana',
  'note':'test3'
}

collection.insert_one(dic)
collection.delete_one({'note':'test2'})
print('OK')