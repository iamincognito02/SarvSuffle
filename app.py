
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

#initialize the database
db=SQLAlchemy(app)

#create database model
class Students(db.Model):
    id= db.Column(db.Integer,primary_key= True)
    name= db.Column(db.String[50], nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    
#CREATE A FUNCTION TO RETURN A STRING WHEN WE ADD SOMETHING
def __repr__(self):
       return '<name %r>' % self.id

@app.route('/')
def root():
    return redirect(url_for("index"))

@app.route('/students', methods=['POST','GET'])
def index():
    title = "students list"
    if request.method == 'POST':
         student_name= request.form['name']
         new_student=Students(name=student_name)
         #push to database
         db.session.add(new_student)
         db.session.commit()
         return redirect('/students')
    else:
        students =Students.query.order_by(Students.date_created)
        return render_template('index.html',students=students)
@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    student_to_update= Students.query.get_or_404(id)
    if request.method == "POST":
        student_to_update.name=request.form['name']
        db.session.commit()
        return redirect('/students')
    else:
        return render_template('update.html',student_to_update=student_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    student_to_delete=Students.query.get_or_404(id)
    db.session.delete(student_to_delete)
    db.session.commit()
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True, port=5000)