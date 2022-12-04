from flask import Flask , render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,LoginManager,login_required,logout_user,current_user
import json
import os

log_in = 0

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
    
    
class Profile(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50),nullable = False)
    about =db.Column(db.String(100),nullable = False)
    job = db.Column(db.String(50),nullable = False)
    country = db.Column(db.String(50),nullable = False)
    phone =db.Column(db.Integer,nullable = False)
    t_h = db.Column(db.String(50),nullable = False)
    insta_h = db.Column(db.String(50),nullable = False)
    fb_h = db.Column(db.String(50),nullable = False)
    linkd_h = db.Column(db.String(50),nullable = False)
    image = db.Column(db.String(50),nullable = False)


@app.route('/',methods =['GET','POST'])
def page_login():
    if(request.method == 'POST'):
        global u_name
        u_name = request.form.get("username")
        password = request.form.get("password")
        user = Register.query.filter_by(username = u_name).first()
        if(user):
            if(user.password == password):
                return redirect(url_for("Home"))
    return render_template("pages-login.html")

@app.route('/home')
def Home():
    posts = Register.query.filter_by(username = u_name).first()
    return render_template("home.html",post = posts)



@app.route('/pages-register',methods = ['GET','POST'])
def page_register():
    if(request.method == 'POST'):
        Name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        pword = request.form.get('password')
        if(Name != '' and email !='' and username != '' and pword !=''):
            def_set = Profile(username = username,about = para["def_about"],job = para["job"],country = para["country_def"],phone = para["phone"],t_h = para["t_h"],insta_h=para["insta_h"],fb_h=para["fb_h"],linkd_h=para["linkd_h"],image =para["image"])
            entry = Register(name = Name, email = email, username = username,password = pword)
            db.session.add(entry)
            db.session.commit()
            db.session.add(def_set)
            db.session.commit()
            return redirect(url_for("page_login"))
        
    return render_template("pages-register.html")


@app.route('/home/profile')
def profile():
    username = u_name
    posts = Register.query.filter_by(username = username).first()
    profile = Profile.query.filter_by(username = username ).first()
    return render_template('profile.html',post = posts,profile = profile)


@app.route('/home/setting')
@app.route('/home/setting/<id>')
def setting(id = None):
    posts = Register.query.filter_by(username = u_name).first()
    profile = Profile.query.filter_by(username = u_name ).first()
    return render_template('setting.html',post = posts,profile = profile, id = 'profile-edit')
        
        
if __name__ =="__main__":
    app.run(debug=True)