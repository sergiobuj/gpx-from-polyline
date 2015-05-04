from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

from gpx_from_polyline import polyline_to_gpx

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    params = {}
    if request.method == 'POST':
        try:
            polyline = request.form['polyline'].strip()
            params['polyline'] = polyline
            params['gpx'] = polyline_to_gpx(polyline)

            if request.form['button'] == 'Download':
                response = make_response(params['gpx'])
                response.headers["Content-Disposition"] = "attachment; filename=polylineToGPX.gpx"
                return response

        except Exception as e:
            params['error'] = e


    return render_template('index.html', params=params) # show post template

if __name__ == '__main__':
#    app.debug = True
    app.run(host='0.0.0.0')
