import csv
from app import app
from app import db
with open("listasasistencia.csv") as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for entry in data:
    newentry = clasedbasistencia(courseid=entry['courseid'], coursename=entry['course_title'], dayoftheweek=entry['days'], teacherfirstname=entry['profefirstname'], teacherlastname=entry['profelastname'], teacherid=entry['staff_id'], studentfirstname=entry['first_name'], studentlastname=entry['last_name'], studentid=entry['student_id'])
    db.session.add(newentry)
    db.session.commit()