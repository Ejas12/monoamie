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
    student.first_name,
    student.last_name,
    student.phone,
    schedule.course_period_id
    FROM liftinghands.students  student
    join liftinghands.schedule schedule on student.student_id = schedule.student_id;
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
liftinghands.students.CUSTOM_11 as 'Encargado 1',
liftinghands.students.phone as 'Telefono directo',
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
liftinghands.students.phone as 'Telefono directo',
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
    select profes.first_name,
    profes.last_name,
    profes.staff_id,
    profes.email,
    profes.phone,
    horarios.short_name,
    horarios.days,
    horas.start_time,
    horas.end_time,
    detallescurso.course_period_id
    FROM liftinghands.course_details detallescurso
    inner join liftinghands.school_periods horas on detallescurso.period_id = horas.period_id
    join liftinghands.course_periods horarios on detallescurso.course_id = horarios.course_id
    join liftinghands.staff profes on detallescurso.teacher_id = profes.staff_id
    where horarios.title like '%q1%' and horarios.marking_period_id is not null
    group by detallescurso.course_period_id
    order by horarios.short_name;
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




