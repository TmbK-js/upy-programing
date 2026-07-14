numero = float(input("Introduce el número a evaluar: "))
limite_inferior = float(input("Introduce el límite inferior del rango: "))
limite_superior = float(input("Introduce el límite superior del rango: "))

if numero >= limite_inferior and numero <= limite_superior:
    print(f"El número {numero} está DENTRO del rango [{limite_inferior}, {limite_superior}].")
else:
    print(f"El número {numero} está FUERA del rango [{limite_inferior}, {limite_superior}].")