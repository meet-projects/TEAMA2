from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, User, Post, Group 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/')
def main():
    return render_template('main_page.html')

@app.route('/signup/')
def signup():
	return render_template('SignUp.html')

@app.route('/home/', methods = ['GET','POST'])
def after_sign_in():
    if request.method == 'GET':
            return render_template('SignUp.html')
    else:
        _name = request.form['name']
        _password = request.form['password']
        _username = request.form['usename']
        _email = request.form['email']
        _birthday = request.form['DOBDay']
        _birthmonth = request.form['DOBMonth']
        _brithyear = request.form['DOBYear']

        user = User(name = _name,password = _password,username = _username,email = _email,birthday = _birthday,birthmonth = _birthmonth,birthyear = _birthyear)
        session.add(user)
        session.commit()
        return redirect(url_for('after_sign_in'))
@app.route('/group/<string:name>/')
def group_page(name):
    return render_template("group_page.html",n=name)
    
    
    







if __name__ == '__main__':
    app.run(debug=True)
