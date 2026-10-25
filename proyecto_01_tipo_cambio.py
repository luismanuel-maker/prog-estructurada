# Proyecto 1 · Tipo de cambio del BCN
# Nombre: Luis Manuel Castillo Zeledón
fechas = ["2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06",
          "2023-10-09", "2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13",
          "2023-10-16", "2023-10-17", "2023-10-18", "2023-10-19", "2023-10-20",
          "2023-10-23", "2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27",
          "2023-10-30", "2023-10-31"]

tasas = [36.4330, 36.4340, 36.4350, 36.4360, 36.4370,
         36.4400, 36.4410, 36.4420, 36.4430, 36.4440,
         36.4470, 36.4480, 36.4490, 36.4500, 36.4510,
         36.4540, 36.4550, 36.4560, 36.4570, 36.4580,
         36.4610, 36.4620]
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
def pedir_monto(mensaje):
    try:
        m = float(input(mensaje))
    except ValueError:
        print("Eso no es un número.")
        return -1
    if m <= 0:
        print("El monto tiene que ser mayor que cero.")
        return -1
    return m


salir = False
while salir == False:
    print()
    print("=== TIPO DE CAMBIO OFICIAL · OCTUBRE 2023 ===")
    print("1. Consultar tipo de cambio de una fecha")
    print("2. Convertir dólares a córdobas")
    print("3. Convertir córdobas a dólares")
    print("4. Salir")
    op = input("Elija una opción: ")

    if op == "1":
        f = input("Fecha (AAAA-MM-DD): ")
        pos_l, comp_l = busqueda_lineal(fechas, f)
        pos_b, comp_b = busqueda_binaria(fechas, f)
        if pos_b == -1:
            print("No hay registro para esa fecha (fin de semana o fuera del período).")
            print("Búsqueda lineal : " + str(comp_l) + " comparaciones")
            print("Búsqueda binaria: " + str(comp_b) + " comparaciones")
        else:
            print("Tipo de cambio: C$ " + f"{tasas[pos_b]:.4f}" + " por US$ 1")
            print("Búsqueda lineal : posición " + str(pos_l) + ", " + str(comp_l) + " comparaciones")
            print("Búsqueda binaria: posición " + str(pos_b) + ", " + str(comp_b) + " comparaciones")

    elif op == "2":
        f = input("Fecha (AAAA-MM-DD): ")
        dolares = pedir_monto("Monto en dólares: ")
        if dolares != -1:
            p, c = busqueda_binaria(fechas, f)
            if p == -1:
                print("No hay registro para esa fecha (fin de semana o fuera del período).")
            else:
                cordobas = dolares * tasas[p]
                print(f"US$ {dolares:.2f} equivalen a C$ {cordobas:.2f}")

    elif op == "3":
        f = input("Fecha (AAAA-MM-DD): ")
        cordobas = pedir_monto("Monto en córdobas: ")
        if cordobas != -1:
            p, c = busqueda_binaria(fechas, f)
            if p == -1:
                print("No hay registro para esa fecha (fin de semana o fuera del período).")
            else:
                dolares = cordobas / tasas[p]
                print(f"C$ {cordobas:.2f} equivalen a US$ {dolares:.2f}")

    elif op == "4":
        print("Hasta luego")
        salir = True

    else:
        print("Opción no válida, intente de nuevo.")