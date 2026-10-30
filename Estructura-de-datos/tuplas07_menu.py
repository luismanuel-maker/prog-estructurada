menu = ("Gallo pinto", "Nacatamal", "Quesillo")
precios = (60.00, 90.00, 70.00)



lista_precios = list(precios)
for i in range(len(lista_precios)):
    lista_precios[i] = round(lista_precios[i] * 1.10, 2)
nuevos_precios = tuple(lista_precios)

menu = menu + ("Vigorón",)

print("Precios originales:", precios)
print("Precios con aumento:", nuevos_precios)
print("Menú ampliado:", menu)
print("Cantidad de platos:", len(menu))
print("¿nuevos_precios es tupla?:", type(nuevos_precios) == tuple)