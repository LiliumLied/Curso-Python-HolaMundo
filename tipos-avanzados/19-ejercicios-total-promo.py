def aplicar_promocion(compras):
    cuentas_cliente_con_promocion = {
        cliente: monto for cliente, monto in compras.items() if monto > 150}

    costo_promocion = 0
    for cliente, monto in cuentas_cliente_con_promocion.items():
        cuentas_cliente_con_promocion[cliente] = round(monto * 0.9, 2)
        costo_promocion += monto - cuentas_cliente_con_promocion[cliente]
    return [costo_promocion]


compras = {'Cliente1': 200,    'Cliente2': 100,    'Cliente3': 180}
costo_promocion = aplicar_promocion(compras)
print(costo_promocion)  # 38.0
