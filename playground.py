from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
@app.route('/')
def yah():
	print("yah");
	return render_template('home.html')


@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
	return "Query Inserted... !!!"

@app.route("/background_test/")
def background_test():
	print("yah");
	return("nothing");

@app.route("/connect4/<value>/")
def connect4_home(value):
	print("test Connect 4 page");
	return render_template('connect4.html')
if __name__ == '__main__':
	
	app.run(debug=True)




