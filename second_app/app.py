from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
app.secret_key = "Secret Key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pwsd = db.Column(db.String(100))

    def __init__(self, name, pwsd):
     self.name = name
     self.pwsd  = pwsd











@app.route('/')
def index():
	return render_template('index.html')


@app.route('/service', methods=["GET"])
def service():
	uname = request.args.get('uname')
	pswd = request.args.get('pswd')
	return render_template('service.html', name = uname, password = pswd)

@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/main')
def main():
	return render_template('main.html')


@app.route('/registration')
def Registration():
	all_data = Data.query.all()
	return render_template('registration.html', employees=all_data)




@app.route('/insert', methods=['POST'])
def insert():

	if request.method == "POST":

		name = request.form['name']
		pwsd = request.form['pwsd']

		my_data = Data(name,pwsd)
		db.session.add(my_data)
		db.session.commit()

		flash("Data are successfull inserted")

		return redirect(url_for('Registration'))




@app.route('/update', methods=['GET','POST'])
def update():

	if request.method == "POST":

		my_data = Data.query.get(request.form.get('id'))

		my_data.name = request.form['name']
		my_data.pwsd = request.form['pwsd']

		db.session.commit()

		flash("Data are Updated Successfull")

		return redirect(url_for('Registration'))



@app.route('/delete/<id>/', methods=['GET','POST'])
def delete(id):
  my_data = Data.query.get(id)
  db.session.delete(my_data)
  db.session.commit()
  flash("Data are Successfully Deleted")
  return redirect(url_for('Registration'))



if __name__ == "__main__":
	app.run(debug=True)
