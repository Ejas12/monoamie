from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb
from flask_table import Table, Col, LinkCol

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/NinosMatriculados', methods=['GET', 'POST'])
def reporteNinosMatriculados():

    connectionobj = MySQLdb.connect(host='172.26.6.27', user='root', passwd='289av9SeNTbW', db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
SELECT liftinghands.students.first_name as 'Nombre',
liftinghands.students.last_name as 'Apellido',
liftinghands.students.CUSTOM_10 as 'Segundo_Apellido',
liftinghands.students.phone as 'Telefono_directo',
liftinghands.students.CUSTOM_11 as 'Encargado_1',
liftinghands.students.CUSTOM_12 as 'Telefono_Encargado_1',
liftinghands.schedule.course_id as 'Course_ID'

FROM liftinghands.students
left  JOIN liftinghands.schedule ON liftinghands.schedule.student_id=liftinghands.students.student_id
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    class ItemTable(Table):
        Nombre = Col('Nombre')
        Apellido = Col('Apellido')
        Segundo_Apellido = ('Segundo_Apellido')
        Telefono_directo = ('Telefono_directo')
        Encargado_1 = ('Encargado_1')
        Telefono_Encargado_1 = ('Telefono_Encargado_1')
        Course_ID = ('Course_ID')


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
    detallescurso.course_period_id
    FROM liftinghands.students  student
    join liftinghands.schedule schedule on student.student_id = schedule.student_id
    join liftinghands.course_details detallescurso on schedule.course_id = detallescurso.course_id;
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
    DBcursor.execute("""select
    profes.first_name,
    profes.last_name,
    profes.phone,
    profes.email,
    profes.staff_id,
    detallescurso.course_title,
    detallescurso.cp_title,
    detallescurso.course_period_id,
    tabladias.days,
    periodos.start_time,
    periodos.end_time
    from liftinghands.staff profes
    left outer join liftinghands.course_details detallescurso on (detallescurso.teacher_id = profes.staff_id or detallescurso.secondary_teacher_id = profes.staff_id)
    join liftinghands.school_periods periodos on periodos.period_id = detallescurso.period_id
    join liftinghands.course_periods tabladias on tabladias.course_period_id = detallescurso.course_period_id
    where profes.profile = 'Teacher' and detallescurso.cp_title like '%q1%'
    order by detallescurso.course_period_id
    """)
    listaninos = DBcursor.fetchall()
    return render_template('taleprofesfilter.html', title='Reporte de Profes para elaboracion de listas', data=listaninos)


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




