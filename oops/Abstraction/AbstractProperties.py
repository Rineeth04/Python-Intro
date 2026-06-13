from abc import ABC,abstractmethod
class car(ABC):
    @property
    @abstractmethod
    def brand(self):
        pass
class hatchback(car):
    @property
    def brand(self):
        return "audi"

#c = car()
h= hatchback()
print("brand of the hatchback car is:",h.brand)

