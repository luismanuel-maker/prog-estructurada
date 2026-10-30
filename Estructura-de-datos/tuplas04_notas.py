notas = (85, 72, 90, 72, 64, 90, 72, 58)

print("Cantidad de notas:", len(notas))
print("Veces que aparece 72:", notas.count(72))
print("Primera posición del 90:", notas.index(90))
print("¿Hay algún 100?:", 100 in notas)

aprobados = 0
for nota in notas:
    if nota >= 60:
        aprobados += 1
reprobados = len(notas) - aprobados

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)