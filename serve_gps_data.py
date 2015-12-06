from flask import Flask, request, jsonify
import config

app = Flask(__name__)

def write_to_log(data):
	with open(config.log_file, "a") as f:
		f.write("Recieved parameter: %s \r\n" % data)


@app.route("/")
def hello():
	return "Hello World!"


@app.route("/gps", methods=['GET', 'POST'])
def serve():
	p = ""

	if request.method == 'GET':
		p = request.args.get(config.wait_for_param, 'NULL_GET')

	if request.method == 'POST':
		p = request.form.get(config.wait_for_param, 'NULL_POST')

	write_to_log(p)

	return jsonify({'error': 0, 'message': p})


if __name__ == '__main__':
	app.run(debug=True)