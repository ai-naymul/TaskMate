from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCEHMY_DATABSE_URI'] = 'sqlite:///task.db'
# db = SQLAlchemy(app)

# class TaskManager(db.Model):
#     id = db.Column(db.Interger, primary_key=True, nullable=False)
#     task_name = db.Column(db.String(500), nullable=False)

@app.route("/")
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)