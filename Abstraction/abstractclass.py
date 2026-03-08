from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("A human can walk,eat and sleep")
class snake(animal):
    def move(self):
        print("snake will slide in the floor")
class dog(animal):
    def move(self):
        print("dogs will bark and bite")
class lion(animal):
    def move(self):
        print("lions will roar")
h=human()
h.move()
l=lion()
l.move()
s=snake()
s.move()
d=dog()
d.move()