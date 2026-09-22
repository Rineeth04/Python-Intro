from abc import ABC,abstractmethod
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class EnglishGreet(Greet):
    def say_hello(self):
        print("Hello!")

class SpanishGreet(Greet):
    def say_hello(self):
        print("¡Hola!")

e = EnglishGreet()
s = SpanishGreet()
print("English Greeting:",e.say_hello())

print("Spanish Greeting:",s.say_hello())
