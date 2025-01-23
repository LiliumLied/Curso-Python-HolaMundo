print("Bienvenidos al conversosr de unidades de tiempo")
print("Las uinidades son Segundos, Minutos, Horas, Dias, Meses y Años")

cantidad = 0


def a_segundos(unidad):
    if unidad == "minutos":
        resultado = cantidad * 60
        print(f"La cantidad de ingresada fue {cantidad} de {
              unidad} que en segundos es {resultado}")
    elif unidad == "horas":
        resultado = cantidad * 3600
        print(f"La cantidad de ingresada fue {cantidad} de {
              unidad} que en segundos es {resultado}")
    elif unidad == "dias":
        resultado = cantidad * 86400
        print(f"La cantidad de ingresada fue {cantidad} de {
              unidad} que en segundos es {resultado}")
    elif unidad == "meses":
        resultado = cantidad * 2592000
        print(f"La cantidad de ingresada fue {cantidad} de {
              unidad} que en segundos es {resultado}")
    elif unidad == "años":
        resultado = cantidad * 31104000
        print(f"La cantidad de ingresada fue {cantidad} de {
              unidad} que en segundos es {resultado}")
    else:
        print("Unidad invalida")          