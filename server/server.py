from flask import Flask

app = Flask(__name__)

@app.route('/latest-location-data/<int:long>$<int:lat>')
def latest_location_data(long: int, lat: int) -> str:
    return str(long) + " " + str(lat)

app.run()
