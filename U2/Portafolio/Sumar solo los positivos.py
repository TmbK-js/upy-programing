cantidad = int(input("¿Cuántos números deseas ingresar en total?: "))
suma_positivos = 0

for i in range(cantidad):
    num = float(input(f"Ingresa el número {i + 1}: "))
    if num > 0:
        suma_positivos += num  

print(f"La suma de los números positivos ingresados es: {suma_positivos}")