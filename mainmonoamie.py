from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import Loginform
from flask_mysqldb import MySQLdb
from flask_table import Table, Col, LinkCol

sqlserverip = '172.31.36.62'
sqlserveruser = 'liftingmonoami'
sqlpass = 'LiftingAnonos2018'
sqlattendanceserver = '127.0.0.1'
app = Flask(__name__)
app.config.from_object(Config)


class tablaasistencia(Table):
    courseid = Col('courseid')
    coursename = Col('coursname')
    dayoftheweek = Col('dayoftheweek')
    teachername = Col('teachername')
    teacherlastname = Col('teacherlastname')
    teacherid = Col('teacherid')
    studentname = Col('studentname')
    studentlastname = Col('studentlastname')
    studentid = Col('studentid')
    weekatt1 = Col('weekatt1')
    weekatt2 = Col('weekatt2')
    weekatt3 = Col('weekatt3')
    weekatt4 = Col('weekatt4')
    weekatt5 = Col('weekatt5')
    weekatt6 = Col('weekatt6')
    weekatt7 = Col('weekatt7')
    weekatt8 = Col('weekatt8')
    weekatt9 = Col('weekatt9')
    weekatt10 = Col('weekatt10')
    weekatt11 = Col('weekatt11')
    weekatt12 = Col('weekatt12')
    weekatt13 = Col('weekatt13')
    weekatt14 = Col('weekatt14')
    weekatt15 = Col('weekatt15')
    classes = ['table', 'table-responsive', 'table-hover']

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
where liftinghands.schedule.course_id is not  null and  liftinghands.students.first_name !='Deleted'
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
    return render_template('dynamictable.html', title='Lista Ninos Matriculados', data = htmlninosmatriculados )




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
where liftinghands.schedule.course_id is null and  liftinghands.students.first_name !='Deleted'
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
where (liftinghands.schedule.course_id is not  null or liftinghands.schedule.course_period_id <=202) and  liftinghands.students.first_name !='Deleted'
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

@app.route('/asistencia', methods=['GET', 'POST'])
def asistencia():

    connectionobj = MySQLdb.connect(host=sqlattendanceserver, user=sqlserveruser, passwd=sqlpass, db='liftingasistencia')
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""SELECT attendanceid,
    courseid,
    coursename,
    dayoftheweek,
    teachername,
    teacherlastname,
    teacherid,
    studentname,
    studentlastname,
    studentid,
    weekatt1,
    weekatt2,
    weekatt3,
    weekatt4,
    weekatt5,
    weekatt6,
    weekatt7,
    weekatt8,
    weekatt9,
    weekatt10,
    weekatt11,
    weekatt12,
    weekatt13, 
    weekatt14,
    weekatt15
    from chicosyhorarios""")
    def makeDictFactory(cursor):
        columnNames = [d[0] for d in cursor.description]
        def createRow(*args):
            return dict(zip(columnNames, args))
        return createRow
    DBcursor.rowfactory = makeDictFactory(DBcursor)
    listaninos = DBcursor.fetchall()
    htmlninosmatriculados = tablaasistencia(listaninos)
    return render_template('dynamictable.html', title='asistencia', data = htmlninosmatriculados )


@app.route('/listabonita', methods=['GET'])
def listabonita():
    class ItemTable(Table):
        Primer_Nombre = Col('Primer_Nombre')
        Apellido = Col('Apellido')
        Segundo_Apellido = Col('Segundo_Apellido')
        Fecha_de_nacimiento = Col('Fecha_de_nacimiento')
        Telefono_Directo = Col('Telefono_Directo')
    
    connectionobj = MySQLdb.connect(host=sqlserverip, user=sqlserveruser, passwd=sqlpass, db='liftinghands', charset='utf8', use_unicode=True, cursorclass=MySQLdb.cursors.DictCursor)
    DBcursor = connectionobj.cursor()
    DBcursor.execute("""
    select 
    studenttable.first_name as 'Primer_Nombre',
    studenttable.last_name as 'Apellido',
    studenttable.CUSTOM_10 as 'Segundo_Apellido',
    studenttable.birthdate as 'Fecha_de_nacimiento',
    studenttable.phone as 'Telefono_Directo'
    from liftinghands.students as studenttable
    left join liftinghands.schedule schedule on studenttable.student_id=schedule.student_id
    left join liftinghands.course_details coursedetails on schedule.course_period_id=coursedetails.course_period_id
    where coursedetails.cp_title  like '%q2%'
    group by studenttable.student_id;
    """)
    listaninos = DBcursor.fetchall()
    tableninos = ItemTable(items)
    return render_template('dynamictable.html', title='ListaBonita', data =tableninos)


if __name__ == '__main__':
    app.run(debug=True)
    application.run(host='0.0.0.0')



