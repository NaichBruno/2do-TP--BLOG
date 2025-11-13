import random

# Se define el rango: 
def definir_rango():
    print("Definir rango de energia generada ")
    minimo = int(input("Ingrese el valor minimo: "))
    maximo = int(input("Ingrese el valor maximo: "))
    while maximo <= minimo:
        print("El valor maximo debe ser mayor al minimo.")
        maximo = int(input("Ingrese nuevamente el valor maximo: "))
    return minimo, maximo


# Funcion: Ingresar regiones
# Y se genera la energia aleatoria

def ingresar_regiones(minimo, maximo):
    print("Ingreso de regiones")
    i=0
    regiones = []
    energia = []
    n_regiones = 15
    for i in range(n_regiones):
        nombre = input(f"Ingrese el nombre de la región {i + 1}: ")
        regiones.append(nombre)
        energia_generada = random.randint(minimo, maximo)
        energia.append(energia_generada)
    return regiones, energia


# Funcion: Metodo de ordenamiento burbuja

def ordenar_listas(regiones, energias):
    largo = len(energias)
    for i in range(largo - 1):
        for j in range(0, largo - 1 - i):
            if energias[j] > energias[j + 1]:
                aux = energias[j]
                energias[j] = energias[j + 1]
                energias[j + 1] = aux
                auxx = regiones[j]
                regiones[j] = regiones[j + 1]
                regiones[j + 1] = auxx

# Datos

def datos(regiones, energia):
    max_energia = energia[0]
    indice_max = 0
    for i in range(1, len(energia)):
        if energia[i] > max_energia:
            max_energia = energia[i]
            indice_max = i

    print(f"La región con mayor energía es '{regiones[indice_max]}' con {max_energia}.")

    divisibles = 0
    no_divisibles = 0
    for valor in energia:
        if valor % 5 == 0:
            divisibles = divisibles + 1
        else:
            no_divisibles = no_divisibles + 1

    print(f"Regiones con producción divisible por 5: {divisibles}")
    print(f"Regiones con producción no divisible por 5: {no_divisibles}")

# Función: Búsqueda binaria

def busqueda_binaria(regiones, energia, valor_buscado):
    izquierda = 0
    derecha = len(energia) - 1
    encontrado = False
    posicion_encontrada = -1
    while izquierda <= derecha and not encontrado :
        medio = (izquierda + derecha) // 2
        if energia[medio] == valor_buscado:
            encontrado = True
            posicion_encontrada = medio
        elif energia[medio] < valor_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    if encontrado: 
        print(f"Se encontro una región con {valor_buscado}: {regiones[posicion_encontrada]}.")
    else:
        print(f"No existe ninguna región con {valor_buscado}.")


# PROGRAMA PRINCIPAL
minimo, maximo = definir_rango()

regiones, energia = ingresar_regiones(minimo, maximo)

datos(regiones, energia)

ordenar_listas(regiones, energia)
print("Datos ordenados por produccion de energia:")
for i in range(len(regiones)):
    print(f"{regiones[i]} = {energia[i]}")

valor_buscado = int(input("Ingrese un valor de energia a buscar: "))

busqueda_binaria(regiones, energia, valor_buscado)


print("Fin del programa ")