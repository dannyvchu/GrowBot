from pump import PeristalticPump

def main():
    pump = PeristalticPump(1, 2, 3, 4, 5, 6)
    pump.move_rel(2)


if __name__ == "__main__":
    main()