# ------------------------ Funciones ---------------------
'''
En python, se puede definir funciones utilizando la palabra clave def.
'''

def saludar (nombre):
    mensaje = f"hola,{nombre}!"
    return mensaje

# Llamada a la funcion
nombre = input("como te llamas bebe?\n") # Pedir informacion por consola
resultado_saludo = saludar(nombre)
print(resultado_saludo)