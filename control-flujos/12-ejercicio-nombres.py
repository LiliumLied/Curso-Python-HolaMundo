print("Bienvenidos")


# primer_nombre = input("Ingresa tu primer nombre: ").capitalize()
# segundo_nombre = input("Ingresa tu segundo nombre: ").capitalize()
# primer_apellido = input("Ingresa tu primer aepllido ").capitalize()
# segundo_apellido = input("Ingresa tu segundo apellido ").capitalize()


primer_nombre = input("Ingresa tu primer nombre: ").capitalize()

if not primer_nombre:
    print("Estos campos no pueden estar vacios")
    exit()
# primer_nombre = input("Ingresa tu primer nombre: ").capitalize()

segundo_nombre = input("Ingresa tu segundo nombre: ").capitalize()

primer_apellido = input("Ingresa tu primer aepllido ").capitalize()

if not primer_apellido:
    print("Estos campos no pueder estar vacios")
    exit()

segundo_apellido = input("Ingresa tu segundo apellido ").capitalize()


NOMBRE_COMPLETO = f"{primer_nombre} {segundo_nombre} {
    primer_apellido} {segundo_apellido}".replace("  ", " ")
print(NOMBRE_COMPLETO)
