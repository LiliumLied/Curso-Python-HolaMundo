def aplicar_promocion(compras):
    clientes_con_promocion = [cliente for cliente,
                              monto in compras.items() if monto > 150]
    cuentas_cliente_con_promocion = {
        cliente: monto for cliente, monto in compras.items() if monto > 150}
    for cliente, monto in cuentas_cliente_con_promocion.items():
        cuentas_cliente_con_promocion[cliente] = round(monto * 0.9, 2)
    return [clientes_con_promocion, cuentas_cliente_con_promocion]


compras = {'Cliente1': 200,    'Cliente2': 100,    'Cliente3': 180}
resultado = aplicar_promocion(compras)
print(resultado)
# [['Cliente1', 'Cliente3'], {'Cliente1': 180.0, 'Cliente3': 162.0}]
