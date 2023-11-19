edad = 18

"""
podemos usar operadores logicos:
*and = &&
*or = ||
*not = !
"""

if edad < 18:
    print("Eres ,empr de edad, mocoso")
elif edad > 18 and edad < 65:
    print("Eres un adulto")
else:
    print("Eres un anciano.")