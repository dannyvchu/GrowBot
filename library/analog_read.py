
def _analogRead(self, bits=1024, sim=False):
    # read straight from hardware
    # returns number of bits from 0 - 100% of the resolution
    if sim:
        reading = random.randrange(0, bits)



    else:
        print("We do not have hardware yet!")
        # use self.sig_pin
        pass