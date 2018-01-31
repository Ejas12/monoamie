from flask import Flask, render_template, flash, redirect
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb


app = Flask(__name__)

m

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hola %s' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash('Usuario logueado {},'.format(form.username.data))
        return redirect('/')
    return render_template('Loginform.html', title='Sign In', form=form)


@app.route('/testreport')
def testreport():
    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands')
    DBcursor = connectionobj.cursor()
    queriedlist = DBcursor.execute("SELECT * FROM liftinghands.students;")
    listaninos = queriedlist.fetchall()
    return str(listaninos)