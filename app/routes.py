from flask import render_template
from app import app
from app import 
from flask_mysqldb import MySQLdb
from flask_table import Table, Col, LinkCol
from app.models import clasedbasistencia
@app.route('/NinosMatriculados', methods=['GET', 'POST'])
def reporteNinosMatriculados():

    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True)
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
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted' and liftinghands.schedule.marking_period_id != 12
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    class ItemTable(Table):
        liftinghands.students.first_name = Col('liftinghands.students.first_name')
        liftinghands.students.last_name = Col('liftinghands.students.last_name')
        liftinghands.students.CUSTOM_10 = Col('liftinghands.students.CUSTOM_10')
        liftinghands.students.phone = Col('liftinghands.students.phone')
        liftinghands.students.CUSTOM_11 = Col('liftinghands.students.CUSTOM_11')
        liftinghands.students.CUSTOM_12 = Col('liftinghands.students.CUSTOM_12')
        liftinghands.schedule.course_id = Col('liftinghands.schedule.course_id')
        classes = ['table', 'table-responsive', 'table-hover']

    htmlninosmatriculados = ItemTable(listaninos)
    return render_template('dynamictable.html', title='Lista Ninos Matriculados', data = htmlninosmatriculados)




@app.route('/reportelistas', methods=['GET', 'POST'])
def reportelistas():

    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
    SELECT 
    student.first_name,
    student.last_name,
    student.phone,
    detallescurso.course_period_id
    FROM liftinghands.students  student
    join liftinghands.schedule schedule on student.student_id = schedule.student_id
    join liftinghands.course_details detallescurso on schedule.course_id = detallescurso.course_id
    where detallescurso.cp_title like '%q2%';
    """)
    listaninos = DBcursor.fetchall()
    return render_template('tablelistadeclases.html', title='Reporte de alumnos para elaboracion de listas de clase', data=listaninos)



@app.route('/NOMatriculados', methods=['GET', 'POST'])
def reporteNOatriculados():

    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True)
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
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted' and liftinghands.schedule.marking_period_id != 12
group by liftinghands.students.student_id
order by liftinghands.students.student_id;""")
    listaninos = DBcursor.fetchall()
    return render_template('tablematriculados.html', title='Reporte No matriculados', data=listaninos)


@app.route('/Listaconcumples', methods=['GET', 'POST'])
def Listaconcumples():

    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True)
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
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted' and liftinghands.schedule.course_period_id >=202
group by liftinghands.students.student_id
order by liftinghands.students.student_id;
""")

    listaninos = DBcursor.fetchall()
    return render_template('tablematriculadosconcumples.html', title='Reporte de alumnos matriculados con edades y grados', data=listaninos)

@app.route('/listaprofes', methods=['GET', 'POST'])
def listaprofes():

    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True)
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
    where profes.profile = 'Teacher' and detallescurso.cp_title like '%q2%'
    order by detallescurso.course_period_id
    """)
    listaninos = DBcursor.fetchall()
    return render_template('taleprofesfilter.html', title='Reporte de Profes para elaboracion de listas', data=listaninos)


@app.route('/monkey', methods=['GET', 'POST'])
def monkey():
    return render_template('monkey.html')

@app.route('/cantidadcursos', methods=['GET', 'POST'])

def cantidadcursos():
    
    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True)
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


@app.route('/fullschedulelist')

def fullschedulelist():
    searchquery = clasedbasistencia.query.all()
    class ItemTable(Table):
        entryid = Col('Entry ID')
        courseid = Col('Course ID')
        coursename = Col('Course Name')
        dayoftheweek = Col('Day of the week')
        teacherfirstname = Col('First Name')
        teacherlastname = Col('Last Name')
        teacherid = Col('Teacher ID')
        studentfirstname = Col('Student Name')
        studentlastname = Col('Student Lastname')
        studentid = Col('Student Id')
        weekatt1 = Col('week 1')
        weekatt2 = Col('week 2')
        weekatt3 = Col('week 3')
        weekatt4 = Col('week 4')
        weekatt5 = Col('week 5')
        weekatt6 = Col('week 6')
        weekatt7 = Col('week 7')
        weekatt8 = Col('week 8')
        weekatt9 = Col('week 9')
        weekatt10 = Col('week 10')
        weekatt11 = Col('week 11')
        weekatt12 = Col('week 12')
        weekatt13 = Col('week 13')
        weekatt14 = Col('week 14')
        weekatt15 = Col('week 15')
    foundkids = ItemTable(searchquery)
    return render_template ('dynamictable.html', title='Asistencia', data=foundkids)
    


if __name__ == '__main__':
    app.run(debug=True)
    application.run(host='0.0.0.0')



