# projectcars-webapp

This is a Python/Flask web app that uses the UDP stream feature in Project CARS to provide useful telemetry and analysis.

The project relies on the library [pcars](https://github.com/jamesremuscat/pcars) from James Muscat to interpret the UDP stream.

## usage

Download and install the pcars library from the link above, as well as flask (`pip install flask`).

Clone this repo, `cd` into it and run `python app.py`.

Navigate your browser to `localhost:8080` and start using! Make sure UDP is enabled in game.

## todo

* ~~stop incomplete laps being detected (lap time = -1.00)~~
* ~~find a better way to detect when a new lap is started~~
* complete shut down method
* colour code tyre/brake temperatures
* create full (read: easy) installer

## screenshots

On desktop:
![desktop01](screenshot/desktop01.png)

And on mobile:
![mobile01](screenshot/mobile01.png)