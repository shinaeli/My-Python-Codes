class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        self.battery_size = 100

    def get_range(self):
        if self.battery_size == 75:
            range = 260
            print(f"This car can go about {range} miles on a full charge.")
        elif self.battery_size == 100:
            range = 315
            print(f"This car can go about {range} miles on a full charge.")
        else:
            print(f'No range exists for {self.battery_size}.')


battery1, battery2, battery3 = Battery(75), Battery(100), Battery(175)
battery1.describe_battery()
battery2.describe_battery()
battery3.describe_battery()
battery1.get_range()
battery2.get_range()
battery3.get_range()

# This car has a 75-kWh battery.
# This car has a 100-kWh battery.
# This car has a 175-kWh battery.
# This car can go about 260 miles on a full charge.
# This car can go about 315 miles on a full charge.
# No range exists for 175.
