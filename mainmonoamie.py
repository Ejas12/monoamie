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

    return 'Hola %s' % username

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
liftinghands.students.CUSTOM_15 as 'Direccion',
liftinghands.schedule.course_id
FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablematriculados.html', title='Reporte Test', data=listaninos)



@app.route('/listasdeclases')
def listasdeclases():

    connectionobj = MySQLdb.connect(host='172.31.25.244', user='root', passwd='Anonos123', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT 
profes.first_name as 'Nombre del profe',
profes.last_name as 'Apellido del profe',
coursedetails.course_title as 'Curso',
student.first_name as 'Nombre',
Student.last_name as 'Apellido',
student.CUSTOM_10 as 'Segundo Apellido',
student.phone as 'Telefono directo',
student.CUSTOM_11 as 'Encargado 1',
student.CUSTOM_12 as 'Telefono Encargado 1',
student.CUSTOM_13 as 'Encargado 2',
student.CUSTOM_14 as 'Telefono Encargado 2',
student.CUSTOM_15 as 'Direccion',
coursedetails.cp_title as 'horario'


FROM liftinghands.students  student

left outer JOIN liftinghands.schedule schedule ON student.student_id=schedule.student_id
left outer join liftinghands.course_details coursedetails on schedule.course_id=coursedetails.course_id
left outer join liftinghands.staff profes on coursedetails.teacher_id=profes.staff_id
where schedule.course_id is not  null and  student.first_name !='Deleted'

order by coursedetails.course_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablelistadeclase.html', title='Listas de Clase', data=listaninos)