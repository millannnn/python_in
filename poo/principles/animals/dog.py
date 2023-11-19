from .animal import Animal

class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def make_sound(self):
        return "Guau, guau"
    
    def get_information(self):
        return f"{self.name} es un perro de raza {self.race} y tiene {self.age} años."