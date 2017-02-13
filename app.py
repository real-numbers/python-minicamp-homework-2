from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
	
@app.route('/sum/<int1>/<int2>')
def theSum(int1,int2):
	return str(int1) + " + " + str(int2) + " = " + str(int(int1) + int(int2))
	
@app.route('/product/<int1>/<int2>')
def theProduct(int1,int2):
	return str(int1) + " x " + str(int2) + " = " + str(int(int1) * int(int2))
	
@app.route('/difference/<int1>/<int2>')
def theDifference(int1,int2):
	return str(int1) + " - " + str(int2) + " = " + str(int(int1) - int(int2))

@app.route('/birthday')
def birthday():
    return "October 30 1950"

@app.route('/greeting/<name>')
def greeting(name):
    return "Hello " + name	
	
@app.route('/favoritefoods')
def favorites():
	myFavorites = ['chocolate', 'Pop Tarts', 'squid']
	return jsonify(myFavorites)

if __name__ == "__main__":
    app.run()
