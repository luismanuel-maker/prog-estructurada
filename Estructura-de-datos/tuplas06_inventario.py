inventario = (
    ("Café molido 400 g", 145.00, 30),
    ("Arroz 1 lb", 18.50, 120),
    ("Frijol rojo 1 lb", 32.00, 85),
    ("Aceite 1 L", 78.00, 0),
    ("Azúcar 1 lb", 20.00, 60),
)

valor_total = 0
for nombre, precio, existencia in inventario:
    print(f"{nombre} | C$ {precio:.2f} | {existencia} unidades")
    valor_total += precio * existencia

print(f"Valor total del inventario: C$ {valor_total:.2f}")
print("Productos agotados:")
for nombre, precio, existencia in inventario:
    if existencia == 0:
        print(f"  {nombre}")