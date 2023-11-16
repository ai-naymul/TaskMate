from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SECRET_KEY'] = 'munnabhaibcs'
db = SQLAlchemy(app)

class TaskManager(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task_name = db.Column(db.String(500), nullable=False)

class MyForm(FlaskForm):
    checkbox = BooleanField('Check me out')
    submit = SubmitField('Add')


@app.route("/", methods=['GET','POST'])
def index():
    form = MyForm()
    tasks = TaskManager.query.all()
    if request.method == 'POST':
        task = request.form.get('task')
        if task:  # Check if task is not empty
            new_task = TaskManager(task_name=task)
            db.session.add(new_task)
            db.session.commit()
    
    return render_template('index.html', tasks=tasks, form=form)

@app.route("/delete_task/<int:task_id>", methods=['POST'])
def delete_task(task_id):
    task = TaskManager.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    print("Running")