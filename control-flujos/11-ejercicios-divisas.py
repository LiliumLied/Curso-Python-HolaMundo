print("Bienvenidos al conversosr de divisas")
print("las divisas son USD, EUR, MXN")

cantidad = float(input("Ingresa cantidad a convertir: "))
# resultado = 0.0

divisa = input("Ingresa tu divisa de origen: ").uper()
if divisa.lower() == "USD":
    euro = cantidad * 0.95
    mxn = cantidad * 20.28
    print(f"La cantidad ingresa es {cantidad}, la divisa de origen {
          divisa}, y sus valores en Euro es: {euro} y en Peso Mexicano {mxn}")
elif divisa.lower() == "EUR":
    usd = cantidad * 1.0526
    mxn = cantidad * 21.36
    print(f"La cantidad ingresa es {cantidad}, la divisa de origen {
          divisa}, y sus valores en Dolar es: {usd} y en Peso Mexicano {mxn}")
else:
    print("Divisa invalida")
