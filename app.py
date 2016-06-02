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
	car = 0
	car_class = 0
	speed = pcarsListener.getChannel("speed")
	rpm = pcarsListener.getChannel("rpm")
	max_rpm = pcarsListener.getChannel("maxRpm")
	gear = pcarsListener.getChannel("gear")
	oil_temp = pcarsListener.getChannel("oilTempCelsius")
	oil_pres = pcarsListener.getChannel("oilPressureKPa")
	water_temp = pcarsListener.getChannel("waterTempCelsius")
	water_pres = pcarsListener.getChannel("waterPressureKPa")
	throttle_perc = pcarsListener.getChannel("throttle")
	brake_perc = pcarsListener.getChannel("brake")
	fuel_level = pcarsListener.getChannel("fuelLevel")
	fuel_capacity = pcarsListener.getChannel("fuelCapacity")
	location = 0
	variant = 0
	length = 0
	track_temp = pcarsListener.getChannel("trackTemperature")
	air_temp = pcarsListener.getChannel("ambientTemperature")
	wind_spd = pcarsListener.getChannel("windSpeed")
	fl_tyre_temp = pcarsListener.getTyre(0, "tyreTemp")
	fr_tyre_temp = pcarsListener.getTyre(1, "tyreTemp")
	rl_tyre_temp = pcarsListener.getTyre(2, "tyreTemp")
	rr_tyre_temp = pcarsListener.getTyre(3, "tyreTemp")
	fl_brake_temp = pcarsListener.getTyre(0, "brakeTempCelsius")
	fr_brake_temp = pcarsListener.getTyre(1, "brakeTempCelsius")
	rl_brake_temp = pcarsListener.getTyre(2, "brakeTempCelsius")
	rr_brake_temp = pcarsListener.getTyre(3, "brakeTempCelsius")
	aero_dmg = pcarsListener.getChannel("aeroDamage")
	engine_dmg = pcarsListener.getChannel("engineDamage")
	lap_time = pcarsListener.getChannel("lastLapTime")
	s1_time = 0
	s2_time = 0
	s3_time = 0

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