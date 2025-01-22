print("Bienvenido al calculador de cambio por tu compra")
costo_producto = int(input("Ingresa la el valor del producto a comprar: "))
cantidad = int(input("Ingresa la cantidad de dinero de tu compra: "))

# cambio = cantidad-costo_producto


if cantidad == costo_producto:
    print(f"La cantidad ingresa es {cantidad}, el costo del producto fue {
          costo_producto}, El cliente ha pagado el monto exacto. no requiere cambio")
elif cantidad < costo_producto:
    resultado = cantidad-costo_producto
    print(f"La cantidad ingresa es {cantidad}, el costo del producto fue {
          costo_producto}, El cliente ha pagado menos. Faltan {resultado} dolares")
elif cantidad > costo_producto:
    resultado = cantidad-costo_producto
    print(f"La cantidad ingresa es {cantidad}, el costo del producto fue {
          costo_producto}, El cliente ha pagado mas. El cambio es {resultado} dolares")
