from flask import Flask , render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/gech'
#app.config['SQLALCHEMY_BINDS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = True)
    email = db.Column(db.String(50),nullable = True)
    username = db.Column(db.String(50),nullable = True)
    password = db.Column(db.String(50),nullable = True)


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