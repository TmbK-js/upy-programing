numero = int(input("Introduce un número entero: "))

if numero > 0:
    if numero % 2 == 0:
        print(f"El número {numero} es positivo y es PAR.")
    else:
        print(f"El número {numero} es positivo y es IMPAR.")
else:
    print(f"El número {numero} no es un número positivo (es cero o negativo).")