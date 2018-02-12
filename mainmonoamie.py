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
coursedetails.cp_title as 'horario',
profes.staff_id as 'ProfeId',
coursedetails.course_id as 'courseID'


FROM liftinghands.students  student

left outer JOIN liftinghands.schedule schedule ON student.student_id=schedule.student_id
left outer join liftinghands.course_details coursedetails on schedule.course_id=coursedetails.course_id
left outer join liftinghands.staff profes on coursedetails.teacher_id=profes.staff_id
where profes.staff_id is not  null and  student.first_name !='Deleted'

order by coursedetails.course_id;
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
    DBcursor.execute(""" 
select
profes.first_name as 'profenombre',
profes.last_name as 'profeapellido',
profes.staff_id as 'profeid',
coursedetails.course_title as 'profecurso',
coursedetails.cp_title,
horarios.room as 'aula',
horarios.days as 'profedia',
horas.start_time as 'profehorariostart',
horas.end_time as 'profehorariosend',
coursedetails.course_id as 'courseID'

FROM liftinghands.staff  profes

left outer JOIN liftinghands.course_details coursedetails ON profes.staff_id=coursedetails.teacher_id
left outer join liftinghands.course_periods horarios on coursedetails.course_id=horarios.course_id 
left outer join liftinghands.school_periods horas on horarios.period_id=horas.period_id
where coursedetails.course_id is not null
group by coursedetails.course_id
order by coursedetails.course_id;

   """)
    listaninos = DBcursor.fetchall()
    return render_template('tableprofes.html', title='Reporte Test', data=listaninos)


@app.route('/monkey')
def monkey():
    return render_template('monkey.html')