def total_cuenta(total, porcentaje):
    descuento = total*(porcentaje/100)
    total_descuento = total-descuento
    return total_descuento


total = 100
descuento = 10
total_final = total_cuenta(total, descuento)
print(f"El  total con el descuento es de : {total_final}")
