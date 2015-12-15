from flask import Flask, request, jsonify
import models
import config

app = Flask(__name__)


def write_to_log(data):
    with open(config.log_file, "a") as f:
        f.write("Recieved parameter: %s \r\n" % data)

def write_to_db(lat, lon):
    point = models.Point()
    point.lat = lat
    point.lon = lon
    point.save()



@app.route("/")
def hello():
    return "Hello World!"


@app.route("/gps", methods=['GET', 'POST'])
def serve():
    lat_raw = request.args.get('latitude', '')
    lon_raw = request.args.get('longitude', '')

    if not lat_raw or not lon_raw:
        lat_raw = request.args.get('lat', '')
        lon_raw = request.args.get('lon', '')

        if not lat_raw or not lon_raw:
            return jsonify({
                'error': 400,
                'message': 'Bad request. Provide lat-lon or latitude-longitude',
            })

    lat = float(lat_raw)
    lon = float(lon_raw)

    write_to_db(lat, lon)

    return jsonify({'error': 0, 'lat': lat, 'lon': lon})


@app.route('/list', methods=['GET',])
def list():
    points = models.Point.select().order_by(models.Point.created_at.desc())
    data = [point.json for point in points]

    return jsonify({
        'points': data,
        'error': 0,
    })


if __name__ == '__main__':
    app.run(debug=True)
