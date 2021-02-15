"""
qwiic_soil_moisture_sensor
============
Python module for the [SparkFun Qwiic Soil Moisture Sensor](https://www.sparkfun.com/products/17731)

This python package is a port of the existing [SparkFun Soil Moisture Sensor Arduino Examples](https://github.com/sparkfun/Zio-Qwiic-Soil-Moisture-Sensor/tree/master/Firmware/Qwiic%20Soil%20Moisture%20Sensor%20Examples)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

"""
from __future__ import print_function, division

import qwiic_i2c


#======================================================================
# Define the device name and I2C addresses. These are set in the class defintion
# as class variables, making them avilable without having to create a class instance.
#
#
# The name of this device - note this is private
_DEFAULT_NAME = "Qwiic Soil Moisture Sensor"

# Some devices have multiple available addresses - this is a list of these addresses.
# NOTE: The first address in this list is considered the default I2C address for the
# device.
_AVAILABLE_I2C_ADDRESS = [0x28, 0x29] ###LAC FIX ADDRESSES

# Register addresses
COMMAND_LED_OFF = 0x00
COMMAND_LED_ON = 0x01
COMMAND_CHANGE_ADDRESS = 0x03
COMMAND_GET_VALUE = 0x05
COMMAND_NOTHING_NEW = 0x99
SENSOR_STATUS = 0x3F

class QwiicSoilMoistureSensor(object):
    """
    QwiicSoilMoistureSensor

        :param address: The I2C address to use for the device.
                        If not provided, the default address is used.
        :param i2c_driver: An existing i2c driver object. If not provided
                        a driver object is created.
        :return: The Soil Moisture Sensor device object.
        :rtype: Object
    """
    device_name         = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # Constructor
    def __init__(self, address=None, i2c_driver=None):

        # Did the user specify an I2C address?
        self.address = address if address is not None else self.available_addresses[0]

        # load the I2C driver if one isn't provided
        if i2c_driver is None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c is None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver

    # ----------------------------------
    # is_connected()
    #
    # Is an actual board connected to our system?

    def is_connected(self):
        """
            Determine if a Soil MoistureSensor device is conntected to the system..
            :return: True if the device is connected, otherwise False.
            :rtype: bool
        """        
        return qwiic_i2c.isDeviceConnected(self.address)

    connected = property(is_connected)

    # ----------------------------------
    # begin()
    #
    # Initialize the system/validate the board.
    def begin(self):
        """
            Initialize the operation of the Soil Moisture Sensor module
            :return: Returns true of the initialization was successful, otherwise False.
            :rtype: bool
        """
        
        # Set variables
        self.level = 0

        # Basically return True if we are connected...
        return self.is_connected()

    #****************************************************************************#
    #
    #   Sensor functions
    #
    # ****************************************************************************#
    # Updates the moisture level data
    # Returns nothing
    def read_moisture_level(self):
        """
            Reads the results from the sensor and stores internally
            :rtype: integer

        """
        
        data = self._i2c.readBlock(self.address, COMMAND_GET_VALUE, 2)
        self.level = data[1] << 8 | data[0]
        
    #----------------------------------------------------
    # Checks to see if error bit is set
    def check_status_error(self):
        """
            Returns  if the Error bit on the sensor is set.

            :return: value of Error bit
            :rtype: integer

        """
        # return the status bit
        value = self._i2c.readByte(self.address, SENSOR_STATUS)

        return value & 1 << 0


    # --------------------------------------------------------------
    # led_off()
    #
    # Turn the onboard LED off
    def led_off(self):
        """
            Turn off the onboard LED.
            :return: Nothing
            :rtype: void
        """
        self._i2c.writeCommand(self.address, 0x00)
    
    # --------------------------------------------------------------
    # led_on
    #
    # Turns the onboard LED on
    def led_on(self):
        """
            Turn on the onboard LED.
            :return: Nothing
            :rtype: void
        """
        self._i2c.writeCommand(self.address, 0x01)


    # ----------------------------------------------
    # change_address(newAddress)
    #
    # This function changes the I2C address of the Qwiic Soil Moisture Sensor. The address
    # is written to the memory location in EEPROM that determines its address.
    def change_address(self, newAddress):
        """
        Changes the I2C address of the Qwiic Soil Moisture Sensor reader
            :param newAddress: the new address to set the Soil Moisture Sensor reader to
            :rtype: bool
        """
        if newAddress < 0x07 or newAddress > 0x78:
            return false
        
        self._i2c.writeByte(self.address, COMMAND_CHANGE_ADDRESS, newAddress)
        
        self.address = newAddress



