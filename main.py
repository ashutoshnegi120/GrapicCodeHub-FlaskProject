from flask import Flask , render_template,request
from flask_sqlalchemy import SQLAlchemy
import json

with open("config.json",'r') as config:
    para = json.load(config)['params']

local_server = True
app = Flask(__name__)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = para["local_host"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = para["public_host"]
#app.config['SQLALCHEMY_BINDS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(50),nullable =False)
    username = db.Column(db.String(50),nullable = False)
    password = db.Column(db.String(50),nullable = False)


@app.route('/')
def page_login():
    return render_template("pages-login.html")

@app.route('/pages-register',methods = ['GET','POST'])
def page_register():
    if(request.method == 'POST'):
        Name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        pword = request.form.get('password')
        
        entry = Register(name = Name, email = email, username = username,password = pword)
        db.session.add(entry)
        db.session.commit()
    return render_template("pages-register.html")

if __name__ =="__main__":
    app.run()