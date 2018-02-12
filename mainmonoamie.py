from flask import Flask, render_template, flash, redirect
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash('Usuario logueado {},'.format(form.username.data))
        return redirect('/')
    return render_template('Loginform.html', title='Sign In', form=form)


@app.route('/NinosMatriculados')
def reporteNinosMatriculados():

    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.CUSTOM_10 as 'Segundo Apellido',
liftinghands.students.phone as 'Telefono directo',
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1',
liftinghands.students.CUSTOM_13 as 'Encargado 2',
liftinghands.students.CUSTOM_14 as 'Telefono Encargado 2',
liftinghands.schedule.course_id

FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablematriculados.html', title='Reporte Test', data=listaninos)



@app.route('/reportelistas')
def reportelistas():

    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
    """)
    listaninos = DBcursor.fetchall()
    return render_template('tablelistadeclases.html', title='Listas de Clase', data=listaninos)



@app.route('/NOMatriculados')
def reporteNOatriculados():

    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.CUSTOM_10 as 'Segundo Apellido',
liftinghands.students.phone as 'Telefono directo',
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1',
liftinghands.students.CUSTOM_13 as 'Encargado 2',
liftinghands.students.CUSTOM_14 as 'Telefono Encargado 2',
liftinghands.schedule.course_id

FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablematriculados.html', title='Reporte Test', data=listaninos)


@app.route('/Listaconcumples')
def Listaconcumples():

    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.CUSTOM_10 as 'Segundo Apellido',
liftinghands.students.phone as 'Telefono directo',
liftinghands.students.birthdate as 'cumpleanos',
liftinghands.enroll_grade.title as 'Grado',
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1',
liftinghands.students.CUSTOM_13 as 'Encargado 2',
liftinghands.students.CUSTOM_14 as 'Telefono Encargado 2',
liftinghands.students.CUSTOM_15 as 'Direccion',
liftinghands.schedule.course_id as 'courseID'


FROM liftinghands.students

left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
left join liftinghands.enroll_grade on liftinghands.enroll_grade.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;
""")

    listaninos = DBcursor.fetchall()
    return render_template('tablematriculadosconcumples.html', title='Reporte Test', data=listaninos)

@app.route('/listaprofes')
def listaprofes():

    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""    """)
    listaninos = DBcursor.fetchall()
    return render_template('tableprofes.html', title='Reporte Test', data=listaninos)


@app.route('/monkey')
def home():
    return render_template('monkey.html')