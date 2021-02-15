Qwiic_Soil_Moisture_Sensor_Py
===============

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-soil-moisture-sensor/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun_qwiic_soil_moisture_sensor.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Soil_Moisture_Sensor_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_Soil_Moisture_Sensor_Py.svg" /></a>
	<a href="https://qwiic-soil-moisture-sensor-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-soil-moisture-sensor-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Soil_Moisture_Sensor_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>

</p>

<img src="https://cdn.sparkfun.com/assets/parts/1/6/8/4/8/17731-SparkFun_Qwiic_Soil_Moisture_Sensor-01.jpg"  align="right" width=300 alt="SparkFun Qwiic Soil Moisture Sensor">


Python module for the [SparkFun Qwiic Soil Moisture Sensor](https://www.sparkfun.com/products/17731)

This python package is a port of the existing [SparkFun Soil Moisture Sensor Arduino Examples](https://github.com/sparkfun/Zio-Qwiic-Soil-Moisture-Sensor/tree/master/Firmware/Qwiic%20Soil%20Moisture%20Sensor%20Examples)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

### :warning: **Using this sensor on a Raspberry Pi**? :warning:
Your system might need modification. See this [note](#raspberry-pi-use).

## Contents

* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The qwiic Soil Moisture Sensor Python package current supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)
* [NVidia Jetson Nano](https://www.sparkfun.com/products/15297)
* [Google Coral Development Board](https://www.sparkfun.com/products/15318)

Dependencies
--------------
This driver package depends on the qwiic I2C driver:
[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun qwiic Soil Moisture Sensor module documentation is hosted at [ReadTheDocs](https://qwiic-soil-moisture-sensor-py.readthedocs.io/en/latest/?)

Installation
---------------
### PyPi Installation

This repository is hosted on PyPi as the [sparkfun-qwiic-soil-moisture-sensor](https://pypi.org/project/sparkfun-qwiic-soil-moisture-sensor/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-soil_moisture_sensor
```
For the current user:

```sh
pip install sparkfun-qwiic-soil_moisture_sensor
```
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun_qwiic_soil_moisture_sensor-<version>.tar.gz
```

Example Use
 -------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import qwiic_soil_moisture_sensor
import time
import sys

def runExample():

	print("\nSparkFun qwiic soil moisture sensor Example 1\n")
	mySoilSensor = qwiic_soil_moisture_sensor.QwiicSoilMoistureSensor()

	if mySoilSensor.connected == False:
		print("The Qwiic Soil Moisture Sensor device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySoilSensor.begin()

	print("Initialized.")

	while True:
		mySoilSensor.read_results()
		print (mySoilSensor.level)
		mySoilSensor.LEDon()
		time.sleep(1)
		mySoilSensor.LEDoff()
		time.sleep(1)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)


```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
