from flask_pymongo import PyMongo

import flask
app = flask.Flask(__name__)

#app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://13.233.199.195:27017/demo"
mongo = PyMongo(app)


print(mongo)

@app.route('/mongo', methods=['GET'])
def get_all_docs():
  doc = mongo.db.flask.insert({'location':'apac-blr'})
  return "Inserted"
  

@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.inventory.find({})
    print(user)
    return user
 

if __name__ == "__main__":
    app.run(debug=True)
