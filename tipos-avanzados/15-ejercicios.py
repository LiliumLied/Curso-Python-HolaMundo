string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            char


sin_espacios = quita_espacios(string)
print(sin_espacios)
