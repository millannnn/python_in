from animals.dog import Dog
from animals.cat import Cat

def main():
    dog = Dog("Cronos", 3, "Labrador")
    cat = Cat("Afrodita", 1, "Negro")

    animals = [dog, cat]

    for animal in animals:
        print(animal.get_information())
        print(animal.make_sound())
        print("------------------")

# si llaman a este archivo lo primero que va a hacer es ejecutar el metodo main
if __name__ == "__main__":
    main()