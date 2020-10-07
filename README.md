# flask-mongo-db

# commands to run flask app

`python app.py`

# Output

<flask_pymongo.PyMongo object at 0x7ff2842f7890>
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
<flask_pymongo.PyMongo object at 0x7fb213415190>
 * Debugger is active!
 * Debugger PIN: 297-313-204
/Users/gaurav/Downloads/flask-mongo/app.py:15: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
  doc = mongo.db.flask.insert({'location':'apac-blr'})
127.0.0.1 - - [07/Oct/2020 12:53:34] "GET /mongo HTTP/1.1" 200 -


# verify DB Details in MongoDBon AWS Ubuntu Instance

ubuntu@ip-172-31-2-241:~$ mongo
MongoDB shell version v3.6.8
connecting to: mongodb://127.0.0.1:27017
Implicit session: session { "id" : UUID("91e72e08-e0f0-468b-b582-efb0a2e5221e") }
MongoDB server version: 3.6.8
Server has startup warnings: 
2020-10-07T06:35:34.670+0000 I STORAGE  [initandlisten] 
2020-10-07T06:35:34.670+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2020-10-07T06:35:34.670+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2020-10-07T06:35:38.986+0000 I CONTROL  [initandlisten] 
2020-10-07T06:35:38.987+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2020-10-07T06:35:38.987+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2020-10-07T06:35:38.987+0000 I CONTROL  [initandlisten] 
> show dbs
admin   0.000GB
config  0.000GB
demo    0.000GB
local   0.000GB
> show collections
> 
> show dbs
admin   0.000GB
config  0.000GB
demo    0.000GB
local   0.000GB
> 
> 
> show collections
> use demo
switched to db demo
> show collections
abcd
flask
inventory
user
> db.flask.find()
{ "_id" : ObjectId("5f7d6cf6099bfc45bd1c7ee7"), "location" : "apac-blr" }
> 
