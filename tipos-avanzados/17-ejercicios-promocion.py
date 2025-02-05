def aplicar_promocion(compras):
    clientes_con_promocion = []
    for cliente, monto in compras.items():
        if monto >= 150:
            clientes_con_promocion.append(cliente)
    return clientes_con_promocion


compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180}

clientes_promocion = aplicar_promocion(compras)
print(clientes_promocion)  # ['Cliente1', 'Cliente3']
