from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
	
@app.route('/sum/<int1>/<int2>')
def theSum(int1,int2):
	return "The sum is " + str(int(int1) + int(int2))

@app.route('/birthday')
def birthday():
    return "October 30 1950"

@app.route('/greeting/<name>')
def greeting(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run()
