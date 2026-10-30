estudiantes = ("Ana", "Luis", "Carla", "José", "Marta")
notas_grupo = (78, 92, 85, 66, 95)
ranking = sorted(zip(notas_grupo, estudiantes), reverse=True)
for posicion, (nota, nombre) in enumerate(ranking, start=1):
    print(f"{posicion}. {nombre} - {nota}")