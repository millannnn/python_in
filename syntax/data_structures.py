# -------------------------- Estructuras de datos -------------------

"""------------- Listas ----------------
* Sintaxis: [elemento1, element2, ... , elementoN]
* Las listas son colecciones ordenadas y mutables de elementos.
* Puedes agregar, eliminar y modificar elementos despues de haber creado la lista.
* Se accede a los elementos mediante indices (que comienzan desde 0)
"""

lista = [1, 2, 'tres', 4.0, True]
lista.append(5) # agrega un elemento al final
lista[2] = "nuevo" #modifica un elemento
del lista[1] # elimina un elemento por indice
lista[4] # Acceder a la posicion 4 de la lista

print("Lista:")
print(lista)
print(lista[4])

"""-------------- Tuplas -----------
* Sintaxis: (elemento1, elemento2, ... , elementoN)
* Las tuplas son coleccione ordenadas e inmutables de elementos.
* No puedes cambiar el contenido de una tupla despues de haberla creado.
* Se accede a los elementos mediante indices (que comienzan desde 0)
"""

tupla = (1, 2, 'tres', 4.0, True)
valor = tupla[2] # Accede a un elemento por indice

"""------------------ Diccionarios ------------
* Sintaxis: {
    clave1 : valor1,
    clave2 : valor2,
    ... ,
    claveN : valorN
}

* Los diccionarios son colecciones no ordenadas de pares clave-valor.
* Puedes agregar, eliminar y modificar elementos.
* Se accede a los valores mediante claves, no indices.
"""

diccionario= {
    'clave1': 'valor1',
    'clave2': 42,
    'clave3': [1, 2, 3]
}

print("Diccionario")
print(diccionario)

diccionario['clave4'] = 'nuevo valor' # Agrega un nuevo par clave-valor.
del diccionario['clave1'] # Elimina un par clave-valor por clave
