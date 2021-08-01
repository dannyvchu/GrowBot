from Devices import moist 

def main():
    sig_pin = 1
    pwr_pin = 2
    m = moist.MoistureSensor(sig_pin, pwr_pin)
    moistness = m.read_soil()
    print("The moistness level is {}%!".format(moistness))



if __name__ == '__main__':
    main()