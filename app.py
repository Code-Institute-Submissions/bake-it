import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'bake-it'
app.config["MONGO_URI"] = os.getenv('MONGO_URI','mongodb://localhost')

mongo = PyMongo(app)
 
@app.route("/")
@app.route("/home")
def home():
  if 'username' in session:
        return 'You are logged in as ' + session['username']
  return render_template("index.html")

@app.route("/log_in", methods=['POST', 'GET'])
def log_in():
  members = mongo.db.members
  login_member = members.find_one({'username' : request.form['username']})
  if login_member:
    if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_member['password'].encode('utf-8')) == login_member['password'].encode('utf-8'):
      session['username'] = request.form['username']
    return redirect(url_for('my_recipes', username =session['username'])) 

  return 'Invalid username/password combination'


@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():

  if request.method == 'POST':
        members = mongo.db.members
        existing_member = members.find_one({'username' : request.form['username']})

        if existing_member is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            hashpass = str(hashpass, encoding='utf-8', errors='strict')
            members.insert({'username' : request.form['username'], 'password' : hashpass, 'member_type' :'admin'})
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        
        return 'That username already exists!' 
  return render_template("sign_up.html")

@app.route("/my_recipes/<username>")
def my_recipes(username):
    return render_template("my_recipes.html", cat_list = list(mongo.db.recipe_category.find()), recipes=mongo.db.recipes.find())

@app.route("/get_recipes")
def get_recipes():
    return render_template("all_recipes.html", cat_list = list(mongo.db.recipe_category.find()), recipes=mongo.db.recipes.find())

@app.route("/display_recipe/<recipe_id>")
def display_recipe(recipe_id):
  return render_template("recipe.html", cat_list = list(mongo.db.recipe_category.find()),recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
