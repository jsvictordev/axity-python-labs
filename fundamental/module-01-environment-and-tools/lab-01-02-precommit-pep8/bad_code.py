def calcular_total(precio, cantidad):
    resultado = precio * cantidad
    return resultado


def saludar(nombre):
    print("Hola " + nombre)


total = calcular_total(100, 3)
saludar("Victor")
print(total)
