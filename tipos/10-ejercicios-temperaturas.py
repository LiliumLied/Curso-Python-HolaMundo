print("Bienvenido al conversor de temperatura")
print("Ingresa la temperatura en grados celcius")
celcius = float(input())
fahrenheit = celcius * 9/5 + 32
kelvin = celcius + 273.15

print(f"Temperatura en grados Celcius {celcius}")
print(f"Temperatura en grados Fahrenheit {fahrenheit}")
print(f"Temperatura en grados Kelvin {kelvin}")
