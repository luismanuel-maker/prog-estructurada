# Proyecto 2 · Consulta de estudiantes por carné UNI
# Nombre: Luis Manuel Castillo Zeledón
carnes = ["2023-0118U", "2023-0274U", "2023-0391U", "2023-0456U", "2023-0582U",
          "2023-0647U", "2023-0733U", "2023-0819U", "2023-0905U", "2023-1042U",
          "2024-0063U", "2024-0127U", "2024-0215U", "2024-0298U", "2024-0344U",
          "2024-0410U", "2024-0487U", "2024-0535U", "2024-0619U", "2024-0702U",
          "2024-0788U", "2024-0861U", "2025-0034U", "2025-0109U", "2025-0186U",
          "2025-0252U", "2025-0329U", "2025-0413U", "2025-0497U", "2025-0560U"]

nombres = ["María José Rivas Zeledón", "Carlos Andrés Mairena López",
           "Ana Gabriela Espinoza Rugama", "Luis Fernando Obando Castillo",
           "Kevin Josué Blandón Pérez", "Fernanda Isabel Rocha Gutiérrez",
           "José Daniel Talavera Ruiz", "Valeria Sofía Centeno Aráuz",
           "Bryan Alexander Chavarría Mendoza", "Katherine Lucía Herrera Picado",
           "Jorge Luis Moncada Úbeda", "Daniela Alejandra Somarriba Cruz",
           "Eduardo Josué Castellón Vega", "Mariela Auxiliadora Lanuza Torres",
           "Óscar Danilo Pineda Hernández", "Ximena Carolina Galeano Molina",
           "Francisco Javier Ortega Zamora", "Heydi Massiel Matamoros Sáenz",
           "Ernesto Rafael Dávila Membreño", "Gissell Marcela Arana Quintero",
           "Axel Mauricio Jarquín Salgado", "Scarleth Yahoska Romero Huete",
           "Josué David Sequeira Bermúdez", "Camila Fernanda Urbina Narváez",
           "Héctor Manuel Ponce Largaespada", "Yaritza Lisseth Morales Duarte",
           "Marvin Antonio Sandino Flores", "Nohelia Patricia Cerda Valle",
           "Wilber Josué Vílchez Martínez", "Andrea Belén Guevara Mejía"]

carreras = ["Ingeniería en Sistemas", "Ingeniería Civil", "Ingeniería Industrial",
            "Ingeniería Eléctrica", "Ingeniería en Computación", "Arquitectura",
            "Ingeniería en Sistemas", "Ingeniería Química", "Ingeniería Mecánica",
            "Ingeniería Electrónica", "Ingeniería Agrícola", "Ingeniería en Sistemas",
            "Ingeniería Civil", "Ingeniería Industrial", "Ingeniería Eléctrica",
            "Ingeniería en Computación", "Arquitectura", "Ingeniería en Sistemas",
            "Ingeniería Química", "Ingeniería Civil", "Ingeniería Mecánica",
            "Ingeniería Electrónica", "Ingeniería en Sistemas", "Ingeniería Industrial",
            "Ingeniería Agrícola", "Ingeniería en Computación", "Ingeniería Civil",
            "Ingeniería en Sistemas", "Ingeniería Eléctrica", "Arquitectura"]


# revisa que el carné tenga el formato AAAA-NNNNU
def carne_valido(carne):
    if len(carne) != 10:
        return False
    if carne[0:4].isdigit() == False:
        return False
    if carne[4] != "-":
        return False
    if carne[5:9].isdigit() == False:
        return False
    if carne[9] != "U":
        return False
    return True


def busqueda_lineal(lista, buscado):
    comp = 0
    for i in range(len(lista)):
        comp += 1
        if lista[i] == buscado:
            return i, comp
    return -1, comp


def busqueda_binaria(lista, buscado):
    izq = 0
    der = len(lista) - 1
    cont = 0
    while izq <= der:
        medio = (izq + der) // 2
        cont += 1
        if lista[medio] == buscado:
            return medio, cont
        if lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, cont


# lineal pero sin importar mayusculas
def buscar_nombre(lista, buscado):
    comp = 0
    b = buscado.lower()
    for i in range(len(lista)):
        comp += 1
        if lista[i].lower() == b:
            return i, comp
    return -1, comp


# recorre TODA la lista y guarda todas las posiciones donde aparece
def buscar_todos(lista, buscado):
    posiciones = []
    comp = 0
    for i in range(len(lista)):
        comp += 1
        if lista[i] == buscado:
            posiciones.append(i)
    return posiciones, comp


seguir = True
while seguir:
    print()
    print("=== REGISTRO ACADÉMICO UNI · CONSULTA ===")
    print("1. Buscar por carné")
    print("2. Buscar por nombre completo")
    print("3. Listar estudiantes de una carrera")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        c = input("Carné: ")
        if carne_valido(c) == False:
            print("Formato inválido. Ejemplo de carné: 2024-0153U")
        else:
            pb, cb = busqueda_binaria(carnes, c)
            pl, cl = busqueda_lineal(carnes, c)
            if pb == -1:
                print("No se encontró ese carné en el registro.")
                print("Búsqueda lineal : " + str(cl) + " comparaciones")
                print("Búsqueda binaria: " + str(cb) + " comparaciones")
            else:
                print("Estudiante: " + nombres[pb])
                print("Carrera   : " + carreras[pb])
                print("Búsqueda lineal : posición", pl, end=", ")
                print(cl, "comparaciones")
                print("Búsqueda binaria: posición", pb, end=", ")
                print(cb, "comparaciones")

    elif opcion == "2":
        n = input("Nombre completo: ")
        pos, comp = buscar_nombre(nombres, n)
        if pos == -1:
            print("No se encontró ese nombre.")
            print("Búsqueda lineal:", comp, "comparaciones")
        else:
            print("Carné   : " + carnes[pos])
            print("Carrera : " + carreras[pos])
            print("Búsqueda lineal: posición " + str(pos) + ", " + str(comp) + " comparaciones")

    elif opcion == "3":
        carr = input("Carrera: ")
        lista_pos, comp = buscar_todos(carreras, carr)
        for p in lista_pos:
            print("  " + carnes[p] + "  " + nombres[p])
        if len(lista_pos) == 0:
            print("No hay estudiantes de esa carrera (escríbela igual, con tildes).")
        print("Total: " + str(len(lista_pos)) + " estudiantes · " + str(comp) + " comparaciones")

    elif opcion == "4":
        print("Saliendo...")
        seguir = False

    else:
        print("Opción no válida.")