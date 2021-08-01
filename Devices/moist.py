# Import Depencies
import time, random


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
        self._power(True)
        # Wait 10 milliseconds
        time.sleep(.01)
        # Read and save the signal from sensor
        self.moistness = self._perc_read(sim=True)
        # Turn off power
        self._power(False)
        # Return value
        return self.moistness

    def _power(self, state):
        # On or Off power
        # use self.pwr_pin
        pass

    def _perc_read(self,sim=False):
        # Convert pin from bit to percent
        # call _analogRead from lib
        return random.randrange(80, 100)
    
