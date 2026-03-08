class ferrari:
    def fuel_type(self):
        print("fuel type of the ferrari is petrol")
    def max_speed(self):
        print("max speed of the ferrari is 350km/hr")

class lamborghini:
    def fuel_type(self):
        print("fuel type of the lamborghini is petrol")
    def max_speed(self):
        print("max speed of the lamborghini is 300km/hr")

# create object of the ferrari class
f1 = ferrari()
l1 = lamborghini()

#iterate the objects and call the methods
for car in (f1,l1):
    car.fuel_type()
    car.max_speed()
    