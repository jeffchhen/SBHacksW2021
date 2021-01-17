from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
@app.route('/')
def yah():
	return render_template('test3.html')


@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
	return "Query Inserted... !!!"

@app.route("/background_test/")
def background_test():
	print("yah");
	return("nothing");

@app.route("/connectN/")
def connect4_home():
	print("test Connect 4 page");
	return render_template('connect4.html')
@app.route('/test')
def test():
	return render_template('yoinkedfromGH.html')
@app.route('/process', methods=['POST'])
def process():
	email = request.form['email']
	name = request.form['name']
	if name and email:
		newName = name[::-1]
		return jsonify({'name' : newName})
	return jsonify({'error' : 'Missing data!'})
@app.route("/battleship/")
def battleship():
	return render_template('battleship.html')
@app.route("/hungergames/")
def hungergames():
	print("test Connect 4 page");
	return render_template('hungergames.html')
if __name__ == '__main__':
	
	app.run(debug=True)




