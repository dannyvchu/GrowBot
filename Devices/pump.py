# this object contains all the methods to control a peristaltic pump
from Library import TON_Timer
import time


class PeristalticPump():
    def __init__(self, STEP, DIR, MS1, MS2, MS3, ENABLE, **config):
        self.STEP_pin = STEP
        self.DIR_pin = DIR  # low = fwd, high = rev
        self.MS1_pin = MS1
        self.MS2_pin = MS2
        self.MS3_pin = MS3
        self.ENABLE_pin = ENABLE
        self.config_pin = config
        self.deg_per_step = 0.1  # deg/step
        self.motor_dir = 0 # 0 = FWD, 1 = REV
        self.velocity= 1 # rpm
        self.timebase = 1 # ms
        self.timer = TON_Timer()
        self.deg_fb = 0 # angle feedback 
        self.motor_delay_ms = 5 # ms
        self.simulate = True # simulate pin outputs
        self.zero() # Initialize rotation to zero degrees

    def move_vel(self, vel_cmd):
        # Moves the pump in a direction at a constant speed
        # Sign of the vel_cmd indicates direction
        pass

    def move_rel(self, deg_cmd):
        # Moves the pump a specfic number of degrees
        # Sign of the deg_cmd indications direction

        num_steps = deg_cmd / self.deg_per_step

        for i in range(num_steps):
            _step(sim=self.simluate)
            self._delay(self.motor_delay_ms)

        pass

    def zero(self):
        self._zero()


    def _zero(self):
        self.deg_fb = 0

    def _step(self, size = 'full_step', dir = 'fwd', sim = False):
        # digital outputs to achieve a step
        if dir.upper() == 'FWD':
            self.motor_dir = 0
        elif dir.upper() == 'REV':
            self.motor_dir = 1
        else:
            # default forwards
            self.motor_dir = 0

        # write direction to motor driver
        if not sim:
            # write to pins
            self._digitalWrite(self.DIR_pin, self.motor_dir) 

        else:
            self._simulate_step()

        # document open loop change in angle
        if not self.motor_dir:
            self.deg_fb = self.deg_fb + self.deg_per_step
        else:
            self.deg_fb = self.deg_fb - self.deg_per_step

    def _delay(self, ms):
        # returns true when a certain number of seconds have passed
        self.timer.start(ms)

        # sits in endless loop until timer returns true
        while not self.timer.check_time():
            pass

    def _digitalWrite(self, pin, state):
        pass


    def _simulate_step(self):
        print("Stepped Forward")
    