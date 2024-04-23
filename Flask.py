from flask import Flask, render_template, request
from Create_dicts import interventions_dict, slopes, locations, beds, widths, info_dict
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', slope_options=slopes,
                           location_options=locations,
                           bed_condition_options=beds,
                           bed_width_options=widths)

@app.route('/result', methods=['POST'])
def result():
    slope = request.form['slope']
    location = request.form['location']
    bed_condition = request.form['bed_condition']
    bed_width = request.form['bed_width']

    key = (slope, location, bed_condition, bed_width)
    interventions = interventions_dict.get(key, "No intervention found")
    info = info_dict

    return render_template('result.html', interventions=interventions,info=info)

if __name__ == '__main__':
    app.run(debug=True)