from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
@app.route('/')
def yah():
	return render_template('home.html')


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
@app.route("/battleship/")
def battleship():
	return render_template('battleship.html')
@app.route("/hungergames/")
def hungergames():
	print("test Connect 4 page");
	return render_template('hungergames.html')
if __name__ == '__main__':
	
	app.run(debug=True)




