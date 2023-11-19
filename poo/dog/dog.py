class Dog:
    '''
    Metodo constructor es un metodo que sirve para dar un estado inicial 
    a un objeto cuando este es instanciado
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Guau, Guau!"
    def get_information(self):
        return f"{self.name} tiene {self.age} años"
