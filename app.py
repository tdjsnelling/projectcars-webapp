# NAME app.py
# DESC main flask application file
# AUTH tom snelling
# YEAR 2016

from flask import Flask, render_template, request
import pcarsListener, json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/getData')
def getData():
	car = pcarsListener.getChannel("mCarName")
	car_class = 
	speed = 
	rpm = 
	max_rpm = 
	gear = 
	oil_temp = 
	oil_pres = 
	water_temp = 
	water_pres = 
	throttle_perc = 
	brake_perc = 
	fuel_level = 
	fuel_capacity = 
	location = 
	variant = 
	length = 
	track_temp = 
	air_temp = 
	wind_spd = 
	fl_tyre_temp = 
	fr_tyre_temp = 
	rl_tyre_temp = 
	rr_tyre_temp = 
	fl_brake_temp = 
	fr_brake_temp = 
	rl_brake_temp = 
	rr_brake_temp =
	aero_dmg = 
	engine_dmg = 
	lap_time = 
	s1_time = 
	s2_time = 
	s3_time = 

	return json.dumps([	car,
						car_class,
						speed,
						rpm,
						max_rpm,
						gear,
						oil_temp,
						oil_pres,
						water_temp,
						water_pres,
						throttle_perc,
						brake_perc,
						fuel_level,
						fuel_capacity,
						location,
						variant,
						length,
						track_temp,
						air_temp,
						wind_spd,
						fl_tyre_temp,
						fr_tyre_temp,
						rl_tyre_temp,
						rr_tyre_temp,
						fl_brake_temp,
						fr_brake_temp,
						rl_brake_temp,
						rr_brake_temp,
						aero_dmg,
						engine_dmg,
						lap_time,
						s1_time,
						s2_time,
						s3_time])

@app.route('/kill')
def kill():
	pcarsListener.terminate()
	return 0

if __name__ == "__main__":
	app.run(debug = True, host='localhost', port=8080, passthrough_errors=True)