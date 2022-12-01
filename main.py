from flask import Flask , render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,LoginManager,login_required,logout_user,current_user
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


@app.route('/',methods =['GET','POST'])
def page_login():
    if(request.method == 'POST'):
        username = request.form.get("username")
        password = request.form.get("password")
        user = Register.query.filter_by(username = username).first()
        if(user):
            if(Register.query.filter_by(password = password).first()):
                return redirect(url_for("Home"))
    return render_template("pages-login.html")

@app.route('/home')
def Home():
    return render_template("home.html")



@app.route('/pages-register',methods = ['GET','POST'])
def page_register():
    if(request.method == 'POST'):
        Name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        pword = request.form.get('password')
        if(Name != '' and email !='' and username != '' and pword !=''):
            entry = Register(name = Name, email = email, username = username,password = pword)
            db.session.add(entry)
            db.session.commit()
            return render_template("pages-register.html")
        
    return render_template("pages-register.html")
        
        
if __name__ =="__main__":
    app.run(debug=True)