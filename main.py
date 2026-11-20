def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido al proyecto colaborativo con Git y GitHub."

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    print(saludar(nombre))