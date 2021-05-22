import bmpsensor
import time
from flask import Flask,render_template,Response

app = Flask(__name__)
@app.route('/temperature/')
def gen_temp():
    while True:
        temp,pressure,altitude=bmpsensor.readBmp180()
        print("\nTemperature: %0.1f C" % temp)
        # print("\nHumidity: %0.1f %%" % bme280.humidity)
        print("\nPressure: %0.1f hpa" % pressure)
        print("\nAltitude: %0.2f meters" % altitude)
        tem={'temp':temp,'pressure':pressure,'altitude':altitude}
        return render_template('index.html',**tem)
        time.sleep(2)

'''
@app.route('/get_temp')
def get_temp():
    return Response(gen_temp())
@app.route('/temperature/')
def index():
    return render_template('index.html')
'''
        
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)
