from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    @abstractmethod
    def printDetails(self):
        pass
    def accelerate(self):
        print("speed up")
    def break_applied(self):
        print("slow down")
#child class
class hatchback(car):
    def printDetails(self):
        print("brand:",self.brand)
        print('model:',self.model)
        print('year:',self.year)
    def sunroof(self):
        print("no sunroof is available")
class suv(car):
    def printDetails(self):
        print('model:',self.model)
        print('brand:',self.brand)
        print('year:',self.year)
    def sunroof(self):
        print("sunroof is available..")

car1=hatchback('audi','x7',2016)
car1.accelerate()
car1.printDetails()
car1.break_applied()
car1.sunroof()
print("---------------")
car2=suv('xuv',700,2020)
car2.accelerate()
car2.printDetails()
car2.sunroof()
car2.break_applied()
