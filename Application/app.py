from flask import Flask, redirect, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Eminfo(db.Model):
    SrNo = db.Column(db.Integer, primary_key=True, nullable=False)
    employee_id = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    DOB = db.Column(db.String)

    def __repr__(self) -> str:
        return f"{self.SrNo} - {self.name}"


@app.route('/', methods=['GET', 'POST'])
def empinfo():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        DOB = request.form['DOB']
        employee = Eminfo(employee_id=employee_id, name=name, DOB=DOB)
        db.session.add(employee)
        db.session.commit()
    employees = Eminfo.query.all()
    return render_template('mainpage.html', employees=employees)


@app.route('/create')
def create():
    employees = Eminfo.query.all()
    return render_template('create.html', employees=employees)


@app.route('/delete/<int:SrNo>')
def delete(SrNo):
    employee = Eminfo.query.filter_by(SrNo=SrNo).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect('/')

@app.route('/Update/<int:SrNo>', methods=['GET', 'POST'])
def update(SrNo):
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        DOB = request.form['DOB']
        employee = Eminfo.query.filter_by(SrNo=SrNo).first()
        employee.employee_id = employee_id
        employee.name = name
        employee.DOB = DOB
        db.session.add(employee)
        db.session.commit()
        return redirect('/')
    employee = Eminfo.query.filter_by(SrNo=SrNo).first()
    return render_template('update.html', employee=employee)
    
if __name__ == "__main__":
    app.run(debug=True, port=8095)
