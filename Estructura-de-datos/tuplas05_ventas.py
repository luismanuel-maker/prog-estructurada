dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
ventas = (2450.00, 3120.50, 2890.00, 4100.75, 3675.25, 5230.00, 4810.50)

total = 0
mejor_venta = ventas[0]
mejor_dia = dias[0]
for i in range(len(ventas)):
    total += ventas[i]
    if ventas[i] > mejor_venta:
        mejor_venta = ventas[i]
        mejor_dia = dias[i]

promedio = total / len(ventas)

print(f"Total de la semana: C$ {total:.2f}")
print(f"Promedio diario: C$ {promedio:.2f}")
print(f"Mejor día: {mejor_dia} con C$ {mejor_venta:.2f}")
print("Días sobre el promedio:")
for i in range(len(ventas)):
    if ventas[i] > promedio:
        print(f"  {dias[i]}: C$ {ventas[i]:.2f}")