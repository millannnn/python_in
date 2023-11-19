class Animal:
    # Primer principio: Abstraccion = Es tomar las caracteristicas mas generales de un objeto
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # metodo abstracto que sera implementado por las clases derivadas

    def get_information(self):
        return f"{self.name} tiene {self.age} años."