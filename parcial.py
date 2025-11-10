#Elementos repetidos en una lista
def programa1():
    print("Verificar si no hay elementos repetidos")
    datos = input("Ingrese los elementos separados por espacios: ")
    lista = datos.split()

    if len(lista) == len(set(lista)):
        print("No existen elementos repetidos en la lista.")
    else:
        print("Existen elementos repetidos en la lista.")


#Vocales en una cadena
def programa2():
    print("Buscar cadena con dos o más vocales")
    entrada = input("Ingrese las cadenas separadas por espacios: ")
    lista = entrada.split()
    vocales = "aeiouAEIOU"
    encontrada = False

    for palabra in lista:
        contador = 0
        for letra in palabra:
            if letra in vocales:
                contador += 1
        if contador >= 2:
            print("La cadena con dos o más vocales es:", palabra)
            encontrada = True
            break

    if not encontrada:
        print("No existe")


#comparador de listas
def programa3():
    print("Elementos que están en la primera lista y no en la segunda")
    lista1 = input("Ingrese los elementos de la primera lista separados por espacios: ").split()
    lista2 = input("Ingrese los elementos de la segunda lista separados por espacios: ").split()

    resultado = []

    for elemento in lista1:
        if elemento not in lista2:
            resultado.append(elemento)

    print("Elementos que están en la primera lista y no en la segunda:", resultado)

#Promedio de array
def programa4():
    print("Calcular el promedio de un arreglo")
    entrada = input("Ingrese los números separados por espacios: ")
    lista = [float(x) for x in entrada.split()]

    suma = 0
    for num in lista:
        suma += num

    promedio = suma / len(lista)
    print("El promedio del arreglo es:", promedio)


def main():
    programa1()
    programa2()
    programa3()
    programa4()


main()
