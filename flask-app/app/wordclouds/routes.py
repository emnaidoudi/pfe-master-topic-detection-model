from flask import Blueprint
from flask import jsonify
import json
import pymongo as pm


clouds = Blueprint('word-clouds', __name__)

@clouds.route("/")
def easyrun():
    myclient = pm.MongoClient(host="localhost",
                    port=27017,
                    username="accretioadmin",
                    password="adminaccretio&2017",
                   authSource="admin")

    mydb = myclient["topic_detection"]
    mycol = mydb["word_clouds"]
    mydoc = mycol.find({})
    list_clouds = list(mydoc)
    #list_word_clouds = list_clouds[0]["word-clouds"]
    print(list_clouds)
    return json.dumps(list_clouds)


  
