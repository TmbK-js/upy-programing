n = int(input("Introduce un número entero positivo (N): "))

if n > 0:
    suma = 0
    for i in range(1, n + 1):
        suma += i 
    print(f"La suma de todos los números desde 1 hasta {n} es: {suma}")
else:
    print("Por favor, introduce un número entero mayor que 0.")