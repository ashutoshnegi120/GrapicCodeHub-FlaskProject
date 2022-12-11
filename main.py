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
    
class Post(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    post_id = db.Column(db.String(50),nullable = False)
    question = db.Column(db.String(100000),nullable = False)
    date = db.Column(db.String(50),nullable = False)
    name = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(50),nullable = False)
class Comment(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    comment_id= db.Column(db.String(50),nullable = False)
    post_id_store = db.Column(db.String(100),nullable = False)
    comment_line = db.Column(db.String(500000),nullable = False)
    name = db.Column(db.String(50),nullable = False)
    date = db.Column(db.String(50),nullable = False)
    
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
    list_post = Post.query.filter_by().all()
    return render_template("home.html",post = posts, list_post = list_post)



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


@app.route('/home/profile',methods = ['GET','POST'])
def profile():
    username = u_name
    posts = Register.query.filter_by(username = username).first()
    profile = Profile.query.filter_by(username = username ).first()
    if(request.method == 'POST'):
        if('edit' in request.form ):
            posts.name =  request.form.get("fullName")
            profile.about =  request.form.get("about")
            profile.job = request.form.get("country")
            profile.phone = request.form.get("phone")
            posts.email = request.form.get("email")
            profile.t_h = request.form.get("twitter")
            profile.fb_h = request.form.get("facebook")
            profile.insta_h= request.form.get("instagram")
            profile.linkd_h = request.form.get("linkedin")
            try:
                db.session.commit()
            except:
                return "somting Wrong!!!!"
    return render_template('profile.html',post = posts,profile = profile)


@app.route('/home/setting',methods = ['GET','POST'])
def setting(id = None):
    posts = Register.query.filter_by(username = u_name).first()
    profile = Profile.query.filter_by(username = u_name ).first()
    if(request.method == 'POST'):
        if('edit' in request.form ):
            posts.name =  request.form.get("fullName")
            profile.about =  request.form.get("about")
            profile.job = request.form.get("country")
            profile.phone = request.form.get("phone")
            posts.email = request.form.get("email")
            profile.t_h = request.form.get("twitter")
            profile.fb_h = request.form.get("facebook")
            profile.insta_h= request.form.get("instagram")
            profile.linkd_h = request.form.get("linkedin")
            try:
                db.session.commit()
            except:
                return "somting Wrong!!!!"        
    return render_template('setting.html',post = posts,profile = profile)
        
@app.route('/home/<string:post_id>',methods = ['GET'])
def post_display(post_id):
    posts = Register.query.filter_by(username = u_name).first()
    post_dit = Post.query.filter_by(post_id = post_id).first()
    return render_template("post_comment.html",post = posts,postDisplay = post_dit)    

@app.route('/home/post/<string:post_id>',methods = ['GET'])
def post_display_comment(post_id):
    posts = Register.query.filter_by(username = u_name).first()
    post_dit = Post.query.filter_by(post_id = post_id).first()
    comment_dit = Comment.query.filter_by(post_id_store = post_id).all()
    return render_template("post_with_othercomment.html",post = posts,postDisplay = post_dit,comment = comment_dit)

if __name__ =="__main__":
    app.run(debug=True)