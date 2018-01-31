from flask import Flask, render_template, flash, redirect
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb


app = Flask(__name__)


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
    DBcursor.execute("SELECT liftinghands.students.first_name as 'Nombre',liftinghands.students.last_name as 'Apellido', liftinghands.students.CUSTOM_10 as 'Segundo Apellido', liftinghands.students.phone as 'Telefono directo', liftinghands.students.CUSTOM_11 as 'Encargado 1', liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1', liftinghands.students.CUSTOM_13 as 'Encargado 2', liftinghands.students.CUSTOM_14 as 'Telefono Encargado 2', liftinghands.students.CUSTOM_15 as 'Direccion' FROM liftinghands.students;")
    listaninos = DBcursor.fetchall()
    return render_template('table.html', title='Reporte Test', data=listaninos)