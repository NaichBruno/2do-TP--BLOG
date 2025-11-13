#SELECCIÓN
lista1 = [5, 2, 9, 1, 7]

for i in range(len(lista1)):
    indice_menor = i
    for j in range(i + 1, len(lista1)):
        if lista1[j] < lista1[indice_menor]:
            indice_menor = j
    aux = lista1[i]
    lista1[i] = lista1[indice_menor]
    lista1[indice_menor] = aux

print(lista1)


print("Ordenada por selección:", lista1)


#INSERCIÓN
lista2 = [8, 3, 6, 4, 2]

for i in range(1, len(lista2)):
    valor = lista2[i]
    j = i - 1
    while j >= 0 and lista2[j] > valor:
        lista2[j + 1] = lista2[j]
        j -= 1
    lista2[j + 1] = valor

print("Ordenada por inserción:", lista2)


#BURBUJEO
lista3 = [10, 15, 5, 20, 0]

for i in range(len(lista3)):
    for j in range(0, len(lista3) - i - 1):
        if lista3[j] > lista3[j + 1]:
            aux = lista3[j]
            lista3[j] = lista3[j + 1]
            lista3[j + 1] = aux

print(lista3)


print("Ordenada por burbujeo:", lista3)


"""
En la lista 1 para que sea de forma descendente seria: if lista [j] > lista [indice_mayor]:
En la lista 2 para que sea de forma descendente seria: while j >= 0 and lista [j] < valor: 
En la lista 3 para que sea de forma descendente seria: if lista [j] < lista [j + 1]:
"""
