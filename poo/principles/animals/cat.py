from .animal import Animal
# Segundo principio: Herencia = una clase hija puede heredar atributos y comportamientos de una clase padre.
class Cat(Animal):
    def __init__(self, name, age, color):
        # Cuarto Principio: Encapsulamiento = los atributos de la clase estan ocultos para otras clases
        super().__init__(name, age)
        self.color = color
    
    # Tercer principio: Polimorfismo = Muchos comportamientos.
    def make_sound(self):
        return "Miau, Miau!"
    
    """ Sin hacer polimorfismo
    def get_information(self):
    return super().get_information() """

    def get_information(self):
        return f"{self.name} es un gato de color {self.color} y tiene {self.age} años."