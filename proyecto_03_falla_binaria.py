# Proyecto 3 Por qué falla el cogigo binario?
# Nombre: Luis Manuel Castillo Zeledón
facturas = [4821, 1307, 9654, 2290, 7716, 3348, 5012, 8875, 1180, 6433, 2957, 7041, 3895, 9210, 5568]
buscados = [8875, 4821, 2290, 7041, 9210, 1180]
def busqueda_lineal(lista, buscado):
    comp = 0
    for i in range(len(lista)):
        comp = comp + 1
        if lista[i] == buscado:
            return i, comp
    return -1, comp
def busqueda_binaria(lista, buscado):
    izq = 0
    der = len(lista) - 1
    comp = 0
    while izq <= der:
        medio = (izq + der) // 2
        comp += 1
        if lista[medio] == buscado:
            return medio, comp
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, comp
def binaria_con_traza(lista, buscado):
    izq = 0
    der = len(lista) - 1
    comp = 0
    vuelta = 1
    while izq <= der:
        medio = (izq + der) // 2
        comp += 1
        print("Vuelta", vuelta, "-> izq =", izq, " der =", der, " medio =", medio, " lista[medio] =", lista[medio])
        if lista[medio] == buscado:
            print("   lo encontré en la posición", medio)
            return medio, comp
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
        vuelta += 1
    print("   ya no quedan candidatos, no está")
    return -1, comp
def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
def busqueda_segura(lista, buscado):
    if esta_ordenada(lista):
        return busqueda_binaria(lista, buscado)
    else:
        return busqueda_lineal(lista, buscado)
print("=== BINARIA SOBRE LISTA DESORDENADA ===")
print("Buscado   Real   Binaria   Comparaciones   Veredicto")
print("-------   ----   -------   -------------   ---------")
for b in buscados:
    real, c1 = busqueda_lineal(facturas, b)
    pos_bin, c2 = busqueda_binaria(facturas, b)
    if pos_bin == real:
        veredicto = "CORRECTO"
    else:
        veredicto = "FALLA"
    print(f"{b:>6}   {real:>4}   {pos_bin:>7}   {c2:>13}   {veredicto}")
print()
print("=== TRAZA BUSCANDO 7041 ===")
binaria_con_traza(facturas, 7041)
print()
print("¿facturas está ordenada?", esta_ordenada(facturas))
print()
print("=== BÚSQUEDA SEGURA ===")
print("Buscado   Real   Segura   Comparaciones   Veredicto")
print("-------   ----   ------   -------------   ---------")
for b in buscados:
    real, c1 = busqueda_lineal(facturas, b)
    pos_seg, c3 = busqueda_segura(facturas, b)
    if pos_seg == real:
        veredicto = "CORRECTO"
    else:
        veredicto = "FALLA"
    print(f"{b:>6}   {real:>4}   {pos_seg:>6}   {c3:>13}   {veredicto}")
facturas_ordenadas = sorted(facturas)
print()
print("=== BINARIA SOBRE LA COPIA ORDENADA ===")
print("¿facturas_ordenadas está ordenada?", esta_ordenada(facturas_ordenadas))
print("Buscado   En la copia   Real en facturas")
print("-------   -----------   ----------------")
for b in buscados:
    en_copia, c = busqueda_binaria(facturas_ordenadas, b)
    real, c1 = busqueda_lineal(facturas, b)
    print(f"{b:>6}   {en_copia:>11}   {real:>16}")