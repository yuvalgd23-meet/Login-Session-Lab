from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['POST', 'GET']) # What methods are needed?
def home():

		if request.method == 'POST':
			try:
				in1 = request.form['fq']
				login_session['fq'] = request.form['fq']
				in2 = request.form['q']
				login_session['q'] = request.form['q']
				in3 = request.form['aa']
				login_session['aa'] = request.form['aa']
				if login_session['fq'] == '' or login_session['q'] == '' or login_session['aa'] == '':
					return redirect(url_for("error"))
				else:
					return render_template('thanks.html')
			except: 
				return render_template('error.html')
	
		else:
			return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', login_session = login_session) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html', login_session = login_session)


if __name__ == '__main__':
	app.run(debug=True)