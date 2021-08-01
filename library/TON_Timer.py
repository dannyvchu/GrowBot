from datetime import datetime

class TON_Timer():
    def __init__(self, time_ms = 1000):
        self.init_time = datetime.utcnow().timestamp()
        self.time_ms_goal = time_ms
        self.time_elapsed = 0
        self.complete = False

    def start(self, time_ms = 1000):
        # restarts init_time
        self.time_ms = time_ms
        self.complete = False
        self.time_elapsed = 0
        self.init_time = datetime.utcnow().timestamp()
        self.check_time()

    def check_time(self):
        self.time_elapsed = datetime.utcnow().timestamp() - self.init_time

        if self.time_elapsed > self.time_ms_goal:
            self.complete = True
            return True
        else:
            self.complete = False
            return False
