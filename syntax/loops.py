#------------------- Bucles -------------------
# En python, se pueden usar dos tipos principales de bucles: for y while

# * El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, o rango).
frutas = ["manzana", "platano", "uva", "cereza"]

for fruta in frutas:
    print(fruta)

# el bucle while se ejecuta mientras una condicion sea verdadera,
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# ? La sentencia break se utiliza para salir de un bucle antes de que se complete su ejecucion normal.
for fruta in frutas:

    if fruta == 'platano':
        break

    #print (fruta)

# Toda la sentencia continua se utiliza para omiti ek resto del codigo en la iteracion actual y pasar a la siguiente iteracion,
for fruta in frutas:
    if fruta == 'manzana':
        continue

    print(fruta)