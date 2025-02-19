from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

mongo_host = 'login-flask-db-svc.default.svc.cluster.local'
mongo_port = 27017
mongo_username = 'mis-admin'
mongo_password = 'mis_2023'
auth_db = 'mis'

client = MongoClient(mongo_host, username=mongo_username, password=mongo_password, authsource=auth_db)

@app.route("/show_databases", methods=['GET'])
def get_databases():

    dbs = ", ".join(client.list_database_names())
    
    return render_template('index.html', database_names=dbs)

@app.route("/")
def hello():
    return render_template('index.html', database_names="Not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)