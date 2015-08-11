
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
@app.route('/',methods = ['GET','POST'])
def sign_in():
	if request.method == 'GET':
    		return render_template('main_page.html')
	else:
		users = session.query(User).filter_by(username = request.form['user_name'])
		user = users.filter_by(password = request.form['password']).first()
		if user == None:
			return render_template('main_page.html')
		else:
			return redirect(url_for('after_sign_in', user_id = user.id))

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
		return render_template('after_sign_in.html', groups = _groups_list,placeholder = 'search', user_id=user_id)
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
		return render_template('after_sign_in.html', groups = _groups_list,placeholder = 'no group by that name', user_id=user_id)
	else:
		return redirect(url_for('group_page',name = group_name, post_activity = 0,user_id = user_id))
		
	
    
@app.route('/group/<string:name>/<int:user_id>/<int:post_activity>', methods = ['GET','POST'])
def group_page(name,post_activity,user_id):
	if request.method == 'GET':
		group = session.query(Group).filter_by(name = name).first()
		group_id = group.id
		posts = session.query(Post).filter_by(group_id = group_id)
	    	return render_template("group_page.html",n=name,posts=posts,user_id = user_id)
	else:
		if post_activity == 1:
			return new_post(user_id,name)
		if post_activity == 2:
			return join_group(user_id,name)

def join_group(user_id,name):
	group = session.query(Group).filter_by(name = name).first()
	group_user = GroupUser(userID = user_id, groupID = group.id)
	session.add(group_user)
	session.commit()	
	return redirect(url_for('after_sign_in',user_id = user_id))

def new_post(user_id,name):
	content = request.form['to_post']
	group_id = session.query(Group).filter_by(name = name).first().id
	post = Post(user_poster_id = user_id, group_id = group_id,content = content)
	session.add(post)
	session.commit()
	return redirect(url_for('group_page',name = name,user_id = user_id, post_activity = 0))

@app.route('/profile/<int:user_id>/')
def profile(user_id):
	person_posts = session.query(Post).filter_by(user_poster_id = user_id)
	person=session.query(User).filter_by(id=user_id).first()
	return render_template("profile.html", posts=person_posts,person=person)


@app.route('/add group/<int:user_id>', methods=['GET','POST'])
def add_group(user_id):
	if request.method == 'GET':
		return render_template('add_group.html',user_id = user_id)
	else:
		name = request.form['group_name']
		group = Group(name = name)
  		session.add(group)
		session.commit()
		return redirect(url_for('after_sign_in',user_id = user_id))  
    
    







if __name__ == '__main__':
    app.run(debug=True)
