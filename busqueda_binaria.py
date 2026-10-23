#Esta es una prueba
def busqueda_lineal(lista, objetivo):
    i = 0
    while i < len(lista):
        if lista[i] == objetivo:
            return i          # encontrado: devuelve la posición
        i = i + 1
    return -1                 # se recorrió todo sin encontrarlo


precios = [120, 85, 340, 60, 210]
posicion = busqueda_lineal(precios, 340)

if posicion != -1:
    print("Encontrado en el índice", posicion)
else:
    print("El valor no está en la lista")