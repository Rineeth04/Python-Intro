class vehicle:
    def __init__(self,name,brand,color,price):
        self.name = name
        self.brand = brand
        self.color = color
        self.price = price
    def show(self):
        print("details of the vehicle",self.name,self.brand,self.color,self.price)
    
    def max_speed(self):
        print("max speed of the vehicle is 200km/hr")
    
    def change_gear(self):
        print("change gear of the vehicle")

# inherit the vehicle class to child class car
class car(vehicle):
    def max_speed(self):
        return super().max_speed()
        #print("max speed of the car is 250km/hr")
    def change_gear(self):
        return super().change_gear()
       # print("change gear of the car")

#car object
car1 = car("BMW","X5","Black",50000)
car1.show()
car1.max_speed()
car1.change_gear()

#vehicle object
vehicle1 = vehicle("Bike","Honda","Red",10000)
vehicle1.show()
vehicle1.max_speed()
vehicle1.change_gear()
