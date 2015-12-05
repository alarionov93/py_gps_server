from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"


@app.route("/gps_data_server", methods=['GET', 'POST'])
def serve():
	if request.method == 'GET':
		param = request.form['test']
		with open("data.log", "a") as f:
			string = str("Recieved parameter: %s \r\n" % param)
			f.write(string)
		return request.form['test']

if __name__ == '__main__':
	app.run()