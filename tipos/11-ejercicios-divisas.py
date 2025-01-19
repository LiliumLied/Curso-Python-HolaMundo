print("Bienvenido al conversor de divisas")
cantidad = int(input("Ingresa la cantidad que deseasa convertir"))

USD = cantidad*0.050
EUR = cantidad*0.047
GBP = cantidad*0.039
JPY = cantidad*7.71

print(f"La cantidad ingresada es {cantidad} que equivale a {USD} USD")
print(f"La cantidad ingresada es {cantidad} que equivale a {EUR} EUR")
print(f"La cantidad ingresada es {cantidad} que equivale a {GBP} GBP")
print(f"La cantidad ingresada es {cantidad} que equivale a {JPY} JPY")
