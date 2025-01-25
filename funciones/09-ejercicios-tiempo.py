print("Bienvenidos al conversosr de unidades de tiempo")
print("Las uinidades son Segundos, Minutos, Horas, Dias, Meses y Años")


def a_segundos(cantidad, unidad):
    if unidad == "minutos":
        return cantidad * 60
    elif unidad == "horas":
        return cantidad * 3600
    elif unidad == "dias":
        return cantidad * 86400
    elif unidad == "meses":
        return cantidad * 2592000
    elif unidad == "años":
        return cantidad * 31536000
    else:
        print("Unidad invalida")


def de_segundos(cantidad, unidad):
    if unidad == "minutos":
        return cantidad / 60
    elif unidad == "horas":
        return cantidad / 3600
    elif unidad == "dias":
        return cantidad / 86400
    elif unidad == "meses":
        return cantidad / 2592000
    elif unidad == "años":
        return cantidad / 31536000
    else:
        print("Unidad invalida")


def convertir_tiempo(cantidad, unidad_origen, unidad_destino):
    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)
    if cantidad_en_segundos == "Error":
        return "Unidad de tiempo no válida"
    cantidad_convertida = de_segundos(cantidad_en_segundos, unidad_destino)
    return f"{cantidad} {unidad_origen}(s) son {cantidad_convertida} {unidad_destino}(s)"


print(convertir_tiempo(2, 'meses', 'horas'))
