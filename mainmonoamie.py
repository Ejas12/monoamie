from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/NinosMatriculados', methods=['GET', 'POST'])
def reporteNinosMatriculados():

    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.CUSTOM_10 as 'Segundo Apellido',
liftinghands.students.phone as 'Telefono directo',
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1',
liftinghands.schedule.course_id

FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablematriculados.html', title='Reporte de ninos matriculados', data=listaninos)



@app.route('/reportelistas', methods=['GET', 'POST'])
def reportelistas():

    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
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
    return render_template('tablelistadeclases.html', title='Reporte de alumnos para elaboracion de listas de clase', data=listaninos)



@app.route('/NOMatriculados', methods=['GET', 'POST'])
def reporteNOatriculados():

    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.CUSTOM_10 as 'Segundo Apellido',
liftinghands.students.phone as 'Telefono directo',
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1',
liftinghands.schedule.course_id

FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablematriculados.html', title='Reporte No matriculados', data=listaninos)


@app.route('/Listaconcumples', methods=['GET', 'POST'])
def Listaconcumples():

    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.birthdate as 'cumpleanos',
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.CUSTOM_12 as 'Telefono Encargado 1',
liftinghands.enroll_grade.title as 'Grado',
liftinghands.schedule.course_id as 'courseID'


FROM liftinghands.students

left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
left join liftinghands.enroll_grade on liftinghands.enroll_grade.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;
""")

    listaninos = DBcursor.fetchall()
    return render_template('tablematriculadosconcumples.html', title='Reporte de alumnos matriculados con edades y grados', data=listaninos)

@app.route('/listaprofes', methods=['GET', 'POST'])
def listaprofes():

    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
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
coursedetails.course_id as 'courseID',
profes.email as 'profeemail',
profes.phone as 'profephone'
FROM liftinghands.staff  profes

left outer JOIN liftinghands.course_details coursedetails ON profes.staff_id=coursedetails.teacher_id
left outer join liftinghands.course_periods horarios on coursedetails.course_id=horarios.course_id 
left outer join liftinghands.school_periods horas on horarios.period_id=horas.period_id
where coursedetails.course_id is not null and coursedetails.marking_period_id != '1'
order by coursedetails.course_id desc


   """)
    listaninos = DBcursor.fetchall()
    return render_template('tableprofes.html', title='Reporte de Profes para elaboracion de listas', data=listaninos)


@app.route('/monkey', methods=['GET', 'POST'])
def monkey():
    return render_template('monkey.html')

@app.route('/cantidadcursos', methods=['GET', 'POST'])

def cantidadcursos():
    
    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute(""" 
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
#liftinghands.schedule.course_id,
count(*)
FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.last_name;


   """)
    listaninos = DBcursor.fetchall()
    return render_template('tablecantidadcursos.html', title='Cantidad de cursos matriculados por alumno', data=listaninos)




@app.route("/test")
def test():
    return "<h1 style='color:blue'>Hello There!</h1>"
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash('Usuario logueado {},'.format(form.username.data))
        return redirect('/')
    return render_template('Loginform.html', title='Sign In', form=form)


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    application.run(host='0.0.0.0')




