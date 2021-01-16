from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
@app.route('/')
def yah():
	print("yah");
	return render_template('test.html')


@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
	return "Query Inserted... !!!"

@app.route("/background_test/")
def background_test():
	print("yah");
	return("nothing");

if __name__ == '__main__':
	
	app.run(debug=True)




