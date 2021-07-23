# Import Depencies
import time


# Create Moisture Sensor Class
class MoistureSensor():
    def __init__(self, sig_pin, pwr_pin):
        self.sig_pin = sig_pin
        self.pwr_pin = pwr_pin
        self.bits_to_perc = 1.0 # bits/perc
        self.moistness = 0.0 # perc
    
    # Take soil moisture reading
    def read_soil(self):
        # Turn on power
        self._power(pwr_pin, True)
        # Wait 10 milliseconds
        time.sleep(.01)
        # Read and save the signal from sensor
        self.moistness = self._analogRead(sig_pin)
        # Turn off power
        self._power(pwr_pin, False)
        # Return value
        return self.moistness

    def _power(self, pin, state):
        # On or Off power
        pass

    def _perc_read(self, pin):
        # Convert pin from bit to percent
        return 420.69
