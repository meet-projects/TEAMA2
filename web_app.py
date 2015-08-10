
from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, User, Post, Group, GroupUser 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/')
def main():
    return render_template('main_page.html')

@app.route('/signup/', methods = ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('SignUp.html')    	
	else:
	        _name = request.form['name']
        	_password = request.form['password']
        	_username = request.form['username']
        	_email = request.form['email']
        	_birthday = request.form['DOBDay']
        	_birthmonth = request.form['DOBMonth']
        	_birthyear = request.form['DOBYear']

        	user = User(name = _name,password = _password,username = _username,email = _email,birthday = _birthday,birthmonth = _birthmonth,birthyear = _birthyear)
        	session.add(user)
        	session.commit()
        	return redirect(url_for('after_sign_in', user_id = user.id))

@app.route('/home/<int:user_id>', methods = ['GET','POST'])
def after_sign_in(user_id):
	if request.method == 'GET':
		_group_user = session.query(GroupUser).filter_by(userID = user_id)
		_groups = session.query(Group)
		_groups_list = []
		for group in _group_user:
			_groups_list.append(_groups.filter_by( id = group.groupID).first()) 
		return render_template('after_sign_in.html', groups = _groups_list,placeholder = 'search')
	else:
		
		return search(user_id)
		
	

def search(user_id):
	group_name = request.form['text1']
	group = session.query(Group).filter_by(name = group_name).first()
	if group==None:
		_group_user = session.query(GroupUser).filter_by(userID = user_id)
		_groups = session.query(Group)
		_groups_list = []
		for group in _group_user:
			_groups_list.append(_groups.filter_by( id = group.groupID).first()) 
		return render_template('after_sign_in.html', groups = _groups_list,placeholder = 'no group by that name')
	else:
		return redirect(url_for('group_page',name = group_name))
		
	
    
@app.route('/group/<string:name>/')
def group_page(name):
    return render_template("group_page.html",n=name)
    
    
    







if __name__ == '__main__':
    app.run(debug=True)
