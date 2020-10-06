from flask_pymongo import PyMongo

import flask
app = flask.Flask(__name__)

#app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://15.207.109.209:27017/demo"
mongo = PyMongo(app)

print(mongo)



@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.inventory.find({})
    print(user)
    return user
 


app.run()
