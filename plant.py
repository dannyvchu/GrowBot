
class Plant():
    def __init__(self, **config):
        for key, val in config.items():
            print(key, val)

def main():
    dic = {"test":1, "this":2}
    plant = Plant(**dic)
main()