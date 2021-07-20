

class Temperature():
    def __init__(self, pin, unit = 'F'):
        self.pin = pin
        self.unit = unit

    def get_temp_f(self):
        return 75

    def get_temp_c(self):
        return self.get_temp_f() * 5/9 - 32


def main():
    temp = Temperature(1, unit = 'F')
    temp_arr = []
    for i in range(5000):
        temp_arr.append(Temperature(i, unit = 'F'))
        print(temp_arr[i].pin)


