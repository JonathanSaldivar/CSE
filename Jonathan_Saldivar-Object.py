class Car(object):
    def __init__(self, wheels, colour="Red", extra_gas=15):
        self.engine = "honda"
        self.wheels = wheels
        self.transmission = "manual"
        self.gas_left = extra_gas
        self.color = colour
        self.functioning = True

    def add_gas(self, time):
        if self.functioning:
            if self.gas_left >= 15:
                print("The car is already full on gas")
                return

            self.gas_left += time
            if self.gas_left > 15:
                print("The car gets gas.")
                self.gas_left = 15

            else:
                print("The car is now at %d%% " % self.gas_left)
        else:
            print("The car does not drive no more.")

    def crash(self, time):
        self.functioning = False
        print("I drove the car...")
        print()
        print("And crashed it to the wall")
