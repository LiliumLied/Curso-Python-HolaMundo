print("Bienvenido")

tweet = input("Ingresa tu tweet: ")

while True:
    if not tweet:
        print("No se aceptan tweet vacios")
        break
    elif len(tweet) > 20:
        print("Ha sobrepasado el limite de caracteres")
        break
    elif len(tweet) <= 20:
        print("Tweet ha sido publicado")
        break
    else:
        break
