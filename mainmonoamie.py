from flask import Flask, render_template, flash, redirect
from config import Config
from forms import Loginform
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Anonos123'
app.config['MYSQL_DATABASE_DB'] = 'liftinghands'
app.config['MYSQL_DATABASE_HOST'] = '172.31.25.244'
mysql.init_app(app)

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
    connectionobj = mysql.connection.cursor()
    connectionobj.execute("SELECT * FROM liftinghands.students;")
    listaninos = connectionobj.fetchall()
    return str(listaninos)